#%%writefile apps/ex4_widgets.py

# 위젯 4종을 하나씩 추가 — slider → selectbox → text_input → button
# [왜] 위젯 값이 그 즉시 화면에 반영되는 것을 눈으로 확인하는 연습입니다
import streamlit as st

# [흐름] 위젯을 하나씩 추가하면서 st.write로 값이 반영되는지 확인합니다
st.title("🎛️ 위젯 하나씩 추가하기")

level = st.slider("숙련도 (1~10)", 1, 10, 3)                          # ① 범위 선택
interest = st.selectbox("관심 주제", ["rerun", "위젯", "레이아웃"])    # ② 드롭다운 선택
name = st.text_input("이름을 입력하세요", value="수강생")              # ③ 문자열 입력

st.write(f"{name}님, 숙련도 {level}점, 관심 주제 '{interest}'")

# [핵심] button은 클릭 직후 rerun 1회 동안만 True — 계속 누른 것처럼 보이려면 다음 파일(ST2)의 session_state가 필요합니다
if st.button("확인"):                                                  # ④ 클릭 트리거
    st.success("버튼이 클릭된 그 rerun에서만 이 메시지가 보입니다.")
