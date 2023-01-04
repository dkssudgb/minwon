import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="시각화",
    layout="wide",
)

st.markdown("# 시각화")

tab1, tab2, tab3 = st.tabs(["민원 데이터","경찰청 민원 API 데이터 시각화" ,"API 데이터"])

with tab1:
   st.header("민원 데이터 시각화")

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
   st.header("API 데이터 시각화")