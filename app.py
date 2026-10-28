
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="centered"
)

# App title
st.title("🎓 Student Performance Dashboard")
st.write("Welcome! Analyze your academic performance.")

# User inputs
name = st.text_input("Enter student name")

maths = st.number_input(
    "Maths marks", min_value=0, max_value=100, value=75
)

science = st.number_input(
    "Science marks", min_value=0, max_value=100, value=80
)

english = st.number_input(
    "English marks", min_value=0, max_value=100, value=85
)

# Calculate results
if st.button("Calculate Results"):
    total = maths + science + english
    percentage = total / 3

    st.subheader("Your Results")

    st.write(f"Student Name: {name or 'Student'}")
    st.metric("Total Marks", f"{total}/300")
    st.metric("Percentage", f"{percentage:.2f}%")

    if percentage >= 90:
        st.success("Excellent performance! 🏆")
    elif percentage >= 60:
        st.info("Good job! Keep improving. 👍")
    else:
        st.warning("Keep practicing. You can do it!")

    # Display chart
    marks_data = pd.DataFrame({
        "Subject": ["Maths", "Science", "English"],
        "Marks": [maths, science, english]
    })

    st.bar_chart(
        marks_data.set_index("Subject")
    )

st.caption("Built with Python and Streamlit")
