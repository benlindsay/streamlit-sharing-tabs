import streamlit as st

query_params = st.experimental_get_query_params()

st.write(query_params)