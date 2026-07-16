# 🔨 레벨 2: 확신도 임계값 — 완성 후 `python3.11 -m streamlit run apps/ex4_confidence.py` (4·5절 참고)
# [패턴] analyze()가 돌려주는 label·score 중 score만으로 "판정 불확실"을 가르는 문제입니다.
import streamlit as st
from transformers import pipeline

# [실측] 0.7은 자연스러운 문장에서 거의 발동하지 않는다 — 10개 자연문 테스트 결과 confidence가
#        0.7 미만인 경우는 0/10, 반면 0.95 미만은 2/10이었다(실측: "무난했습니다" 72.6%,
#        "그럭저럭 볼만은 했어요" 73.1%). 모델이 자연문에는 늘 90%+ 확신을 보이기 때문이다.
THRESHOLD = 0.95  # ✏️ 이 값을 바꿔가며 "판정 불확실"이 몇 번 뜨는지 비교해보세요


@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis", model="daekeun-ml/koelectra-small-v3-nsmc")


def analyze(text: str) -> dict:
    clf = load_pipeline()
    result = clf(text, truncation=True, max_length=512)[0]
    # [주의] 5절의 교훈 그대로 — 이 모델은 'positive'가 아니라 '1'/'0'을 돌려줍니다.
    label = "긍정" if result["label"] == "1" else "부정"
    return {"label": label, "score": result["score"]}


st.title("레벨 2 — 확신도가 낮으면 판정 보류")
# [실측] "무난했습니다"는 확신도 72.6%로 측정됨 — THRESHOLD=0.95에서 "판정 불확실"이 뜬다
text = st.text_area("문장 입력", value="무난했습니다")

if st.button("분석"):
    out = analyze(text)

    # ① out["score"]가 THRESHOLD 미만이면 "판정 불확실 🤔"을,
    #    그 이상이면 out["label"]에 따라 "긍정 😊"/"부정 😞"을 보여주세요
    # 힌트: if out["score"] < THRESHOLD: ... else: ...
    pass  # ← 여기에 작성하세요
