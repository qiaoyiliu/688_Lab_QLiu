import streamlit as st

lab1 = st.Page("streamlit_app_lab1.py", title="Lab 1", icon=":material/add_circle:")
lab2 = st.Page("streamlit_app_lab2.py", title="Lab 2", icon=":material/add_circle:")
lab3 = st.Page("streamlit_app_lab3.py", title="Lab 3", icon=":material/add_circle:")
lab4 = st.Page("streamlit_app_lab4.py", title="Lab 4", icon=":material/add_circle:")
lab5 = st.Page("streamlit_app_lab5.py", title="Lab 5", icon=":material/add_circle:")

pg = st.navigation([lab1, lab2, lab3, lab4, lab5])
st.set_page_config(page_title="688Labs", page_icon=":material/edit:")
pg.run()