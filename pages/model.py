import streamlit as st

st.set_page_config(
    page_title="민원분류-모델",
    page_icon="🏷️",
    layout="wide",
)

st.title("모델링")

tab1, tab2 = st.tabs(["형태소 분석", "모델링"])

with tab1:
   st.markdown("## 형태소 분석")
   
   
   

with tab2:
   st.markdown("## 모델링")
   
   st.markdown("""### BLSTM(Bidirectional-LSTM)
               \n- 수업 중 배웠던 모델을 프로젝트에 적용해 보고 성능을 비교해 가장 좋은 성능의 모델을 채택하고자 사용했습니다.
               \n- 기울기 손실 문제 해결을 위해 LSTM 모델을 사용했고, 텍스트를 효과적으로 읽어내기 위해 양방향 순환 신경망(Bidirectional) 과 함께 사용했습니다.
               \n- 자연어 처리 작업에 적합하며 긴 데이터 시퀀스를 처리할 수 있다는 특징이 있습니다.""")
   
   st.markdown("""### BLSTM(Bidirectional-LSTM)
               \n- 시퀀스 데이터인 자연어의 특징을 살려보고자 RNN 모델을 사용했습니다.
               \n- LSTM보다 간단한 구조를 가지는 GRU의 성능을 알아보고 비교하기 위해 사용했습니다.
               \n- 민원 내용을 특정 기관으로 분류할 때 중요한 내용의 많은 부분이 명사에 해당한다고 판단하여 명사만 추출했고, 두 글자 이상의 명사만 사용해 보다 명확한 의미를 갖도록 했습니다.
               \n- 명사만 추출하는 경우 자연어라고 하더라도 시퀀스 데이터의 특징이 떨어진다고 판단해 다른 모델에도 적용해볼 예정입니다.
               
               
               
               """)
