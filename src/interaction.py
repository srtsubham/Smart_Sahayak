import pyttsx3
import speech_recognition as r

s = r.Recognizer()
e = pyttsx3.init()


def t(m):
    e.say(m)
    e.runAndWait()


def l():
    with r.Microphone() as h:
        a = s.listen(h)
        try:
            q = s.recognize_google(a)
            return q.lower()
        except:
            return ""


def i():
    u = l()
    if "print" in u:
        t("Here you canget black and white, colour prints along with binidngs too")
    elif "pen" in u or "stationery" in u:
        t("Accessing stationery dispenser")
    else:
        t("I did not catch that. Could you repeat")


if __name__ == "__main__":
    i()
