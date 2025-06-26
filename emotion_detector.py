from deepface import DeepFace

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion'].lower()
    except Exception as e:
        print(f"[Emotion Detection Error]: {e}")
        return "neutral"
