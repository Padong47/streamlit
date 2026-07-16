# 🔨 도전 과제 A: cache_data / cache_resource 적용 — 완성 후 `streamlit run apps/ex3_cache.py` (4절 참고)
# [패턴] 데이터 로드에는 cache_data, 모델 학습에는 cache_resource를 붙이는 문제입니다.
import time
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

st.title("도전 과제 A — 캐싱 적용")

# [왜] cache_data — 데이터는 호출마다 복사본을 반환해 안전하게 재사용된다(반환값이 DataFrame처럼 변경 가능한 객체일 때 적합).
# ① 아래 함수에 @st.cache_data를 붙이세요 (함수 정의 바로 윗줄)
# 힌트: @st.cache_data
def load_penguins():
    return sns.load_dataset("penguins").dropna()

# [왜] cache_resource — 모델·DB 연결처럼 "리소스"는 복사하지 않고 그대로 재사용해야 한다(cache_data로 감싸면 매번 불필요하게 복사됨).
# ② 아래 함수에 @st.cache_resource를 붙이세요 (함수 정의 바로 윗줄)
# 힌트: @st.cache_resource
def train_dummy_model(df):
    le = LabelEncoder()
    X = df[FEATURES]
    y = le.fit_transform(df["species"])
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model

# [왜] time.time()으로 직접 재서 눈으로 확인 — "캐싱됐다"는 로그 문구가 아니라
#      두 번째 클릭부터 소요 시간이 실제로 줄어드는지 학생이 숫자로 검증하게 한다.
if st.button("데이터 로드 + 모델 학습"):
    start = time.time()
    df = load_penguins()
    model = train_dummy_model(df)
    st.write(f"소요 시간: {time.time() - start:.3f}초 (데이터 {len(df)}행)")
    # 버튼을 두 번 이상 눌러 비교하세요 — 캐싱이 되면 두 번째부터 훨씬 빨라집니다.
