from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import re

app = Flask(__name__)

def detect_overthinking(text):
    score = 0
    reasons = []
    text_lower = text.lower()
    blob = TextBlob(text)

    # Social anxiety keywords
    social_keywords = [
        'everyone was looking', 'everyone looked', 'everyone is looking',
        'everybody looked', 'people were looking', 'they were looking',
        'they stared', 'they saw me', 'they noticed me'
    ]
    for word in social_keywords:
        if word in text_lower:
            score += 4
            reasons.append(f"👥 Social anxiety: '{word}'")
            break

    # Mind reading keywords
    mind_reading = [
        'they think', 'they must', 'they probably', 'they will think',
        'everyone thinks', 'people think', 'they judge', 'they are thinking',
        'i know they', 'what will they think', 'what do they think'
    ]
    for word in mind_reading:
        if word in text_lower:
            score += 5
            reasons.append(f"🎭 Mind reading: '{word}'")
            break

    # Self-blame keywords
    self_blame = [
        'my fault', 'i messed up', 'i ruined', 'i failed',
        'i should have', 'i could have', 'i would have',
        'i did something wrong', 'i made a mistake'
    ]
    for word in self_blame:
        if word in text_lower:
            score += 4
            reasons.append(f"😔 Self-blame: '{word}'")
            break

    # Catastrophizing keywords
    catastrophizing = [
        'what if i fail', 'what if i mess up', 'what if i ruin',
        'worst case', 'worst thing', 'terrible', 'awful',
        'everything is wrong', 'nothing works'
    ]
    for word in catastrophizing:
        if word in text_lower:
            score += 5
            reasons.append(f"🔮 Catastrophizing: '{word}'")
            break

    # Future anxiety
    future_anxiety = [
        'tomorrow', 'next week', 'coming up', 'will happen',
        'what will', 'how will', 'what if they', 'what if i'
    ]
    future_count = sum(1 for w in future_anxiety if w in text_lower)
    if future_count >= 2:
        score += 3
        reasons.append("🔮 Future anxiety detected")

    # Repetitive thinking
    repetitive = ['keep thinking', 'can\'t stop thinking', 'replaying', 'going over',
                  'again and again', 'over and over', 'stuck in my head']
    for word in repetitive:
        if word in text_lower:
            score += 4
            reasons.append(f"🔄 Repetitive thinking: '{word}'")
            break

    # Absolute language
    absolutes = ['always', 'never', 'everything', 'nothing', 'everyone', 'nobody']
    for word in absolutes:
        if word in text_lower:
            score += 3
            reasons.append(f"⚫ Absolute thinking: '{word}'")
            break

    # Questions (racing thoughts)
    question_count = text.count('?')
    if question_count >= 2:
        score += 3
        reasons.append(f"❓ Racing thoughts ({question_count} questions)")

    # Escalation patterns
    if re.search(r'(if|when) .* (then|that will) .* (over|awkward|ruined)', text_lower):
        score += 4
        reasons.append("📈 Catastrophic escalation detected")

    # Avoidance behavior
    if re.search(r'(maybe|perhaps) .* (stop|quit|give up|avoid)', text_lower):
        score += 3
        reasons.append("🚫 Avoidance behavior detected")

    # Question storm (4+ questions)
    if question_count >= 4:
        score += 4
        reasons.append(f"❓ Question storm ({question_count} questions in a row)")

    # Thought loop
    if re.search(r'(can\'t stop thinking|keep thinking|can\'t get it out of my head)', text_lower):
        score += 3
        reasons.append("🌀 Thought loop detected")

    # Rumination over time
    if re.search(r'(hours|days|weeks|keeps|still)', text_lower):
        score += 2
        reasons.append("⌛ Extended rumination over time")

    # TEXTBLOB SENTIMENT
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity < -0.3:
        score += 5
        reasons.append("😢 Strong negative emotion")
    elif polarity < -0.1:
        score += 2
        reasons.append("📉 Negative tone")
    elif polarity > 0.3:
        score = max(0, score - 3)
        reasons.append("😊 Positive tone detected (-3)")

    if subjectivity > 0.6 and polarity < -0.1:
        score += 3
        reasons.append("🎭 Highly emotional/subjective thinking")

    # Self-focus
    self_count = text_lower.count(' i ') + text_lower.count(' me ') + text_lower.count(' my ') + text_lower.count(" i'm ")
    if self_count >= 4:
        score += 3
        reasons.append(f"🎯 High self-focus ({self_count} references)")

    # Uncertainty
    uncertainty = ['maybe', 'perhaps', 'probably', 'i think', 'i guess', 'not sure']
    uncertainty_count = sum(1 for w in uncertainty if w in text_lower)
    if uncertainty_count >= 2:
        score += 3
        reasons.append(f"🤔 High uncertainty ({uncertainty_count} indicators)")

    # Length (rumination)
    word_count = len(text.split())
    if word_count > 100:
        score += 3
        reasons.append(f"📝 Extended rumination ({word_count} words)")

    # CALM THINKING (REDUCES SCORE)
    calm_phrases = [
        "it's fine", "it's okay", "i can handle", "no problem",
        "not a big deal", "that's normal", "it happens",
        "everyone makes mistakes", "i'll try again", "next time"
    ]
    for word in calm_phrases:
        if word in text_lower:
            score = max(0, score - 4)
            reasons.append("✅ Calm thinking detected (-4)")
            break

    # FINAL SCORE
    score = min(20, max(0, score))

    if score <= 8:
        level = "🟢 Normal/Healthy Thinking"
        advice = "No overthinking detected. Your thinking seems balanced."
        color = "#4CAF50"
    elif score <= 12:
        level = "🟡 Low Overthinking"
        advice = "Mild worry detected. Try taking 5 deep breaths."
        color = "#FFC107"
    elif score <= 16:
        level = "🟠 Moderate Overthinking"
        advice = "You're showing signs of overthinking. Step away for 5 minutes."
        color = "#FF9800"
    elif score <= 19:
        level = "🔴 Significant Overthinking"
        advice = "Intense rumination detected. Try grounding exercises."
        color = "#F44336"
    else:
        level = "💀 High Overthinking"
        advice = "Your mind is in overdrive. Take a real break."
        color = "#9C27B0"

    return {
        'score': score,
        'level': level,
        'advice': advice,
        'reasons': reasons[:5],
        'color': color
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    if not text or len(text.strip()) < 10:
        return jsonify({
            'score': 0,
            'level': "🟢 Normal Thinking",
            'advice': "Type something longer to analyze",
            'reasons': [],
            'color': "#4CAF50"
        })

    result = detect_overthinking(text)
    return jsonify(result)


if __name__ == '__main__':
    print("=" * 55)
    print("🧠 HYBRID OVERTHINKING DETECTOR")
    print("   Keywords + TextBlob + Patterns")
    print("=" * 55)
    print("Server: http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True)