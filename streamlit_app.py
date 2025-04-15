import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# 임시 예측 함수
def fake_predict(image):
    return "김밥"

# 영양소 데이터
nutrition_db = {
    "김밥": {"칼로리": 350, "탄수화물": "40g", "단백질": "10g", "지방": "12g"},
    "비빔밥": {"칼로리": 550, "탄수화물": "70g", "단백질": "15g", "지방": "18g"}
}

st.title("음식 사진으로 영양소 알아보기")

uploaded_file = st.file_uploader("음식 사진 업로드", type=["jpg", "png", "jpeg"])

if uploaded_file:
    try:
        img = Image.open(uploaded_file).convert("RGB")
        img.thumbnail((512, 512))  # 메모리 절약
        st.image(img, caption="업로드한 이미지", use_column_width=True)

        with st.spinner("분석 중..."):
            predicted_food = fake_predict(img)
            st.subheader(f"예측된 음식: {predicted_food}")

            if predicted_food in nutrition_db:
                st.write("**영양소 정보:**")
                df = pd.DataFrame([nutrition_db[predicted_food]])
                st.table(df)
            else:
                st.write("영양소 정보가 없어요. 음식 이름을 입력해 보세요:")
                manual_food = st.text_input("음식 이름")
                if manual_food and manual_food in nutrition_db:
                    st.write("**영양소 정보:**")
                    df = pd.DataFrame([nutrition_db[manual_food]])
                    st.table(df)
    except Exception as e:
        st.error(f"이미지 처리 오류: {e}")
else:
    st.warning("이미지를 업로드해 주세요!")
