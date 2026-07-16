# 🔨 도전 과제 B: 새 특징 추가 — 부리 비율 — 완성 후 `streamlit run apps/ex3_feature.py` (6절 예측 탭 number_input 참고)
# [패턴] number_input 2개로 새 특징(비율)을 계산하고 st.metric으로 평균과 비교하는 문제입니다.
import seaborn as sns
import streamlit as st

st.title("도전 과제 B — 새 특징: 부리 비율")

df = sns.load_dataset("penguins").dropna()
avg_ratio = (df["bill_length_mm"] / df["bill_depth_mm"]).mean()

# ① 부리 길이·깊이를 입력받는 number_input 2개를 만드세요
# 힌트: length = st.number_input("부리 길이 (mm)", 30.0, 60.0, 45.0)
#      depth = st.number_input("부리 깊이 (mm)", 13.0, 22.0, 17.0)
length = None  # ← 여기에 number_input 코드를 작성
depth = None  # ← 여기에 number_input 코드를 작성

# ② 새 특징(비율 = length / depth)을 계산하세요
# 힌트: ratio = length / depth
ratio = None  # ← 여기에 계산 코드를 작성

# ③ st.metric으로 비율을 보여주고, 전체 평균(avg_ratio)과의 차이를 delta로 표시하세요
# 힌트: st.metric("부리 비율", f"{ratio:.2f}", delta=f"{ratio - avg_ratio:+.2f}")
pass  # ← 여기에 metric 표시 코드를 작성
