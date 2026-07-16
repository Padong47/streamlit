# 첫 Streamlit 앱 — st.write와 매직으로 화면에 값 띄우기
# [핵심] st.write()는 print()의 웹 버전 — 터미널 대신 브라우저 화면에 출력됩니다
import streamlit as st

st.write("안녕하세요! 이것은 저의 첫 Streamlit 앱입니다.")

# [핵심] 매직(magic) — st.write() 없이 문자열만 적어도 자동으로 화면에 표시됩니다
"매직으로도 이렇게 화면에 뜹니다 ✨"
