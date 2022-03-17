import streamlit as st 

st.set_page_config(page_title="PSAS-Web-App", page_icon=":computer:", layout="wide")

with st.container():
    st.subheader("Hi, This is your PSAS Web-App :wave:")
    st.title("Home page")
    st.write(
        "Dashboard for Posture and Occupational Stress Assessment of a Computer User."
    )
    st.write("[Github Repo >](https://github.com/Sooriyakumar23/PSAS-WebApp.git)")