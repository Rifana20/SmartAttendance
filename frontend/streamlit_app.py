import streamlit as st
import requests
import pandas as pd

st.title("📸 Smart Attendance System")

uploaded_file = st.file_uploader("Upload classroom image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())
    st.image("temp.jpg", caption="Uploaded Image", use_container_width=True)

    if st.button("Mark Attendance"):
        with open("temp.jpg", "rb") as f:
            files = {"file": f}
            try:
                res = requests.post("http://127.0.0.1:5000/mark", files=files)

                if res.status_code == 200:
                    names = res.json().get("present", [])
                    st.success("✅ Attendance Marked")
                    st.table(pd.DataFrame(names, columns=["Name"]))
                else:
                    st.error(f"❌ Server Error: {res.status_code}")
                    st.text(res.text)
                
                # ✅ Show response info only if res exists
                st.write("Response code:", res.status_code)
                st.write("Response text:", res.text)

            except Exception as e:
                st.error("❌ Failed to connect to backend")
                st.text(str(e))
