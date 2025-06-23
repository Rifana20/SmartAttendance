import streamlit as st
import requests
import pandas as pd

st.title("📸 Smart Attendance System")

# Initialize session state to keep history
if "attendance_history" not in st.session_state:
    st.session_state.attendance_history = []

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
                    if names:
                        st.success("✅ Attendance Marked")
                        # Extend history with new names
                        st.session_state.attendance_history.extend(names)
                    else:
                        st.warning("⚠️ No known students matched in the image.")
                    
                    # Remove duplicates and show as table
                    unique_names = list(set(st.session_state.attendance_history))
                    st.table(pd.DataFrame(unique_names, columns=["Name"]))

                    st.write("Response code:", res.status_code)
                    st.write("Response text:", res.text)
                else:
                    st.error(f"❌ Server Error: {res.status_code}")
                    st.text(res.text)

            except Exception as e:
                st.error("❌ Failed to connect to backend")
                st.text(str(e))
