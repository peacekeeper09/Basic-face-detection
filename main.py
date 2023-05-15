import cv2
import PySimpleGUI as sg
import numpy as np

sg.theme('DarkBlue')
layout = [
    [sg.Image(filename='', key='-IMAGE-')],
    [sg.Text('Face Name: '), sg.InputText(key='-NAME-'), sg.Button('Register')],
    [sg.Text('Detected Face: '), sg.Text('', key='-DETECTED-')],
    [sg.Exit()]
]
window = sg.Window('Face Recognition', layout, finalize=True)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

registered_faces = {}

while True:
    event, values = window.read(timeout=20)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if event == 'Register':
            face_name = values['-NAME-']
            face_image = frame[y:y+h, x:x+w]
            registered_faces[face_name] = face_image

    if len(faces) > 0:
        for name, face_image in registered_faces.items():
            resized_face = cv2.resize(face_image, (w, h))
            gray_registered = cv2.cvtColor(resized_face, cv2.COLOR_BGR2GRAY)
            gray_detected = gray[y:y+h, x:x+w]
            diff = cv2.absdiff(gray_registered, gray_detected)
            mean_diff = np.mean(diff)

            if mean_diff < 20:
                window['-DETECTED-'].update(name)
                break
        else:
            window['-DETECTED-'].update('Unknown')

    imgbytes = cv2.imencode('.png', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))[1].tobytes()
    window['-IMAGE-'].update(data=imgbytes)

cap.release()
cv2.destroyAllWindows()
window.close()
