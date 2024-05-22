import streamlit as st

source_code = st.text_area("Source code")
exec(source_code)
