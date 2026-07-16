# 🔨 레벨 1: top-k 슬라이더 — 완성 후 `python3.11 -m streamlit run apps/ex4_topk.py` (3절 참고)
# [패턴] 3절의 이미지 분류 파이프라인(전처리→추론→softmax→topk)에 "k를 사용자가 고른다"만 추가하는 문제입니다.
import streamlit as st
import torch
from PIL import Image
from torchvision.models import MobileNet_V2_Weights, mobilenet_v2


@st.cache_resource
def load_model():
    weights = MobileNet_V2_Weights.DEFAULT
    model = mobilenet_v2(weights=weights)
    model.eval()
    return model, weights.transforms(), weights.meta["categories"]


st.title("레벨 1 — top-k를 사용자가 고르는 이미지 분류")
model, preprocess, categories = load_model()

# ① 슬라이더로 k(1~10)를 입력받으세요 — 기본값 5
# 힌트: k = st.slider("보여줄 개수(top-k)", 1, 10, 5)
# [왜] k가 있어야 아래 topk 호출에서 몇 개까지 보여줄지 정할 수 있습니다
k = None  # ← 여기에 작성하세요

uploaded = st.file_uploader("이미지 업로드", type=["jpg", "jpeg", "png"])
if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, width="stretch")

    # ② 전처리 → 추론 → softmax 는 3절 이미지 분류 앱(apps/m4_image.py)와 완전히 동일합니다
    x = preprocess(image).unsqueeze(0)
    with torch.inference_mode():
        logits = model(x)
    probs = torch.nn.functional.softmax(logits[0], dim=0)

    # ③ torch.topk(probs, ?) 의 ?에 위에서 받은 k를 그대로 연결하세요
    # 힌트: top_prob, top_idx = torch.topk(probs, k)
    # [왜] 위 ①에서 받은 k를 그대로 넘겨야 슬라이더 값과 실제 출력 개수가 연동됩니다
    pass  # ← 여기에 작성하세요

    # for p, i in zip(top_prob, top_idx):
    #     st.write(f"{categories[i]}: {float(p):.4f}")
