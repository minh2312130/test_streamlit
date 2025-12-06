import streamlit as st

from ui import UI
# --- PHẦN HEADER ---
# Chia layout header thành 3 phần: Logo - Thanh tìm kiếm - Nút điều hướng
st.set_page_config(layout="wide")



st.markdown(UI.load_main_page(), unsafe_allow_html=True)



# -------------------