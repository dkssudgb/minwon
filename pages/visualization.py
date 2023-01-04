import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

st.set_page_config(
   page_title="시각화",
   page_icon="🏷️",
   layout="wide",
)

def load_image(img_file):
   img = Image.open(img_file)
   return img

st.markdown("# 시각화")

tab1, tab2, tab3 = st.tabs(["전체 민원","경찰청 민원" ,"경기도 민원"])

with tab1:
   st.header("전체 민원 데이터 시각화📜")
   st.markdown("")
   st.subheader("국민신문고에서 크롤링한 데이터를 워드클라우드로 시각화")
   st.markdown("")
   
   # 이미지 파일 목록 가져오기
   img_list = ['전체', '고용노동부', '교육부', '국무총리_4처', '국무총리_위원회', '국방부', '국토교통부', '기획재정부', '농림축산식품부', '문화체육관광부', '법무부', '보건복지부', '여성가족부', '통일부', '해양수산부', '행정안전', '교육청', '대학교', '지방자치단체']
   
   # select box
   selected1 = st.selectbox('부서 종류 선택', ["선택", "전체", "중앙처리기관", "지방자치기관", "교육기관"])
      
   if selected1 == "전체": # 전체 선택: 하위부서도 전체
      selected2 = st.selectbox("하위 부서 선택", ["전체"])
      for i in img_list[1:]:
         st.markdown("### " + i)
         img = load_image("./images/" + i + ".png")
         st.image(img, width=400)
         st.markdown("")

   elif selected1 == "중앙처리기관": # 중앙처리기관 선택
      slist = ['선택', '전체', '고용노동부', '교육부', '국무총리_4처', '국무총리_위원회', '국방부', '국토교통부', '기획재정부', '농림축산식품부', '문화체육관광부', '법무부', '보건복지부', '여성가족부', '통일부', '해양수산부', '행정안전부']
      selected2 = st.selectbox('하위 부서 선택', slist)
      
      if selected2 == "전체":
         for i in slist[2:]:
            st.markdown("### " + i)
            img = load_image("./images/" + i + ".png")
            st.image(img, width=400)
            st.markdown("")
      for s in slist[2:]:
         if selected2 == s:
            st.markdown("### " + s)
            img = load_image("./images/" + s + ".png")
            st.image(img, width=400)
            st.markdown("")

   elif selected1 == "지방자치기관":
      selected2 = st.selectbox('하위 부서 선택', ["지방자치기관"])
      st.markdown("### 지방자치기관")
      img = load_image("./images/지방자치단체.png")
      st.image(img, width=400)
      st.markdown("")

   elif selected1 == "교육기관":
      slist = ["선택", "전체", "교육청", "대학교"]
      selected2 = st.selectbox('하위 부서 선택', slist)
      
      if selected2 == "전체":
         for i in slist[2:]:
            st.markdown("### " + i)
            img = load_image("./images/" + i + ".png")
            st.image(img, width=400)
            st.markdown("")
      for s in slist[2:]:
         if selected2 == s:
            st.markdown("### " + s)
            img = load_image("./images/" + s + ".png")
            st.image(img, width=400)
            st.markdown("")



