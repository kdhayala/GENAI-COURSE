import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🎓 Student Grade Management",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Management System")
st.markdown("---")

# Session State
if "students" not in st.session_state:
    st.session_state.students = []

# Sidebar
st.sidebar.header("📚 Student Information")

name = st.sidebar.text_input("Student Name")

math = st.sidebar.number_input("Mathematics", 0, 100)
science = st.sidebar.number_input("Science", 0, 100)
english = st.sidebar.number_input("English", 0, 100)
social = st.sidebar.number_input("Social", 0, 100)
computer = st.sidebar.number_input("Computer", 0, 100)

if st.sidebar.button("➕ Add Student"):

    total = math + science + english + social + computer
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if percentage >= 35 else "Fail"

    student = {
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Social": social,
        "Computer": computer,
        "Total": total,
        "Percentage": round(percentage,2),
        "Grade": grade,
        "Status": status
    }

    st.session_state.students.append(student)

    st.success(f"{name} added successfully!")

    if grade in ["A+", "A"]:
        st.balloons()

# Display Records
if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    st.subheader("📋 Student Records")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Students", len(df))
    c2.metric("Average %", round(df["Percentage"].mean(),2))
    c3.metric("Highest %", round(df["Percentage"].max(),2))
    c4.metric("Lowest %", round(df["Percentage"].min(),2))

    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # Search
    st.subheader("🔍 Search Student")

    search = st.text_input("Enter Student Name")

    if search:
        result = df[df["Name"].str.contains(search, case=False)]

        if len(result):
            st.dataframe(result, use_container_width=True)
        else:
            st.warning("Student not found.")

    st.markdown("---")

    # Grade Chart
    st.subheader("📈 Grade Distribution")

    fig = px.histogram(
        df,
        x="Grade",
        color="Grade",
        text_auto=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    csv = df.to_csv(index=False).encode()

    st.download_button(
        "📥 Download Report",
        csv,
        "students.csv",
        "text/csv"
    )

    if st.button("🗑 Clear Records"):
        st.session_state.students=[]
        st.rerun()

else:
    st.info("No student records available. Add students from the sidebar.")