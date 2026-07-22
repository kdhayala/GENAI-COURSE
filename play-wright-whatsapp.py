import os
import time
import datetime
import json
import urllib.parse
from pathlib import Path

import pandas as pd
from playwright.sync_api import sync_playwright


def extract_last_messages(page, limit: int = 3):
    elems = page.locator("div.copyable-text")
    texts = [t.strip() for t in elems.all_inner_texts() if t and t.strip()]
    return texts[-limit:][::-1] if texts else []


def send_whatsapp_messages(contacts_path: str, screenshots_dir: str = "screenshots", report_dir: str = "reports"):
    base = Path(__file__).parent
    contacts_file = base / contacts_path
    screenshots_path = base / screenshots_dir
    reports_path = base / report_dir
    screenshots_path.mkdir(parents=True, exist_ok=True)
    reports_path.mkdir(parents=True, exist_ok=True)

    if not contacts_file.exists():
        print(f"Contacts file not found: {contacts_file}")
        return

    df = pd.read_excel(contacts_file)
    df.columns = [c.title() for c in df.columns]
    if not {"Name", "Phone"}.issubset(set(df.columns)):
        print("contacts.xlsx must contain columns: Name, Phone. Optional: Message")
        return

    report_rows = []

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto("https://web.whatsapp.com/")
        print("Please scan the QR code to log in to WhatsApp Web.")
        page.wait_for_selector('div[contenteditable="true"][data-tab]', timeout=120000)

        for _, row in df.iterrows():
            name = str(row.get("Name", "")).strip()
            phone = str(row.get("Phone", "")).strip()
            template = str(row.get("Message", "")) if "Message" in df.columns else ""

            rec = {"name": name, "phone": phone, "message": None, "sent": False, "screenshot": None, "last_messages": [], "error": None, "timestamp": datetime.datetime.now().isoformat()}

            if not phone:
                rec["error"] = "missing phone"
                report_rows.append(rec)
                continue

            message = template.replace("{name}", name) if template else f"Hello {name}, sent at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            rec["message"] = message

            phone_for_url = phone.lstrip("+").replace(" ", "")
            url = f"https://web.whatsapp.com/send?phone={phone_for_url}&text={urllib.parse.quote(message)}"

            try:
                page.goto(url)
                page.wait_for_selector('div[contenteditable="true"][data-tab]', timeout=15000)
                # send message (Enter)
                page.keyboard.press("Enter")
                time.sleep(1.5)
                # screenshot
                ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                safe = name.replace(" ", "_") or phone_for_url
                shot = screenshots_path / f"{safe}_{ts}.png"
                page.screenshot(path=str(shot))
                rec["screenshot"] = str(shot)
                # extract last 3 messages
                rec["last_messages"] = extract_last_messages(page, limit=3)
                # simple sent check: our message appears in last messages
                rec["sent"] = any(message.strip()[:20] in m for m in rec["last_messages"]) if rec["last_messages"] else True
            except Exception as e:
                rec["error"] = str(e)

            report_rows.append(rec)
            time.sleep(2)

    finally:
        try:
            browser.close()
        except Exception:
            pass
        try:
            p.stop()
        except Exception:
            pass

    # save reports (json + excel)
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    jfile = reports_path / f"whatsapp_report_{now}.json"
    xfile = reports_path / f"whatsapp_report_{now}.xlsx"
    with open(jfile, "w", encoding="utf-8") as f:
        json.dump(report_rows, f, ensure_ascii=False, indent=2)
    # to excel
    rows = []
    for r in report_rows:
        rr = r.copy()
        for i in range(3):
            rr[f"last_message_{i+1}"] = r.get("last_messages", [])[i] if len(r.get("last_messages", [])) > i else ""
        rr.pop("last_messages", None)
        rows.append(rr)
    pd.DataFrame(rows).to_excel(xfile, index=False)
    print(f"Reports saved: {jfile}, {xfile}")


if __name__ == "__main__":
    send_whatsapp_messages("contacts.xlsx")


     
