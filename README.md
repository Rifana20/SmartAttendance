

```markdown
# 📸 Smart Attendance System

The Smart Attendance System is a face recognition–based web application that automates attendance tracking from classroom images. It uses deep learning and facial recognition models to detect and identify students from a group photo and returns a list of students who are present.

---

## 🚀 Features

- 📤 Upload classroom images directly via a simple web interface.
- 🔍 Detect and recognize multiple faces using DeepFace and dlib.
- 📋 Mark attendance with names of detected individuals.
- 🧠 Memory-efficient and lightweight model usage.
- 🧾 View and store attendance history during session.
- 🖥️ Built using **Streamlit** for frontend and **Flask** for backend.

---

## 🧠 Tech Stack & Concepts

### 🔹 Python Libraries

| Library | Purpose |
|--------|---------|
| **Streamlit** | Frontend web app for uploading images and displaying results |
| **Flask** | Lightweight Python backend to handle API requests |
| **face_recognition** | Uses dlib under the hood to detect and recognize faces |
| **DeepFace** | Alternative face detection/recognition framework supporting RetinaFace |
| **dlib** | C++ based machine learning library for facial recognition |
| **OpenCV** | (Optional) Used for advanced face detection/processing |
| **pandas** | Displays the list of present students in table format |
| **requests** | Connects frontend to backend via POST API calls |

---


---

## 📸 How It Works

1. User uploads an image using the Streamlit interface.
2. Image is sent to the Flask backend via HTTP POST request (`/mark` endpoint).
3. The backend:
   - Saves the image temporarily.
   - Loads known faces from the `known_faces/` folder.
   - Detects all faces in the uploaded image using `face_recognition` or `DeepFace`.
   - Compares each detected face to known students.
   - Returns a list of matched names.
4. The frontend displays:
   - Uploaded image.
   - Names of recognized students in a table.
   - Any relevant success or error messages.

---

## ✅ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-attendance.git
cd smart-attendance
````

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

You may also need to install `dlib` using a precompiled `.whl` file if your system doesn’t support building it from source.

### 4. Run Backend (Flask)

```bash
cd backend
python app.py
```

### 5. Run Frontend (Streamlit)

In a new terminal:

```bash
cd frontend
..\venv\Scripts\activate  # Activate the same virtual environment
streamlit run streamlit_app.py
```

---

## 📂 Preparing Known Faces

* Create a `known_faces/` folder in the backend directory.
* Add clear, front-facing images of students.
* Name each image using this format: `Name_Surname.jpg`
* The face recognition logic extracts the name from the file name.

---

## 🧠 Concepts Used

### 🔍 Face Recognition

* Face encoding: Each face is converted into a unique 128-dimensional vector.
* Face comparison: New faces are compared against known vectors using Euclidean distance.

### 🧠 Deep Learning

* Pretrained models like **dlib** or **RetinaFace** are used under the hood.
* No training required — just use reference images for comparison.

### 🧠 Session State

* Streamlit’s `st.session_state` is used to persist attendance data across multiple uploads during the same session.

---

## ⚠️ Limitations & Future Improvements

* ❌ Cannot recognize new students not in the reference folder.
* 📷 Accuracy depends on lighting and face visibility in classroom images.
* 🧠 Add support for saving attendance to CSV or database.
* 🕒 Track timestamp with each attendance.
* 🎓 Add login for teachers and different classes.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ✨ Contributors

* **Rifana Sherin** – Developer, UI Designer, and ML integrator

---

## 📬 Contact

For any questions or feedback, please reach out via [LinkedIn](https://www.linkedin.com/in/rifanasherin) or [email](mailto:youremail@example.com).

```

---

Would you like to also generate a sample `requirements.txt` or add GitHub push instructions with `.gitignore`?
```


