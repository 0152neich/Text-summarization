import streamlit as st
import requests

API_URL = "http://summarization:8000/v1/summarize"

st.title("Text Summarization App 🚀")
st.subheader("Nhập văn bản để tóm tắt:")

input_text = st.text_area("Nhập văn bản vào đây...", height=200)

if st.button("Tóm tắt"):
    if not input_text.strip():
        st.warning("Vui lòng nhập văn bản!")
    else:
        with st.spinner("Đang xử lý..."):
            try:
                response = requests.post(API_URL, json={"text": input_text})
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Tóm tắt thành công!")
                    st.write("**Kết quả:**")
                    st.info(result["info"]["text"])
                else:
                    st.error(f"Lỗi {response.status_code}: {response.json().get('detail', 'Không rõ lỗi')}")

            except requests.exceptions.RequestException as e:
                st.error(f"Lỗi kết nối API: {str(e)}")
