from deepface import DeepFace
import os
import cv2

# Load and encode known faces
def load_known_faces():
    face_db = {}
    for fn in os.listdir("registered_faces"):
        name = "_".join(fn.split("_")[:-1])
        img = cv2.imread(f"registered_faces/{fn}")
        if img is not None:
            face_db.setdefault(name, []).append(img)
    return face_db

KNOWN = load_known_faces()

def recognize_faces(upload_path):
    img = cv2.imread(upload_path)
    detections = DeepFace.extract_faces(img_path=upload_path, enforce_detection=False)
    present = set()
    for det in detections:
        face_img = det["face"]
        # Compare with each known student
        for name, imgs in KNOWN.items():
            for known_img in imgs:
                resp = DeepFace.verify(face_img, known_img, enforce_detection=False)
                if resp["verified"]:
                    present.add(name)
                    break
    return list(present)
