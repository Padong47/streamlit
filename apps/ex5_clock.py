#%%writefile apps/ex5_clock.py
# 시계 트릭 — 위젯을 하나만 건드려도 스크립트 전체가 다시 실행되는 것을 확인
# [왜] 시각이 바뀐다 = rerun이 일어났다는 증거. 오늘 하루 종일 쓰는 디버깅 도구입니다
import time
import streamlit as st

st.title("🕐 시계 트릭")
# [핵심] 위젯을 하나만 만져도 이 캡션의 시각이 바뀝니다
st.caption(f"마지막 실행 시각: {time.strftime('%H:%M:%S')}")

level = st.slider("아무 값이나 움직여보세요", 1, 10, 3)
st.write(f"현재 값: {level}")
