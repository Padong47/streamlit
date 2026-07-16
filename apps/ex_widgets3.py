# 🔨 도전 1: 위젯 3종 조합 — 완성 후 `streamlit run apps/ex_widgets3.py` (4절 참고)
# [패턴] text_input · slider · selectbox 값을 한 문장으로 조합해 st.write로 출력하는 문제입니다.
import streamlit as st

st.title("도전 1 — 위젯 3종 조합")

# ① 이름을 입력받는 text_input을 만드세요
# 힌트: name = st.text_input("이름을 입력하세요", value="수강생")
name = None  # ← 여기에 text_input 코드를 작성

# ② 1~10 사이 숙련도를 받는 slider를 만드세요
# 힌트: level = st.slider("숙련도", 1, 10, 3)
level = None  # ← 여기에 slider 코드를 작성

# ③ 관심 주제를 고르는 selectbox를 만드세요
# 힌트: interest = st.selectbox("관심 주제", ["rerun", "위젯", "레이아웃"])
interest = None  # ← 여기에 selectbox 코드를 작성

# ④ 위 세 값을 한 문장으로 조합해 st.write로 출력하세요
# 힌트: st.write(f"{name}님은 숙련도 {level}점, '{interest}'에 관심이 있습니다.")
pass  # ← 여기에 출력 코드를 작성
