# 🔨 실습: 새 도구 추가 — echo_length (3절 참고)
# [패턴] 도구 하나 추가 = ① 스키마 정의 → ② 함수 구현 → ③ TOOLS에 추가 → ④ TOOL_FUNCS 등록
# 완성 후: python3.11 -m streamlit run apps/ex5b_tool.py
import streamlit as st

from apps.m5b_agent_loop import TOOLS, TOOL_FUNCS, run_agent, provider_available

# ① 스키마 정의 — 3절 analyze_sentiment 스키마와 같은 구조로 작성하세요
#    힌트: name="echo_length", description, parameters에 text(string, required) 하나
echo_length_tool = None  # 여기에 작성하세요 — {"type": "function", "function": {...}}

# ② 함수 구현 — 문자열의 글자 수를 세어 문자열로 반환하세요
def _tool_echo_length(text: str) -> str:
    # 힌트: return f"'{text}' 글자 수: {len(text)}자" 형태면 충분합니다.
    pass  # 여기에 작성하세요


# ③ TOOLS에 추가 — 원본 TOOLS 리스트에 이어 붙입니다(3절의 TOOLS 정의 참고)
# TOOLS.append(echo_length_tool)  # 여기 주석을 해제하세요

# ④ TOOL_FUNCS 등록 — 이게 없으면 run_tool이 "알 수 없는 도구"를 반환합니다
# TOOL_FUNCS["echo_length"] = _tool_echo_length  # 여기 주석을 해제하세요

st.title("echo_length 도구 추가 확인")
st.caption("provider 키/서버가 없으면 데모 모드로 동작합니다(m5b와 동일 규약).")
provider = st.sidebar.selectbox("Provider", ["local", "openrouter", "openai"])
if not provider_available(provider):
    st.info("🧪 데모 모드로 동작 중입니다 — echo_length는 실 provider 연결 시에만 호출됩니다.")

if q := st.chat_input("예) '안녕하세요 반갑습니다' 글자 수 세줘"):
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        with st.status("에이전트가 판단하는 중...", expanded=True) as status:
            answer, trace = run_agent(q, provider)
            for name, result in trace:
                st.write(f"🔧 `{name}` 호출 → {result}")
            status.update(label="완료", state="complete", expanded=False)
        st.markdown(answer)
