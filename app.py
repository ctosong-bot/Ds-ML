import streamlit as st

st.set_page_config(page_title="Data Science & ML Boot Camp", layout="wide", page_icon="🏠")

# หัวข้อหลัก
st.title("🏠 หน้าหลัก (Dashboard)")
st.markdown("### **Boot Camp: Data Science and Machine Learning**")

# เมนูด้านข้าง (Sidebar) สำหรับนำทาง
with st.sidebar:
    st.header("📋 เมนูบทเรียน")
    st.write("Choosak Tosong")
    st.info("7 Day Intensive Hands-on Workshop")
    st.markdown(''':rainbow["Operation Excellence"]''')
    st.caption("Day 1: การจัดการข้อมูลพื้นฐาน")

# ส่วนเนื้อหาหลัก: ใช้ Selectbox ในการเลือกเปลี่ยนหน้า
st.write("#### 💡 เลือกหัวข้อที่ต้องการตรวจสอบด้านล่าง:")

menu_options = {
    "--- กรุณาเลือกรายการ ---": None,
    "💰 ระบบคำนวณส่วนลดตามยอดซื้อ": "pages/app1_discount_calc.py",
    "👉 การทำความสะอาดข้อมูล": "pages/clean_tong (1).py",
    "👉 clean_customers": "pages/clean_customers.py",
    "👉 clean_app": "pages/clean_app.py",
    "👉 transform_app": "pages/transform_app.py",
    "👉 EDA_app": "pages/EDA_app.py",
    "👉 sale_predict.app": "pages/sale_predict.py",
    "👉 truck_predict.app": "pages/truck_predict.py"
}

selected_page = st.selectbox("ขั้นตอนการทำงาน (Workflow):", list(menu_options.keys()))

# ถ้าผู้ใช้เลือกเมนู (ที่ไม่ใช่หน้าว่าง) ให้เปลี่ยนหน้าทันที
if selected_page and menu_options[selected_page]:
    st.switch_page(menu_options[selected_page])

# แสดงโครงสร้าง Roadmap ของคอร์สแบบสวยงามด้านล่าง
st.divider()
st.write("📌 **Roadmap การเรียนรู้ในเซสชันนี้:**")
st.text("Data Preparation ➡️ Data Cleaning ➡️ EDA ➡️ Machine Learning Modeling")
