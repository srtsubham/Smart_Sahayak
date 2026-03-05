import os
import shutil

import cv2
import pyttsx3

e = pyttsx3.init()
c = cv2.VideoCapture(0)
d = "cache"


def p():
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)


def s(t):
    e.say(t)
    e.runAndWait()


def m():
    f = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    b = None

    while True:
        r, f_m = c.read()

        # FIX: Check if frame is valid before processing
        if not r or f_m is None:
            cv2.waitKey(10)
            continue

        g = cv2.cvtColor(f_m, cv2.COLOR_BGR2GRAY)
        g = cv2.GaussianBlur(g, (21, 21), 0)

        if b is None:
            b = g
            continue

        i = cv2.absdiff(b, g)
        t_v = cv2.threshold(i, 25, 255, cv2.THRESH_BINARY)[1]
        t_v = cv2.dilate(t_v, None, iterations=2)
        k, _ = cv2.findContours(t_v.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        a = False
        for n in k:
            if cv2.contourArea(n) > 5000:
                a = True
                break

        if a:
            v = f.detectMultiScale(g, 1.1, 4)
            if len(v) > 0:
                p()
                s("How may I help you")
                return True  # Signal main.py to start interaction

        cv2.imshow("Smart Sahayak - Gateway", f_m)
        if cv2.waitKey(1) == ord("q"):
            break

    return False


if __name__ == "__main__":
    m()
