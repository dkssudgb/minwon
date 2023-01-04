import streamlit as st

st.set_page_config(
    page_title="시각화",
    layout="wide",
)

st.markdown("# 시각화")

tab1, tab2 = st.tabs(["민원 데이터", "API 데이터"])

with tab1:
   st.header("민원 데이터 시각화")

with tab2:
   st.header("API 데이터 시각화")
