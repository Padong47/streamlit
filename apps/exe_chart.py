%%writefile apps/ex3_chart.py
# 랜덤 데이터 차트 — st.line_chart
# [왜] 표보다 그래프가 추세를 한눈에 보여줍니다. DataFrame만 넘기면 축은 Streamlit이 알아서 그립니다
import numpy as np
import pandas as pd
import streamlit as st

st.title("📈 랜덤 데이터 차트")

# [흐름] 20행 3열짜리 무작위 숫자표 — 매번 새로 만들어지는 데이터입니다
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# [핵심] 다시 실행하면 데이터가 바뀌는 이유는 5절(rerun 모델)에서 설명합니다
st.caption("이 앱을 다시 실행하면(재시작 또는 새로고침) 그래프 모양이 매번 바뀝니다.")
