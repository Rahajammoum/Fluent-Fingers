<p align="center">
  <img src="banner2.png" alt="Fluent Fingers Banner" width="65%">
</p>
# Fluent Fingers: ASL to English Translation App

**Fluent Fingers** is an AI-powered web app that translates American Sign Language (ASL) into English in real time. Using YOLOv5 for hand sign detection and Flask + React for full-stack integration, the app helps break communication barriers between the deaf and hearing communities.

---

## 🚀 Features

- 🔤 Real-time ASL alphabet detection via webcam
- 🤖 Custom-trained YOLOv5 model with 400+ epochs
- 🌐 Flask backend + React frontend
- 🧠 Uses OpenCV for camera capture and annotation
- 🎯 95% confidence threshold for accurate prediction
- 🧑‍🤝‍🧑 Designed for accessibility and inclusivity

---

## 🧰 Tech Stack

| Component      | Tech Used                         |
|----------------|-----------------------------------|
| Model Training | Python, PyTorch, YOLOv5           |
| Image Capture  | OpenCV                            |
| Backend        | Flask, Flask-SocketIO             |
| Frontend       | React, JavaScript                 |
| Dataset Tool   | Roboflow for annotation           |

---

## 🏗️ Architecture
Camera Input → OpenCV → YOLOv5 (best.pt) → Flask (API) → React (UI)

## 📁 Folder Structure
fluent-fingers/
├── backend/
│   └── app.py, model/
├── frontend/
│   └── React UI (App.js, components)
├── dataset/
│   └── CollectedImages, annotations
├── LICENSE
├── README.md
├── banner.png

## 🎓 Capstone Team
Raha Jammoum – LinkedIn

Mariam Youssef – mariamayoussef@gmail.com

Reema Mahgana – reema-mahagna@outlook.com

## 🧑‍🏫 Supervisor
Dr. Femilda Josephin Joseph Shobana Bai

## 🏫 İstinye University, Department of Computer Engineering (2024)


## 🔐 License
This project is not open-source.
## 📜 All rights reserved by the authors. Do not copy, reproduce, or use without explicit written permission.

## 🧠 Future Ideas
Voice-to-text output

Phrase-level translation

Mobile version (React Native)

Multilingual output

Adaptive ASL learning assistant


