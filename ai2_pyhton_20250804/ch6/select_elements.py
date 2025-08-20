import streamlit as st


def colorIndex(colorData,findColor="紅色"):
    index = -1
    for i in range(len(colorData)):
        if colorData[i] == findColor:
            return i
    return index

colorDir= {"紅色":0,"藍色":1,"綠色":2}

st.title("請選顏色")    
data = ["紅色","藍色","綠色"]
option_index = st.selectbox("你喜歡的顏色:",data)
st.write(f"option_index:{option_index} {colorIndex(data,option_index)} {colorDir.get(option_index,-1)}")
    