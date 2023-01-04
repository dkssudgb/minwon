import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="국민신문고 민원 분류 자동화 ",
    page_icon="🔖",
    layout="wide",
)

st.markdown("# EDA")
st.markdown("## 주제 : 국민신문고 민원 분류 자동화 ")

with st.sidebar:
    selected = option_menu("민원데이터 분류", ["홈", "모델 예측 결과", "모델 설명", "시각화"], 
        icons=['home', 'search', "explain", "chart"], menu_icon="menu", default_index=1)
    selected