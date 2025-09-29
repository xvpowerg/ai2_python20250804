import streamlit as st
import pandas as pd
import joblib
st.title("銷售預測應用")
model,scaler = joblib.load(r"C:\Users\xvpow\ai2_pyhton_20250804\ch17\scaled_sles_prediction_model.pkl")
tv_spend = st.number_input("輸入TV廣告支出",min_value=0.0)
radio_spend = st.number_input("輸入radio廣告支出",min_value=0.0)
newspaper_spend = st.number_input("輸入newspaper廣告支出",min_value=0.0)

if st.button("預測銷售"):
    input_data = {
        "TV":tv_spend,
        "radio":radio_spend,
        "newspaper":newspaper_spend
    }
    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0][0]
    st.write(f"預測銷售:{prediction:.2f}")
