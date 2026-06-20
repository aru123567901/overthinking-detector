# 🧠 Overthinking Detection Web App

An AI-powered web application that analyzes text input to detect overthinking patterns using hybrid NLP techniques (keyword matching + TextBlob sentiment analysis + pattern recognition).

## 🌐 Live Demo

🔗 **https://overthinking-detector.onrender.com**

---

## 🎯 Features

- **Real-time Analysis** - Instant text processing and feedback
- **0-20 Scoring System** - Quantifies overthinking intensity
- **10+ Cognitive Distortions Detected**:
  - 🎭 Mind Reading - Assuming you know what others think
  - 🔮 Catastrophizing - Expecting worst-case scenarios
  - 🔄 Rumination - Stuck replaying past events
  - 👥 Social Anxiety - Fear of being judged
  - 😔 Self-Blame - Excessive personal responsibility
  - ⚫ Absolute Language - "Always", "Never", "Everything"
  - 🔮 Future Anxiety - Worry about what's coming
  - 🔁 Repetitive Thinking - Looping on same thoughts
  - 📈 Catastrophic Escalation - Small trigger → huge consequences
  - 🚫 Avoidance Behavior - Withdrawing from situations
- **Personalized Advice** - Coping strategies based on severity level
- **Interactive UI** - Clean, modern web interface

---

## 📊 Scoring System

| Score Range | Level | What It Means |
|-------------|-------|---------------|
| 0-8 | 🟢 Normal/Healthy Thinking | No overthinking detected |
| 9-12 | 🟡 Low Overthinking | Mild worry, easily manageable |
| 13-16 | 🟠 Moderate Overthinking | Stuck in thought loops |
| 17-19 | 🔴 Significant Overthinking | Intense rumination |
| 20 | 💀 High Overthinking | Severe, needs intervention |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, Flask |
| **NLP** | TextBlob |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Pattern Matching** | Regex |
| **Deployment** | Render |

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.12+
- pip package manager

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

Author 
Aruhi Patel

License
MIT

