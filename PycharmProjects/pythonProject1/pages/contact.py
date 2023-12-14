import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Me")
df = pandas.read_csv("topics.csv")

with st.form(key="email forms"):
    user_mail = st.text_input("Enter yor email")
    input_options = st.selectbox("what topic you want to discuss?",
                                 df["topic"])
    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: New mail from {user_mail}
From:{user_mail}
Topic:{input_options}
{raw_message}"""
    button = st.form_submit_button("Submit")
    print(button)

    if button:
        send_email(message)
        st.info("The email has been sent successfully")
