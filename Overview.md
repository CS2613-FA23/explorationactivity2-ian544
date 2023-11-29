# OpenCV: An In-Depth Exploration

## 1. Selected Package/Library
**OpenCV (Open Source Computer Vision)**

## 2. About OpenCV
OpenCV is an open-source computer vision and machine learning software library. It is designed to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception. OpenCV is widely used in academia, research, and industry for tasks ranging from simple image processing to complex computer vision applications. [2]

### Purpose and Usage
- **Purpose**: OpenCV aims to provide a comprehensive set of tools for image and video analysis, enabling developers to build applications with advanced computer vision capabilities. [2]
- **Usage**: It can be used with various programming languages such as Python, C++, and Java. The library provides a range of functionalities for image and video processing, including feature detection, object recognition, and machine learning. [2]

### How to Use OpenCV
To use OpenCV in Python, you typically start by installing it: 
```bash
pip install opencv-python
```
Then, you can import the library and start using its functions in your code. [1]

## 3. Functionalities of OpenCV
OpenCV offers a wide range of functionalities, including:

- Image and Video Capture
- Image Processing (Blurring, Sharpening, etc.)
- Object Detection and Recognition
- Facial Recognition
- Machine Learning Support [2]

### Code Snippet Example of Generic OpenCV Python Program
```python
import cv2

# Read an image from file
img = cv2.imread('image.jpg')

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Detect faces in the image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(blurred_img, 1.3, 5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
```

## 4. Creation Date
OpenCV was initially created in 1999 by Gary Bradsky and later supported by Intel. [2]

## 5. Why OpenCV?
I selected OpenCV for its robustness and versatility in computer vision applications. Its extensive set of tools and community support make it a go-to library for various projects, from simple image processing to complex machine learning tasks. It also seemed like a relatively simple way for me to dip my toe into computer vision, as I knew nothing about computer vision before the activity.

## 6. Influence on Learning
Learning OpenCV significantly enhanced my understanding of computer vision concepts, image processing techniques, and how to apply them in real-world scenarios. It provided practical insights into handling image data and extracting meaningful information. 

## 7. Overall Experience and Recommendations
My experience with OpenCV has been overwhelmingly positive. I would recommend it to anyone working on computer vision projects, whether they are beginners or experienced developers. The library's vast documentation and community support make it accessible and enjoyable to work with. My only complaint is that it took me a while to figure out how to get my program to access the xml file from the openCV library. I recommend just downloading the file you're looking for from the internet (the one I wanted was available on GitHub) and putting it in your programs directory.

### Would I Continue Using OpenCV?
Absolutely. The continuous development and improvement of OpenCV, coupled with its widespread adoption, make it a valuable tool for anyone involved in image and video analysis. 

## References 
- [1] https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- [2] https://learning.oreilly.com/library/view/learning-opencv/9780596516130/ch01.html#what_is_opencv