# 🔨 Step A: 실패하는 카운터 — 완성 후 `streamlit run apps/ex_failcounter.py` (5절 rerun 모델 참고)
# [패턴] session_state 없이 카운터를 만들어, 왜 값이 유지되지 않는지 rerun 모델로 직접 확인하는 문제입니다.
import time
import streamlit as st

st.title("Step A — 실패하는 카운터")

# [핵심] 시계 트릭 — 버튼을 누를 때마다 이 시각이 바뀌는지 확인하세요(=rerun이 일어났다는 증거)
st.caption(f"마지막 실행 시각: {time.strftime('%H:%M:%S')}")

# ① count를 0으로 두고, 버튼을 누르면 1 증가시켜 st.write로 보여주세요 (session_state 사용 금지)
# 힌트: count = 0
#      if st.button("증가"):
#          count += 1
#      st.write(count)
pass  # ← 여기에 실패하는 카운터 코드를 작성

# ② 버튼을 5번 눌러보고, count가 왜 1을 넘지 못하는지 위 5절 내용으로 설명해보세요(코드 주석으로 남겨도 좋습니다)
