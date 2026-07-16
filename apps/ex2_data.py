%%writefile apps/ex2_data.py
# 텍스트 + 표 + 숫자 카드 — st.title/st.markdown → st.dataframe/st.metric
# [왜] 화면에 "제목 → 설명 → 데이터"의 기본 골격을 갖추는 연습입니다
import pandas as pd
import streamlit as st

st.title("🍎 오늘의 과일 가격")
st.markdown("아래는 **표**와 **숫자 카드**로 같은 데이터를 보여준 예시입니다.")

# [흐름] 표 형태 데이터는 DataFrame으로 만들고 st.dataframe으로 그대로 띄웁니다
fruit_df = pd.DataFrame({"이름": ["사과", "바나나", "포도"], "가격": [1200, 800, 3000]})
st.dataframe(fruit_df)

# [핵심] metric은 값 하나를 카드 형태로 강조합니다 — 표보다 한눈에 들어옵니다
st.metric("오늘 평균가", f"{fruit_df['가격'].mean():.0f}원")
