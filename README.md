# 🧠 Overthinking Detection Web App

An AI-powered web application that analyzes text input to detect overthinking patterns using hybrid NLP techniques.

## 🎯 Features
- Real-time text analysis
- 0-20 overthinking scoring system
- Detects 10+ cognitive distortions:
  - Mind reading
  - Catastrophizing
  - Rumination
  - Social anxiety
  - Self-blame
  - Absolute language
  - Future anxiety
  - Repetitive thinking
  - Avoidance behavior
  - Question storm
- Personalized coping advice
- Interactive web interface

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **NLP:** TextBlob
- **Frontend:** HTML, CSS, JavaScript
- **Pattern Detection:** Regex

## 📊 Scoring System
| Score | Level |
|-------|-------|
| 0-8 | 🟢 Normal/Healthy Thinking |
| 9-12 | 🟡 Low Overthinking |
| 13-16 | 🟠 Moderate Overthinking |
| 17-19 | 🔴 Significant Overthinking |
| 20 | 💀 High Overthinking |

## 🚀 How to Run Locally

1. Clone the repository:
 git clone https://github.com/YOUR_USERNAME/overthinking-detector.git
cd overthinking-detector
2.install dependencies:
pip install flask textblob
python -m textblob.download_corpora
3.Run the app:
python app.py
4.Open your browser:
Go to http://127.0.0.1:5000

Example Input:
"Everyone was looking at me when I walked in late. I know they were judging me. They probably think I'm so unprofessional."

Project Structure:

overthinking-detector/
├── app.py
├── templates/
│ └── index.html
├── requirements.txt
├── .gitignore
└── README.md
