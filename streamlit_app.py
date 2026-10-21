import requests, streamlit as st

with st.form("quiz"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    answer = st.radio("Your answer", ["A", "B", "C", "D"])
    if st.form_submit_button("Submit"):
        requests.post(st.secrets["SHEET_URL"],
                      json={"name": name, "email": email, "answer": answer})
        st.success("Submitted. Thank you.")
