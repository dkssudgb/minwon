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
   st.markdown("")
   
   st.markdown("""### Konlpy
               \n- 한글 형태소 분석을 위해 사용했습니다.
               \n- 모델 학습 전 각각의 성능을 비교하기 위해 Okt, Kkma, Mecab을 전부 사용해본 후 가장 좋은 성능을 보이는 방법을 채택했습니다.
               \n- 모델 별 객관적인 비교를 위해 동일한 방법으로 형태소 분석 후 모델에 적용했습니다.
               \n- 민원 내용을 특정 기관으로 분류할 때 중요한 내용의 많은 부분이 명사에 해당한다고 판단하여 명사만 추출했고, 두 글자 이상의 명사만 사용해 보다 명확한 의미를 갖도록 했습니다.""")
   st.markdown(""" ```python
               from konlpy.tag import Mecab
               \nmecab = Mecab() """)
   st.markdown(""" ```python
               # 두 글자 이상의 명사만 추출
               \ndef mecab_clean(text):
               \n\tclean_text = []
               \n\tfor word in mecab.pos(text):
               \n\t\tif (word[1] in ['NNG']) & (len(word[0]) > 1):
               \n\t\t\tclean_text.append(word[0])
               \n\treturn " ".join(clean_text) """)
   st.markdown(""" ```python
               # 답변 내용에 적용
               \nfrom tqdm import tqdm
               \ntqdm.pandas()
               \n\ndf['content'] = df['content'].progress_map(mecab_clean) """)
   st.markdown("")
   
   st.markdown("### 불용어 제거")
   st.markdown("""```python
               # 불용어 제거
               \ndef remove_stopwords(text):
               \n\ntokens = text.split(' ')
               \n\nstops = ['경우','귀하','답변','대한','사항','문의','친절','안녕','설명','만족','연락','안내','신문고','질의','민원','내용','추가','필요','생각','감사','말씀','첨부','자료','부분','조치','상담','고객','지원','해당','관련','확인','다음','관리','대해','결과','국민']
               \n\nmeaningful_words = [w for w in tokens if not w in stops]
               \n\nreturn ' '.join(meaningful_words)
               """)

with tab2:
   st.markdown("## 모델링")
   st.markdown("")
   
   st.markdown("### 📌SimpleRNN")
   st.markdown("""```python
               model = Sequential()
               \nmodel.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length))
               \nmodel.add(Bidirectional(SimpleRNN(units=64, return_sequences=True)))
               \nmodel.add(Bidirectional(SimpleRNN(units=128, return_sequences=True)))
               \nmodel.add(Bidirectional(SimpleRNN(units=64, return_sequences=True)))
               \nmodel.add(SimpleRNN(units=32))
               \nmodel.add(Dense(n_class, activation="softmax"))
               """)
   st.markdown("")
   
   st.markdown("""### 📌BLSTM(Bidirectional-LSTM)
               \n- 수업 중 배웠던 모델을 프로젝트에 적용해 보고 성능을 비교해 가장 좋은 성능의 모델을 채택하고자 사용했습니다.
               \n- 기울기 손실 문제 해결을 위해 LSTM 모델을 사용했고, 텍스트를 효과적으로 읽어내기 위해 양방향 순환 신경망(Bidirectional) 과 함께 사용했습니다.
               \n- 자연어 처리 작업에 적합하며 긴 데이터 시퀀스를 처리할 수 있다는 특징이 있습니다.""")
   st.markdown("""```python
               model2 = Sequential()
               \nmodel2.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length))
               \nmodel2.add(Bidirectional(LSTM(units=64, return_sequences=True)))
               \nmodel2.add(Bidirectional(LSTM(units=128, return_sequences=True)))
               \nmodel2.add(Bidirectional(LSTM(units=64)))
               \nmodel2.add(Dense(units=32, activation='elu'))
               \nmodel2.add(Dense(n_class, activation="softmax"))
               """)
   st.markdown("")
   
   st.markdown("""### 📌GRU
               \n- 시퀀스 데이터인 자연어의 특징을 살려보고자 RNN 모델을 사용했습니다.
               \n- LSTM보다 간단한 구조를 가지는 GRU의 성능을 알아보고 비교하기 위해 사용했습니다.
               \n- 민원 내용을 특정 기관으로 분류할 때 중요한 내용의 많은 부분이 명사에 해당한다고 판단하여 명사만 추출했고, 두 글자 이상의 명사만 사용해 보다 명확한 의미를 갖도록 했습니다.
               \n- 명사만 추출하는 경우 자연어라고 하더라도 시퀀스 데이터의 특징이 떨어진다고 판단해 다른 모델에도 적용해볼 예정입니다. """)
   st.markdown("""```python
               model3 = Sequential()
               \nmodel3.add(Embedding(input_dim=5000, output_dim=embedding_dim, input_length=max_length))
               \nmodel3.add(Bidirectional(GRU(units=128, return_sequences=True)))
               \nmodel3.add(Bidirectional(GRU(units=64)))
               \nmodel3.add(Dense(units=32))
               \nmodel3.add(Dense(n_class, activation="softmax"))
               """)