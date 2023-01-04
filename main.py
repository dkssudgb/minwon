import streamlit as st
# from streamlit_option_menu import option_menu
from PIL import Image
# import pandas as pd
# from PyPDF2 import PdfFileReader
# import os

st.set_page_config(
    page_title="국민신문고 민원 분류 자동화 ",
    page_icon="🔖",
    layout="wide",
)

st.title("국민신문고 민원 담당 기관 분류 예측")
st.header("")
st.subheader("")
st.markdown("# ")

def load_image(img_file):
    img = Image.open(img_file)
    return img

img = load_image("./images/news.png")
st.image(img, width=700)

# with st.sidebar:
#     selected = option_menu("민원데이터 분류", ["홈", "모델 예측 결과", "모델 설명", "시각화"], 
#         icons=['home', 'search', "explain", "chart"], menu_icon="menu", default_index=1)
#     selected