with tab2:
   st.header("경찰청 민원 데이터 시각화📜")
   st.markdown("")
   st.subheader("경찰청 민원 발생 건수")
   st.write("**기간 : 2022년 12월 01일 ~ 2022년 12월 31일**")
   st.markdown("""전체 기관 중 민원이 가장 많이 접수된 경찰청의 민원 데이터들을 시각화했습니다.""")

   data0 = pd.read_csv("./api_data/민원발생지역순위_경찰청.csv")
   data1 = pd.read_csv("./api_data/맞춤형통계_경찰청.csv")
   data2 = pd.read_csv("./api_data/핵심키워드_경찰청.csv")
   data3 = pd.read_csv("./api_data/키워드트렌드_경찰청_경찰서.csv")
   # data4 = pd.read_csv("./api_data/키워드기반민원건수_경찰청_경찰서.csv")
   data5 = pd.read_csv("./api_data/연관어분석_경찰청_경찰서.csv")
   # data6 = pd.read_csv("./api_data/키워드기반연령_경찰청_경찰서.csv")

   #민원발생지역순위
   st.subheader("경찰청 민원 지역별 발생 건수")
   st.markdown("""22년 12월 한달간 경찰청에 민원을 많이 접수한 지역은 경기도 입니다.""")
   pxh0 = px.bar(data0, x="label", y="hits",labels={"label" : "지역", "hits" : "건수"}, color="hits", color_continuous_scale="Tealgrn")
   st.plotly_chart(pxh0)

   #맞춤형통계
   st.subheader("접수된 민원 건수")
   st.markdown("""경찰청에 민원이 가장 많이 접수된 날은 12월 8일로 총 3,942건입니다.""")
   data1.rename(columns={'label' : '날짜', 'hits' : '건수'}, inplace=True)
   # pd.to_datetime(data1["날짜"])

   pxh = px.bar(data1, x="날짜", y="건수", color="건수", color_continuous_scale="Teal")
   pxh.update_layout(xaxis=dict(tickformat="%d-%m"))
   st.plotly_chart(pxh)


   #핵심키워드
   st.subheader("경찰청 민원 핵심 키워드 Top10")
   st.markdown("""경찰서를 포함한 민원이 가장 많이 접수되었습니다.""")
   data2.rename(columns={'label' : '키워드', 'value' : '건수'}, inplace=True)

   area_col1, area_col2 = st.columns(2)
   with area_col1:
      st.table(data2[:10])

   with area_col2:
      pxh = px.bar(data2[:10], x="키워드", y="건수", color="건수", color_continuous_scale="Tealgrn")
      pxh.update_layout(xaxis=dict(tickformat="%d-%m"))
      st.plotly_chart(pxh)

   #키워드 트렌드
   st.subheader("키워드 트렌드 : 경찰서")
   st.markdown("""핵심키워드 1위인 경찰서를 포함한 민원 트렌드입니다.""")
   st.markdown("""가장 많이 접수된 날은 12월 5일로 163.4% 증가하였습니다.""")
   data3.rename(columns={'hits' : '건수',
                     'label' : '날짜',
                     'prevRatio' : '증가율'
                     }, inplace=True)

   pxh2 = px.bar(data3, x="날짜", y="증가율", color="증가율", color_continuous_scale="Aggrnyl")
   pxh2.update_layout(xaxis=dict(tickformat="%d-&m"))
   st.plotly_chart(pxh2, use_container_width=True)


   #연관어 분석
   st.subheader("연관어 분석 : 경찰서")
   st.markdown("""핵심키워드 1위인 경찰서와 연관이 높은 키워드 10개 입니다.""")
   data5.rename(columns={"label" : "연관키워드", "value" : "분석스코어"}, inplace=True)

   pxh3 = px.bar(data5[:10], x="연관키워드", y="분석스코어", color="분석스코어", color_continuous_scale="Tealgrn")
   # pxh2.update_layout(xaxis=dict(tickformat="%d-&m"))
   st.plotly_chart(pxh3, use_container_width=True)



