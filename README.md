# 📸 Smart Attendance System

The **Smart Attendance System** is a face recognition–based web application that automates attendance tracking from classroom images. It leverages deep learning and facial recognition models to detect and identify students from a group photo and returns a list of students who are present.

---

## 🚀 Features

- 📤 Upload classroom images via a user-friendly web interface.
- 🔍 Detect and recognize multiple faces using DeepFace and dlib.
- 🧾 Automatically mark and display attendance with student names.
- 💡 Memory-efficient and suitable for small teams and classrooms.
- 🖥️ Built using **Streamlit** for frontend and **Flask** for backend.

---

## 🧠 Tech Stack & Concepts

### 🔹 Python Libraries Used

| Library          | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| **Streamlit**    | Create interactive frontend for uploading images and showing output     |
| **Flask**        | Backend API to process uploaded images and return recognized names      |
| **face_recognition** | Face detection and encoding using dlib                              |
| **DeepFace**     | Alternative deep learning face recognition, supports multiple backends  |
| **dlib**         | ML library used internally by face_recognition for face encoding        |
| **OpenCV**       | (Optional) Pre-processing or face cropping from images                  |
| **pandas**       | Display recognized names in a tabular format                            |
| **requests**     | Send HTTP POST requests from frontend to backend                        |

---

## 📸 How It Works

1. 📤 The user uploads a classroom image via Streamlit.
2. 🧠 The image is sent to the Flask backend through an HTTP POST request (`/mark`).
3. ⚙️ Backend logic:
   - Saves the image temporarily.
   - Loads known faces from a folder.
   - Detects and encodes faces from the image.
   - Compares against known student encodings.
   - Matches faces and returns a list of present students.
4. ✅ The frontend displays:
   - Uploaded image.
   - A table of recognized students.
   - Success or error messages.

---

## ✅ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-attendance.git
cd smart-attendance
Here is a clean, correctly formatted, and complete version of the content you just posted — this can be directly included in your `README.md` under **Installation**, **Concepts Used**, and **Future Improvements** sections:

---

## ✅ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-attendance.git
cd smart-attendance
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If `dlib` fails to install, consider using a prebuilt `.whl` file from [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#dlib](https://www.lfd.uci.edu/~gohlke/pythonlibs/#dlib)

---

### 4. Run the Backend (Flask)

```bash
cd backend
python app.py
```

---

### 5. Run the Frontend (Streamlit)

In a **new terminal** window:

```bash
cd frontend
..\venv\Scripts\activate
streamlit run streamlit_app.py
```

---

## 📂 Preparing Known Faces

* Create a folder named `known_faces/` inside the `backend` directory.
* Add **clear, front-facing images** of each student.
* Name each image as: `Name_Surname.jpg`
  *(e.g., `Alice_Smith.jpg`, `John_Doe.jpg`)*
* These filenames are used to identify each student.

---

## 🧠 Concepts Used

### 🔍 Face Recognition

* **Face Encoding**: Each known face is converted into a 128-dimensional vector using `face_recognition` (dlib).
* **Face Matching**: Uploaded classroom faces are compared with known encodings using **Euclidean distance**.

### 🤖 Deep Learning (via DeepFace)

* Utilizes **pre-trained models** like **RetinaFace** for improved face detection.
* No model training required — only reference images are needed.

### 💾 State Management (Optional Enhancement)

* `st.session_state` (in Streamlit) can be used to **preserve attendance data** between multiple uploads during the same session.

---

## ⚠️ Limitations & Future Improvements

* ❌ **Only recognizes faces available in the known\_faces folder**
* 🌗 **Lighting, blur, or occlusions may reduce accuracy**
* 💾 **Add CSV or database saving feature** for attendance logs
* 📅 **Store timestamp** with each marked attendance
* 🧑‍🏫 **Add login authentication** for teachers/admins
* 🏫 **Support class-wise or subject-wise attendance reports**

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Contributor

* 👩‍💻 **Rifana Sherin** 

---

