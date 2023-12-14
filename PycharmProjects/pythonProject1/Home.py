import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("Best company")


info = st.text("We are the best automated parts "
               "developers in the pan America .Our services are door to door")

st.header("Our team")

col1,col2,col3 = st.columns(3)

df = pandas.read_csv("data (1).csv")
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.text(row["role"])
        st.image("images1/" + row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.text(row["role"])
        st.image("images1/" + row["image"])

with col3:
    for index,row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.text(row["role"])
        st.image("images1/" + row["image"])