with tab3:
   st.header("경기도 민원 데이터 시각화📜")
   st.markdown("")
   area_url_1 = "https://raw.githubusercontent.com/dkssudgb/minwon/main/api_data/%EA%B2%BD%EA%B8%B0%EB%8F%84_%EB%A7%9E%EC%B6%A4%ED%98%95%ED%86%B5%EA%B3%84.csv"
   
   @st.cache
   def area_load_data_1():
      area_df1 = pd.read_csv(area_url_1, encoding='UTF8', index_col=0)
      return area_df1
   area_df1 = area_load_data_1()

   st.subheader("경기도 민원 발생 건수")
   st.write("**기간 : 2022년 12월 01일 ~ 2022년 12월 31일**")
   st.markdown("""전국을 기준으로 민원이 가장 많이 접수된 경기도의 민원 데이터들을 시각화했습니다.""")
   st.markdown("""일정한 주기로 민원 건수가 적게 나타난 이틀은 전부 주말이었습니다.""")


   area_fig1 = px.bar(area_df1, x=area_df1.index, y="민원 건수", color="민원 건수", color_continuous_scale="teal")
   st.plotly_chart(area_fig1, theme="streamlit", use_container_width=True)

   st.markdown("")
   st.markdown("")
   area_url_2 = "https://raw.githubusercontent.com/dkssudgb/minwon/main/api_data/%EA%B2%BD%EA%B8%B0%EB%8F%84_%ED%95%B5%EC%8B%AC%ED%82%A4%EC%9B%8C%EB%93%9C.csv"
   @st.cache
   def area_load_data_2():
      area_df2 = pd.read_csv(area_url_2, encoding='UTF8')
      return area_df2

   area_df2 = area_load_data_2()
   area_df2_2 = area_df2.iloc[1:11]
   area_df2_2.rename(columns={'비중' : '가중치'}, inplace=True)
   area_df2_2['가중치'] = round(area_df2_2['가중치'], 2)


   st.subheader("경기도 민원 핵심 키워드 Top10")
   st.markdown("""체험관과 관련된 민원이 많이 접수되었음을 알 수 있었고, 설계/건축/설비와 관련된 키워드도 상위를 차지했습니다.""")

   area_col1, area_col2 = st.columns(2)
   with area_col1:
      st.table(area_df2_2)

   with area_col2:
      area_fig2_2 = px.bar(area_df2_2, x="키워드", y="가중치", color="가중치", color_continuous_scale="blugrn")
      st.plotly_chart(area_fig2_2, theme="streamlit", use_container_width=True)


   area_url_4 = "https://raw.githubusercontent.com/dkssudgb/minwon/main/api_data/%ED%82%A4%EC%9B%8C%EB%93%9C%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%B2%B4%ED%97%98%EA%B4%80.csv"
   @st.cache
   def area_load_data_4():
      area_df4 = pd.read_csv(area_url_4, encoding='UTF8')
      return area_df4

   area_df4 = area_load_data_4()

   st.markdown("")
   st.markdown("")
   st.subheader("키워드 트렌드 : 체험관")
   st.markdown("""체험관 관련 민원이 400% 증가한 2022년 12월 12일은 월요일로,""")
   st.markdown("""29일을 제외하면 체험관과 관련된 민원은 주로 월요일에 증가했음을 확인할 수 있었습니다.""")

   area_fig4_2 = px.bar(area_df4, x="민원 일자", y="증가율", hover_data=['민원 건수'], color="증가율", color_continuous_scale="teal")
   st.plotly_chart(area_fig4_2, theme="streamlit", use_container_width=True)

   st.markdown("")
   st.markdown("")
   area_url_5 = "https://raw.githubusercontent.com/dkssudgb/minwon/main/api_data/%EC%97%B0%EA%B4%80%EC%96%B4%EB%B6%84%EC%84%9D_%EA%B2%BD%EA%B8%B0%EB%8F%84.csv"
   @st.cache(allow_output_mutation=True)
   def area_load_data_5():
      area_df5 = pd.read_csv(area_url_5, encoding='UTF8')
      return area_df5

   area_df5 = area_load_data_5()
   area_df5['분석 스코어'] = round(area_df5['분석 스코어'], 2)
   area_df5_2 = area_df5.iloc[:10]


   st.markdown("")
   st.markdown("")
   area_url_6 = "https://raw.githubusercontent.com/dkssudgb/minwon/main/api_data/%EC%97%B0%EA%B4%80%EC%96%B4%EB%B6%84%EC%84%9D_%EC%B2%B4%ED%97%98%EA%B4%80.csv"
   @st.cache(allow_output_mutation=True)
   def area_load_data_6():
      area_df6 = pd.read_csv(area_url_6, encoding='UTF8')
      return area_df6

   area_df6 = area_load_data_6()
   area_df6['분석 스코어'] = round(area_df6['분석 스코어'], 2)
   area_df6_2 = area_df6.iloc[:10]


   st.subheader("연관어 분석")

   area_fig5_2 = px.bar(area_df5_2, x="키워드", y="분석 스코어", color="분석 스코어", color_continuous_scale="blugrn")
   area_fig6_2 = px.bar(area_df6_2, x="키워드", y="분석 스코어", color="분석 스코어", color_continuous_scale="teal")

   area_tab_1, area_tab_2 = st.tabs(["키워드 : 경기도", "키워드 : 체험관"])
   with area_tab_1:
      st.markdown("""경기도를 키워드로 한 민원의 연관어로는 파주, 고양, 운정, 김포 등 지역 명이 많았으나""")
      st.markdown("""경기북부 국민안전체험관이라는 키워드가 눈에 띕니다.""")
      st.plotly_chart(area_fig5_2, theme="streamlit", use_container_width=True)
   with area_tab_2:
      st.markdown("""반대로 체험관을 키워드로 한 민원에는 경기도가 연관어 1위로 나타났습니다.""")
      st.markdown("""유치 결정 키워드를 확인한 뒤 추가적으로 조사해본 결과""")
      st.markdown("""경기북부 국민안전체험관의 유치를 위해 파주와 의정부에서 민원이 다수 접수되었다는 기사를 찾을 수 있었습니다.""")
      st.markdown("""https://www.news1.kr/articles/?4843366""")
      st.plotly_chart(area_fig6_2, theme="streamlit", use_container_width=True)