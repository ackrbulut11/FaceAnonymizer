import cv2
import mediapipe as mp 

"""
# face detection with haarcascade
def detectFace(img):

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # convert color bgr to gray
    haar_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(haar_cascade_path)

    faces = haar_cascade.detectMultiScale(gray_img, 1.1, 5)

    return faces
"""

# Face detection with mediapipe
def mp_detectFace(img, face_detection):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(imgRGB)

    bboxes = []
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            h, w, _ = img.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
            bboxes.append(bbox)

    return bboxes


# Blurring
def blurFace(img, bbox):
    x, y, w, h = bbox
    face = img[y:y + h, x:x + w]
    k = (w // 10 * 2 + 1, h // 10 * 2 + 1)  # Dynamic kernel size
    blurredFace = cv2.GaussianBlur(face, k, 20)
    img[y:y + h, x:x + w] = blurredFace

    return img


def main():
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Error: Could not open webcam.")
        return

    # Initialize mediapipe model once
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

    while True:
        ret, frame = webcam.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect faces
        bboxes = mp_detectFace(frame, face_detection)

        # Blur faces
        for bbox in bboxes:
            frame = blurFace(frame, bbox)

        cv2.imshow("Face Blurring", frame)

        # Quit on 'q'
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

    webcam.release()
    cv2.destroyAllWindows()


main()
