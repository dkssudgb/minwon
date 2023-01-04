import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="민원분류-결과",
    page_icon="🏷️",
    layout="wide",
)
tab1, tab2, tab3 = st.tabs(["Test결과", "결론", "개선점"])

with tab1: 
    st.title("결과")

    def load_image(img_file):
        img = Image.open(img_file)
        return img

    st.markdown("### BLSTM")
    area_col1, area_col2 = st.columns(2)
    with area_col1:
        st.markdown("##### BLSTM의 정확도")
        img = load_image("./images/blstm_acc.png")
        st.image(img, width=350)
        
    with area_col2:
        st.markdown("##### \tBLSTM의 손실률")
        img = load_image("./images/blstm_loss.png")
        st.image(img, width=350)
        
    st.markdown("""```text
                🧐 0.8675103305785123
                """)
    st.markdown("")

    st.markdown("### GRU")
    area_col1, area_col2 = st.columns(2)
    with area_col1:
        img = load_image("./images/gru_acc.png")
        st.image(img, width=350)
        
    with area_col2:
        img = load_image("./images/gru_loss.png")
        st.image(img, width=350)
        
    st.markdown("""```text
                🧐 0.8928202479338843
                """)
    st.markdown("")



with tab2:
    st.markdown("""
                ##### 1. 불용어
                \n불용어 사전1 38 단어(kkma, okt 각각 명사 추출이 달라서 두 버전으로 작성, 모델 실행 결과 kkma의 정확도가 높아 kkma로 진행), 불용어 사전2 (okt) 607 단어 두 가지로 진행했습니다. accuracy에 있어서 큰 차이는 나타나지 않았습니다. 
                """)
    st.markdown("")
    
    st.markdown("""
                \n##### 2. 형태소 분석
                \n다른 조건을 최대한 비슷하게 맞춰 두고 okt와 kkma를 비교했을 때, kkma를 사용한 모델이 조금 더 높은 정확도를 기록했습니다. 이후 kkma를 적용하기로 결정하고 모델 레이어 구성 변경 등 다양한 시도를 해보았습니다.
                """)
    st.markdown("")
    
    st.markdown("""
                \n##### 3. 모델
                \n- simple RNN, BLSTM, GRU 모델을 사용했습니다. 
                \n- simple RNN은 epoch 3 이후 accuracy가 0.2 수준에 머무르고 개선되지 않아 학습을 중단했습니다. 
                \n- BLSTM 모델의 accuracy는 0.86으로 GRU 모델과 근소하지만 0.03 정도의 차이가 나타났습니다.
                \n- GRU 모델의 성능이 가장 좋았고 가장 높은 accuracy는 0.89 입니다. optimizer는 adam을 사용했을 때보다 rmsprop을 사용했을 때 accuracy가 0.02 정도 높게 나타났습니다.
                """)



with tab3:
    area_col1, area_col2 = st.columns([0.65, 0.35])
    with area_col1:
        st.markdown("")
        st.markdown("")
        st.markdown("""수집한 민원 데이터에서 각 처리기관에 대한 데이터가 많지 않았고, 빈도수 차이가 심해서 **데이터 불균형 문제**가 있었습니다. 
                    \n이에 대한 해결 방안으로 새로운 데이터를 수집하여 **처리기관에 대한 분류를 새롭게** 진행하였고, 완전히 불균형 문제가 해결되지는 않았지만 예상한 것과 달리 GRU 모델을 사용했을 때 accuracy 0.89로 나쁘지 않은 성능을 보였습니다. """)
        st.markdown("")
        st.markdown("""이번 프로젝트로 양질의 데이터가 모델에 상당한 영향을 끼친다는 것을 알게 되었습니다. 
                    \n시간 관계 상 문제를 완전히 해결하지는 못했지만 더 높은 성능을 위해 오버 샘플링 또는 언더 샘플링과 같은 기법을 사용하거나, 시도 했으나 실패했었던 데이터 증강 기법을 더 공부해서 데이터 불균형 문제를 해결하고 싶습니다. """)
    with area_col2:
        img = load_image("./images/value_counts.png")
        st.image(img, width=250)
    
    st.markdown("")
    st.markdown("저희가 만든 모델이 실제로 사용하기에는 부족한 성능이지만 향후 이 모델이 민원 처리의 효율성을 향상 시키고 많은 사람들이 사용하는 서비스로 성장하기를 기대하고 있습니다. **더 많은 데이터를 확보**해야 하고 **자연어처리에 대한 지식**과 **사용한 알고리즘에 대한 깊이 있는 연구**가 필요할 것입니다. ")
