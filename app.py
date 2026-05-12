import streamlit as st

from workflow import app

st.title("Autonomous Reasearch Agent")

query = st.text_input("Enter research topic")

if st.button("Start Research"):

    result = app.invoke({
        "query" : query
    })

    st.subheader("Final Report")
    st.write(result["final_report"])
