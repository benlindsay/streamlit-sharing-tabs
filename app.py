import os

import streamlit as st

STREAMLIT_URL = os.getenv("STREAMLIT_URL", "/")

query_params = st.experimental_get_query_params()

st.write(query_params)

st.markdown("[/](/)")

st.markdown("[/?foo=bar](/?foo=bar)")

st.markdown("[https://share.streamlit.io/benlindsay/streamlit-sharing-tabs/main/app.py?foo=bar](https://share.streamlit.io/benlindsay/streamlit-sharing-tabs/main/app.py?foo=bar)")

st.markdown(f"[{STREAMLIT_URL}?foo=bar]({STREAMLIT_URL}?foo=bar)")
