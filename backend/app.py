from flask import Flask, request, jsonify
from face_recognition_logic import recognize_faces
import os

app = Flask(__name__)

@app.route('/mark', methods=['POST'])
def mark_attendance():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        temp_path = os.path.join("temp.jpg")
        file.save(temp_path)

        present = recognize_faces(temp_path)
        return jsonify({"present": present})
    
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
