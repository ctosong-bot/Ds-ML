# ================= Navigation & Workflow Section =================
st.write("### 🛠️ เรียนรู้ตามขั้นตอน (Data Science Workflow)")

# (โซนที่ 1 คงเดิม...)

st.write("") # เว้นช่องไฟเล็กน้อย

# โซนที่ 2: Transformation, EDA & Prediction
with st.container(border=True):
    st.markdown("#### 📊 ขั้นตอนที่ 2: การวิเคราะห์และการทำโมเดลพยากรณ์ (Analytics & ML)")
    
    # เจนคอลัมน์ขึ้นมา 4 คอลัมน์สำหรับปุ่มแถวแรก (ปุ่มที่ 5-8)
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

    # 💡 เพิ่มช่องไฟ และแตกคอลัมน์แถวใหม่ (col9, col10) เพื่อความสวยงาม ไม่เบียดกัน
    st.write("") 
    col9, col10, col11, col12 = st.columns(4)

    with col9:
        if st.button("🎯 Classify Redbull", use_container_width=True, key="btn_trans1"):
            st.switch_page("pages/classify_redbull_sale.py")
        st.caption("คาดการณ์ Product ที่มียอดขายสูง")

    with col10:
        if st.button("🧬 Clustering Segment", use_container_width=True, key="btn_pred4"):
            st.switch_page("pages/clustering_segment.py")
        st.caption("คาดการณ์การจัดกลุ่ม Product")
