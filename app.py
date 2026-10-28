
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Personal Expense Tracker")
st.write("Track your daily expenses easily!")

# Initialize expense storage
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Expense input form
with st.form("expense_form"):
    expense_name = st.text_input("Expense name")

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if expense_name.strip() and amount > 0:
            st.session_state.expenses.append({
                "Expense": expense_name,
                "Amount (₹)": amount,
                "Category": category
            })
            st.success("Expense added successfully!")
        else:
            st.error("Enter an expense name and an amount above zero.")

# Show expenses
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    st.subheader("📋 Your Expenses")
    st.dataframe(df, use_container_width=True)

    total = df["Amount (₹)"].sum()
    st.metric("Total Expenses", f"₹{total:,.2f}")

    st.subheader("📊 Expenses by Category")
    category_totals = df.groupby("Category")["Amount (₹)"].sum()
    st.bar_chart(category_totals)

    if st.button("Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()
else:
    st.info("No expenses added yet. Add your first expense above!")

st.caption("Built with Python and Streamlit")
