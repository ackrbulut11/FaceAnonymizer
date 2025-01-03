# Face Detection and Blurring

## Overview
This is a simple Python project for real time face detection and blurring using OpenCV and MediaPipe. It processes video input from the webcam and applies a blur effect to detected faces.

---

## Code Explanation
### mp_detectFace Function
- **Purpose**: Detects faces using MediaPipe's FaceDetection model.
- **Parameters**:
  - `img`: Input image from the webcam.
  - `face_detection`: Preloaded MediaPipe face detection model.
- **Key Steps**:
  1. Converts the image from BGR to RGB (MediaPipe works with RGB).
  2. Processes the image to detect faces.
  3. Extracts bounding box coordinates based on detected faces.

### blurFace Function
- **Purpose**: Blurs detected face regions.
- **Parameters**:
  - `img`: Input image with detected face.
  - `bbox`: Coordinates of the face region.
- **Key Steps**:
  1. Extracts the face region using bounding box values.
  2. Dynamically calculates kernel size for Gaussian blur based on face size.
  3. Applies Gaussian blur and replaces the original face with the blurred one.

### main Function
- **Purpose**: Controls webcam input and integrates detection and blurring.
- **Key Steps**:
  1. Initializes webcam and MediaPipe model.
  2. Continuously reads frames, detects faces, and applies blur.
  3. Displays the processed frames until the user quits with 'q'.

---

![Example Output](example_output.png)

