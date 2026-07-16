# 🔨 도전 2: 사이드바 + columns 대시보드 뼈대 — 완성 후 `streamlit run apps/ex_dashboard.py`
# [패턴] 사이드바(설정) + columns(본문 2단 배치) + metric 조합 문제입니다.
import streamlit as st

st.title("도전 2 — 대시보드 뼈대")

# ① 사이드바에 슬라이더나 selectbox 등 설정용 위젯을 1개 이상 만드세요
# 힌트: target = st.sidebar.slider("목표 값", 0, 100, 50)
target = None  # ← 여기에 사이드바 위젯 코드를 작성

# ② st.columns(2)로 본문을 2단으로 나누세요
# 힌트: col1, col2 = st.columns(2)
col1, col2 = None, None  # ← 여기에 columns 코드를 작성

# ③ 각 칸에 st.metric을 하나씩 표시하세요 (하나는 ①의 target 값을 활용)
# 힌트: col1.metric("현재 값", 42)
#      col2.metric("목표 값", target)
pass  # ← 여기에 metric 표시 코드를 작성
