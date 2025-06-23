# 📸 Smart Attendance System

The **Smart Attendance System** is a web-based application that automates attendance marking using facial recognition. By uploading a classroom image, the system detects and recognizes faces based on a set of known student images and displays the names of those present.

---

## 🚀 Features

- 📤 Upload classroom images directly via the web interface  
- 🔍 Detect and recognize multiple faces using deep learning  
- 📋 Display recognized names in a structured table  
- ✅ Lightweight and runs locally  
- 🔁 Mark attendance from multiple images one at a time  

---

## 🧠 Tech Stack Used

### 🔹 Frontend (Streamlit)

| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `streamlit`   | Web interface for image upload and display   |
| `requests`    | Sends uploaded images to Flask backend       |
| `pandas`      | Displays attendance results in table format  |

### 🔹 Backend (Flask)

| Library             | Purpose                                             |
|---------------------|-----------------------------------------------------|
| `flask`             | Backend web server and route handler                |
| `face_recognition`  | Face detection and encoding using dlib              |
| `deepface`          | Alternative detection using RetinaFace (optional)   |
| `dlib`              | Used internally for facial landmark detection       |
| `os`                | Handling file paths and temp image management       |
| `tf-keras`          | Required backend dependency for DeepFace            |

---

## 📸 How It Works

1. The user uploads an image via the Streamlit UI.  
2. The image is saved temporarily as `temp.jpg`.  
3. A POST request is sent to the Flask backend at `http://127.0.0.1:5000/mark`.  
4. The backend:  
   - Loads known faces from a local folder (`known_faces/`)  
   - Uses `face_recognition` to detect faces in the uploaded image  
   - Compares each face against known encodings  
   - Returns a list of matched student names  
5. The frontend displays the uploaded image and a table of recognized names.

---

## ✅ Local Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-attendance.git
cd smart-attendance

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

You may need to manually install a `.whl` file for `dlib` if build fails.

### 4. Run the Backend (Flask)

```bash
cd backend
python app.py
```

### 5. Run the Frontend (Streamlit)

Open a **new terminal**, activate the same virtual environment:

```bash
cd frontend
..\venv\Scripts\activate
streamlit run streamlit_app.py
```

---

## 📂 Preparing Known Faces

* Create a folder named `known_faces/` inside the `backend` directory.
* Add one clear image per student (frontal face).
* File names must be in the format: `Name_Surname.jpg`.
* These names will be extracted for attendance display.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ✨ Contributor

* **Rifana Sherin**


