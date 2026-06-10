import streamlit as st

# --- 1. ส่วนของ CSS สำหรับตกแต่งสีปุ่ม ---
st.markdown("""
<style>
    /* ตั้งค่าพื้นฐานให้ปุ่ม */
    div.stButton > button {
        border-radius: 10px;
        height: 3em;
        transition: all 0.3s ease;
        border: none;
        color: white;
    }
    
    /* สีปุ่ม Transform (Blue) */
    button[key="btn_trans"] {
        background-color: #3498db !important;
    }
    /* สีปุ่ม EDA (Green) */
    button[key="btn_eda"] {
        background-color: #2ecc71 !important;
    }
    /* สีปุ่ม Sale Predict (Orange) */
    button[key="btn_pred1"] {
        background-color: #f39c12 !important;
    }
    /* สีปุ่ม Truck Predict (Purple) */
    button[key="btn_pred2"] {
        background-color: #9b59b6 !important;
    }
    /* สีปุ่ม Classify (Red) */
    button[key="btn_trans1"] {
        background-color: #e74c3c !important;
    }
    /* สีปุ่ม Clustering (Teal) */
    button[key="btn_pred4"] {
        background-color: #1abc9c !important;
    }

    /* เอฟเฟกต์เวลาเอาเมาส์ไปวาง (Hover) */
    div.stButton > button:hover {
        opacity: 0.8;
        transform: scale(1.02);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. ส่วนของ UI (โซนที่ 2) ---
with st.container(border=True):
    st.markdown("#### 📊 ขั้นตอนที่ 2: การวิเคราะห์และการทำโมเดลพยากรณ์ (Analytics & ML)")
    
    # แบ่งเป็น 2 แถว แถวละ 3 คอลัมน์เพื่อให้ดูสมดุล
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    
    with row1_col1:
        if st.button("🔄 Transform App", use_container_width=True, key="btn_trans"):
            st.switch_page("pages/transform_app.py")
        st.caption("การแปลงรูปแบบข้อมูลและการทำ Feature")
        
    with row1_col2:
        if st.button("📈 EDA App", use_container_width=True, key="btn_eda"):
            st.switch_page("pages/EDA_app.py")
        st.caption("สำรวจและหาความสัมพันธ์ด้วยกราฟ")
        
    with row1_col3:
        if st.button("🔮 Sale Predict", use_container_width=True, key="btn_pred1"):
            st.switch_page("pages/sale_predict.py")
        st.caption("โมเดลพยากรณ์ยอดขาย")
        
    st.divider() # ขีดเส้นคั่นบางๆ ระหว่างแถว
    
    row2_col1, row2_col2, row2_col3 = st.columns(3)

    with row2_col1:
        if st.button("🚛 Truck Predict", use_container_width=True, key="btn_pred2"):
            st.switch_page("pages/truck_predict.py")
        st.caption("โมเดลพยากรณ์รอบรถขนส่ง")
        
    with row2_col2:
        if st.button("🎯 Classify Redbull", use_container_width=True, key="btn_trans1"):
            st.switch_page("pages/classify_redbull_sale.py")
        st.caption("คาดการณ์ Product ที่มียอดขายสูง")

    with row2_col3:
        if st.button("🧬 Clustering Segment", use_container_width=True, key="btn_pred4"):
            st.switch_page("pages/clustering_segment.py")
        st.caption("คาดการณ์ Product การจัดกลุ่ม")
