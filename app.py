import streamlit as st

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="Data Science & ML Boot Camp", layout="wide", page_icon="🏠")

# ส่วนหัวข้อ (Header Section)
st.title("🏠 หน้าหลัก (Main Dashboard)")
st.subheader("Boot Camp: Data Science and Machine Learning")

# สร้างแถบข้อมูลไฮไลท์ด้านบน
col_info1, col_info2 = st.columns([2, 1])
with col_info1:
    st.info("🚀 7 Day Intensive Hands-on Workshop")
with col_info2:
    st.success("👨‍🏫 วิทยากร: Choosak Tosong")

st.markdown(''':rainbow[**"Operation Excellence"**] ''')
st.caption("📅 Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
st.divider()

# ส่วนเมนูเข้าสู่บทเรียน (Navigation Grid)
st.write("### 🛠️ เลือกโมดูลการเรียนรู้และแอปพลิเคชัน")

# แถวที่ 1: ระบบคำนวณและการทำความสะอาดข้อมูล
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("💰 ระบบคำนวณส่วนลด", use_container_width=True):
        st.switch_page("pages/app1_discount_calc.py")
with col2:
    if st.button("🧹 การทำความสะอาดข้อมูล", use_container_width=True):
        st.switch_page("pages/clean_tong (1).py")
with col3:
    if st.button("👤 clean_customers", use_container_width=True):
        st.switch_page("pages/clean_customers.py")
with col4:
    if st.button("📱 clean_app", use_container_width=True):
        st.switch_page("pages/clean_app.py")

# แถวที่ 2: การแปลงข้อมูลและการทำโมเดล Predict
col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("🔄 transform_app", use_container_width=True):
        st.switch_page("pages/transform_app.py")
with col6:
    if st.button("📊 EDA_app", use_container_width=True):
        st.switch_page("pages/EDA_app.py")
with col7:
    if st.button("📈 sale_predict.app", use_container_width=True):
        st.switch_page("pages/sale_predict.py")
with col8:
    if st.button("🚛 truck_predict.app", use_container_width=True):
        st.switch_page("pages/truck_predict.py")
