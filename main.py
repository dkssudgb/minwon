import streamlit as st
from PIL import Image

st.set_page_config(
        page_title="민원 분류 자동화 ",
        page_icon="🗂️",
        layout="wide",
)

def load_image(img_file):
        img = Image.open(img_file)
        return img

st.title("국민신문고 민원 담당 기관 분류 예측\n")

tab1, tab2 = st.tabs(["개요", "EDA"])

with tab1: 
        st.markdown("""\n**민원**은 국민이 행정기관에 어떤 행위나 답변을 요청하는 다양한 의사표시를 통칭하는 개념으로, 
                행정의 민주화와 신뢰도를 높이고 국민들이 가장 간편하게 이용할 수 있는 행정 구제 수단으로 활용되고 있습니다.
                \n우리는 **국민신문고**를 통해서 온라인으로 편리하게 민원을 신청할 수 있습니다.\n\n\n""")

        area_col1, area_col2, area_col3 = st.columns([0.15, 0.7, 0.15])
        with area_col2:
                img = load_image("./images/국민신문고.png")
                st.image(img, width=700)

        st.markdown("")
        st.markdown("")
        st.markdown("""하지만 아래의 사진과 같이 민원을 신청할 때 선택할 수 있는 민원의 수는 
                \n**공공기관 342곳, 중앙행정기관 55곳, 지방자치단체 17곳, 헌법기관 4곳, 교육기관 3곳으로**
                \n민원인의 입장에서 적절한 처리기관을 찾기는 쉽지 않습니다. """)

        area_col1, area_col2, area_col3 = st.columns([0.15, 0.7, 0.15])
        with area_col2:
                img_minwon = load_image("./images/minwon_req.png")
                st.image(img_minwon, width=500)
                
        st.markdown("")
        st.markdown("")
        st.markdown("""민원을 신청할 때 선택한 기관이 적정 처리 기관이 아닐 경우, 알맞은 담당 기관으로 이송된 후 해당 민원이 처리됩니다.
                \n이 과정에서 민원을 처리하는데 더 많은 시간이 소요되고 민원에 대한 대처가 늦어지게 됩니다. """)

        area_col1, area_col2, area_col3 = st.columns([0.15, 0.7, 0.15])
        with area_col2:
                img = load_image("./images/news.png")
                st.image(img, width=500)


        st.markdown("")
        st.markdown("")
        st.markdown("그래서 저희는 이러한 불편함과 번거로움을 줄이고자")
        st.markdown(""" ### 민원 담당 부서를 지정해주는 모델을 구현해보기로 하였습니다.""")



with tab2:
        area_col1, area_col2 = st.columns(2)
        with area_col1:
                st.markdown("##### 대분류 기준) 민원의 개수")
                img = load_image("./images/대분류.png")
                st.image(img, width=500)
        with area_col2:
                st.markdown("##### 민원 개수 상위 50 기관")
                st.markdown("")
                st.markdown("")
                img = load_image("./images/상위50.png")
                st.image(img, width=500)
        st.markdown("""EDA 결과 5가지 대분류를 기준으로 보았을 때 헌법기관으로 들어온 민원이 없는 것을 알 수 있었고, 
                    \n민원 데이터의 빈도수가 기관 별로 많은 차이를 보이는 것을 확인했습니다.""")
        
        st.markdown('#### \"데이터의 불균형이 심해서 처리 기관(label)을 높은 정확도로 분류하는데 한계가 있다.\" ')
        st.markdown("")
        st.markdown("")
        
        st.markdown("#### 문제점 및 해결 과정")
        st.markdown("""EDA 과정에서 얻은 인사이트를 바탕으로 프로젝트의 방향을 조금씩 수정했습니다. 
                    \n우선 데이터의 불균형으로 총 403개의 처리 기관(label) 값을 모두 알맞게 분류해주기에는 한계가 있다고 판단해, 성질이 비슷한 처리 기관들을 묶어서 분류 label 의 수를 줄이기로 결정했습니다. 
                    \n따라서 공공데이터 포털의 “**기획재정부_공공기관 지정현황”**(시장형 공기업, 준시장형 공기업, 위탁집행형 준정부기관, 기타공공기관에 따른 공공기관명 정보를 제공) 데이터를 추가로 수집하여, 이를 기준으로 크롤링 데이터의 처리 기관을 새롭게 분류했습니다.
                    """)
        st.markdown("(링크: https://www.data.go.kr/data/15088742/fileData.do)")
        
        area_col1, area_col2 = st.columns([0.7, 0.3])
        with area_col1:
                img = load_image("./images/분류new그래프.png")
                st.image(img, width=650)
        with area_col2:
                img = load_image("./images/분류new.png")
                st.image(img, width=250)
                
        st.markdown("""기획재정부 공공기관 지정현황 데이터를 기준으로 민원을 새롭게 분류해 모든 민원에 label 값이 존재하도록 만들었습니다. 
                    \n하지만 각 label의 min-max 값이 2개와 4350개로, 아직 데이터 불균형의 문제를 완전히 해결되지 않아 모델 학습 시 높은 성능을 보이기는 힘들 것이라고 예상했습니다. 
                    \n아쉽지만 프로젝트 기간을 고려해 데이터 전처리는 마무리 하고 아래의 최종 데이터셋으로 프로젝트를 진행했습니다.
                    """)
        
        st.markdown("")
        st.markdown("")
        st.markdown("#### 최종 데이터셋")
        img = load_image("./images/최종data.png")
        st.image(img, width=1000)