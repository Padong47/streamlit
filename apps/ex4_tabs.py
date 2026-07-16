# 🔨 레벨 3: 두 모델 통합 — 완성 후 `python3.11 -m streamlit run apps/ex4_tabs.py` (3·5절 참고)
# [패턴] load_model()과 load_pipeline()을 같은 파일에 두고, st.tabs로 화면만 나눕니다 — 모델 로직은 그대로 재사용.
import streamlit as st
import torch
from PIL import Image
from torchvision.models import MobileNet_V2_Weights, mobilenet_v2
from transformers import pipeline

st.title("레벨 3 — 이미지 분류 + 감성분석 통합 앱")


@st.cache_resource
def load_image_model():
    weights = MobileNet_V2_Weights.DEFAULT
    model = mobilenet_v2(weights=weights)
    model.eval()
    return model, weights.transforms(), weights.meta["categories"]


@st.cache_resource
def load_text_pipeline():
    return pipeline("sentiment-analysis", model="daekeun-ml/koelectra-small-v3-nsmc")


# ① st.tabs(["이미지 분류", "감성분석"])로 tab1, tab2를 만드세요
# 힌트: tab1, tab2 = st.tabs([...])
pass  # ← 여기에 작성하세요

# with tab1:
#     model, preprocess, categories = load_image_model()
#     uploaded = st.file_uploader("이미지 업로드", type=["jpg", "jpeg", "png"], key="tab1_upload")
#     # ② 3절의 전처리→추론→top5 로직을 그대로 옮겨오세요
#
# with tab2:
#     text = st.text_area("문장 입력", key="tab2_text")
#     # ③ 5절의 analyze() 로직을 그대로 옮겨오세요
