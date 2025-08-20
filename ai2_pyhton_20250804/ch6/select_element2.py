from datetime import datetime
import streamlit as st

def listDict(dataList):
    dataDict = {}
    for i in range(len(dataList)):
        dataDict[dataList[i]] = i
    return dataDict

option_mut = st.multiselect("喜歡的水果:",["蘋果","香蕉","橘子","西瓜"])
st.write(option_mut)
datList =  ["春季","夏季","秋季","冬季"]
optionDict = listDict(datList)
option_radio =  st.radio("你喜歡的季節:",datList)
st.write("你選的季節是:",optionDict[option_radio],option_radio)

checkBox = st.checkbox("是否同意")
if checkBox:
    st.write("同意")
else:
    st.write("不同意")    
st.write(checkBox)

dataList = list(range(1,11))
option_radio = st.select_slider("選一個範圍",options=dataList,value=(3,6))
st.write("你選的範圍:",option_radio)

value = st.slider("請選範圍",0.0,100.0,value=(25.2567,75.212))
st.write("你選的範圍:",value)

value2 = st.slider("請選範圍",0.0,100.0,value=(25.2567,75.212),step=0.0001,format="%.4f")
st.write("你選的範圍:",value2)