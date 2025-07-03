import cv2
from deepface import DeepFace

# Load OpenCV's pre-trained face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Define emotion detection function
def detect_emotion(frame):
    try:
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # If no face detected, return neutral
        if len(faces) == 0:
            return "neutral"

        # DeepFace emotion analysis (face is present)
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion'].lower()
        return emotion

    except Exception as e:
        print(f"[Emotion Detection Error]: {e}")
        return "neutral"


# Start webcam for testing
def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        emotion = detect_emotion(frame)

        # Display emotion on frame
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
