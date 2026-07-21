# 🩺 Healthy Bot – AI-Powered Student Health Assistant

Healthy Buddy is an AI-powered health chatbot designed to provide students with reliable health awareness and educational guidance in a simple, interactive, and child-friendly interface.

> ⚠️ This project is intended for educational purposes only and does not replace professional medical advice.

---

## 📌 Features

- 🤖 AI-powered health assistance
- 💬 Interactive real-time chat interface
- 🎨 Modern responsive UI
- 🩺 Answers only health-related questions
- ⚡ Fast responses using Groq AI API
- 😊 Simple language with emojis for better understanding
- 🚨 Safety mechanism for serious illnesses:
  - Provides general precautions
  - Advises users to consult a certified doctor
  - Does not diagnose diseases or prescribe medicines

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### AI Integration
- Groq API

### Libraries
- Flask
- Requests
- python-dotenv

---

## 📁 Project Structure

```
HealthyBot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── static.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/HealthyBuddy.git
```

---

### 2. Open the project

```bash
cd HealthyBuddy
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
API_KEY=YOUR_GROQ_API_KEY
```

---

### 5. Run the application

```bash
python app.py
```

---

### 6. Open in your browser

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. User enters a health-related question.
2. JavaScript sends the message to the Flask backend.
3. Flask forwards the request to the Groq AI API.
4. AI generates a response following predefined safety instructions.
5. The response is displayed in the chatbot interface.

---

## 🔒 Safety Features

Healthy Buddy follows responsible AI principles by:

- Providing educational information only
- Avoiding diagnosis and prescription of medicines
- Encouraging users to consult healthcare professionals for serious conditions
- Restricting responses to health-related topics
- Using a controlled system prompt to improve response safety

---

## 🚀 Future Improvements

- User authentication
- Chat history
- Voice input
- Multilingual support
- Nearby hospital locator
- Doctor integration
- Emergency contact feature
- Personalized health tips

---

## 📸 Screenshots

Add screenshots of your chatbot here.

Example:

```
screenshots/home.png
screenshots/chat.png
```

---

## 👨‍💻 Team

Developed as a hackathon project.

Project Name:
**Healthy Buddy – AI Student Health Assistant**

---


## ⚠️ Disclaimer

Healthy Buddy is an AI-powered educational chatbot.

It does **not** diagnose diseases, prescribe medicines, or replace professional healthcare services.

Users experiencing severe symptoms or medical emergencies should immediately consult a qualified healthcare professional or visit the nearest medical facility.

---

## ⭐ Acknowledgements

- Flask
- Groq API
- Moonshot AI (Kimi K2)
- Python
- HTML, CSS & JavaScript
