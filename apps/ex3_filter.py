# 🔨 추가 시도: EDA에 위젯 추가 — 종(species) 필터 — 완성 후 `streamlit run apps/ex3_filter.py` (2절 산점도·5절 EDA 탭 참고)
# [패턴] st.multiselect로 종을 골라 필터링한 데이터만 표와 산점도로 보여주는 문제입니다.
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("추가 시도 — 종 필터 위젯 추가")

df = sns.load_dataset("penguins").dropna()

# ① species 목록 중에서 여러 개 고를 수 있는 multiselect를 만드세요 (기본값: 전체 종)
# 힌트: species_list = df["species"].unique().tolist()
#      selected = st.multiselect("보고 싶은 종", species_list, default=species_list)
selected = None  # ← 여기에 multiselect 코드를 작성

# ② selected에 포함된 종만 필터링하세요
# 힌트: filtered = df[df["species"].isin(selected)]
filtered = None  # ← 여기에 필터링 코드를 작성

# ③ 필터링된 데이터를 표와 산점도로 보여주세요
# 힌트: st.dataframe(filtered)
#      fig, ax = plt.subplots()
#      sns.scatterplot(data=filtered, x="bill_length_mm", y="flipper_length_mm", hue="species", ax=ax)
#      st.pyplot(fig)
pass  # ← 여기에 표시 코드를 작성