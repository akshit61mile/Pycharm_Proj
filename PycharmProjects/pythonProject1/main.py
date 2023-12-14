import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/WIN_20230406_09_37_20_Pro.jpg")

with col2:
    st.title('Akshit Pathania')
    content=("""Hi my name is Akshit and I am working as system 
    engineer in infosys since Feb 2022""")
    st.write(content)

input_text = st.text("Below are the some of the examples of the apps I have built")

col4,empt_col,col3 = st.columns([1.5,.7,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")











