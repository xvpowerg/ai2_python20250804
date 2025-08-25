import streamlit as st
import pandas as pd
st.title("CSV Reading")
upload_file = st.file_uploader("上傳CSV檔",type="csv")
#print(type(upload_file))
if upload_file:
    df = pd.read_csv(upload_file)
    st.subheader("原始數據")
    st.dataframe(df)
    st.subheader("資料描述")
    st.dataframe(df.describe())
    st.subheader("資料圖片")
    st.line_chart(df)

    columns = st.selectbox("選擇顯示的列",df.columns)
    st.dataframe(df[columns])

    selected_columns = st.multiselect("選擇顯示的列",df.columns)
    if selected_columns:
        st.dataframe(df[selected_columns])
    else:
        st.write("請至少選一列")   
