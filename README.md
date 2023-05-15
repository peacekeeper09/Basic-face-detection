# Face Recognition with GUI

This Python program demonstrates face recognition using a webcam with a graphical user interface (GUI). It allows users to register their faces and associate them with names. Once registered, the program can detect and recognize the registered faces in real-time.

## Features

- Real-time face detection and recognition using the webcam.
- Graphical user interface (GUI) built with PySimpleGUI for a user-friendly experience.
- Registration of new faces by capturing an image from the webcam and associating it with a name.
- Automatic face matching against the registered faces using mean pixel difference.
- Display of the recognized face name in the GUI window.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3
- OpenCV (cv2) library
- PySimpleGUI library
- haarcascade_frontalface_default.xml (Haar Cascade classifier for face detection)

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using pip: `pip install opencv-python PySimpleGUI`.
3. Download the `haarcascade_frontalface_default.xml` file and place it in the same directory as the script. You can download it from the official OpenCV GitHub repository.
4. Run the script: `python main.py`.
5. The GUI window will open, showing the webcam feed.
6. To register a face, enter a name in the "Face Name" field and click the "Register" button when your face is in view.
7. The program will capture the face image and associate it with the provided name.
8. To detect and recognize faces, simply let the program run. The recognized face name will be displayed in the "Detected Face" field if a registered face is matched, otherwise it will show "Unknown".
9. Press the "Exit" button or close the window to stop the program.

