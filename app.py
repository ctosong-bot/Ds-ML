import streamlit as st

st.set_page_config(page_title="Data Science & ML Boot Camp", layout="wide", page_icon="🏠")

# ================= Header Section =================
st.title("🏠 Dashboard หน้าหลัก")
st.write("## Boot Camp: Data Science and Machine Learning")

# ออกแบบ Banner ข้อมูลขนาดเล็กด้วย Columns
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    st.info("💡 **Course:** 7 Day Intensive Hands-on Workshop")
with c2:
    st.success("👨‍🏫 **Instructor:** Choosak Tosong")
with c3:
    st.markdown("<div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 5px;'>🚀 <b>Operation Excellence</b></div>", unsafe_allow_html=True)

st.caption("📅 **Day 1 Focus:** การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
st.divider()

# ================= Navigation & Workflow Section =================
st.write("### 🛠️ เรียนรู้ตามขั้นตอน (Data Science Workflow)")

# โซนที่ 1: Data Preparation & Cleaning
with st.container(border=True):
    st.markdown("#### 🧹 ขั้นตอนที่ 1: การเตรียมข้อมูลและการทำความสะอาด (Data Prep)")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("💰 ระบบคำนวณส่วนลด", use_container_width=True, key="btn_calc"):
            st.switch_page("pages/app1_discount_calc.py")
        st.caption("คำนวณส่วนลดตามยอดซื้อพื้นฐาน")
        
    with col2:
        if st.button("🧼 Clean Tong (1)", use_container_width=True, key="btn_clean1"):
            st.switch_page("pages/clean_tong (1).py")
        st.caption("เวิร์กชอปทำความสะอาดข้อมูลชุดที่ 1")
        
    with col3:
        if st.button("👤 Clean Customers", use_container_width=True, key="btn_clean2"):
            st.switch_page("pages/clean_customers.py")
        st.caption("จัดการ Missing/Duplicate ของลูกค้า")
        
    with col4:
        if st.button("📱 Clean App Data", use_container_width=True, key="btn_clean3"):
            st.switch_page("pages/clean_app.py")
        st.caption("เคลียข้อมูลดิบจากระบบแอปพลิเคชัน")

st.write("") # เว้นช่องไฟเล็กน้อย

# โซนที่ 2: Transformation, EDA & Prediction
with st.container(border=True):
    st.markdown("#### 📊 ขั้นตอนที่ 2: การวิเคราะห์และการทำโมเดลพยากรณ์ (Analytics & ML)")
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        if st.button("🔄 Transform App", use_container_width=True, key="btn_trans"):
            st.switch_page("pages/transform_app.py")
        st.caption("การแปลงรูปแบบข้อมูลและการทำ Feature")
        
    with col6:
        if st.button("📈 EDA App", use_container_width=True, key="btn_eda"):
            st.switch_page("pages/EDA_app.py")
        st.caption("สำรวจและหาความสัมพันธ์ด้วยกราฟ")
        
    with col7:
        if st.button("🔮 Sale Predict", use_container_width=True, key="btn_pred1"):
            st.switch_page("pages/sale_predict.py")
        st.caption("โมเดลพยากรณ์ยอดขาย")
        
    with col8:
        if st.button("🚛 Truck Predict", use_container_width=True, key="btn_pred2"):
            st.switch_page("pages/truck_predict.py")
        st.caption("โมเดลพยากรณ์รอบรถขนส่ง")
    with col8:
        if st.button("🚛 classify_redbull_sale", use_container_width=True, key="btn_pred3"):
            st.switch_page("pages/classify_redbull_sale.py")
        st.caption("คาดการ Product ที่มียอดขายสูง")
    with col8:
        if st.button("🚛 clustering_segment", use_container_width=True, key="btn_pred3"):
            st.switch_page("pages/clustering_segment.py")
        st.caption("คาดการ Product การจัดกลุ่ม")
