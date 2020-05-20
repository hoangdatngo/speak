from flask import Flask, render_template, request, redirect
import speech_recognition
import pyaudio
app = Flask(__name__)
text = ""
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)

        # Recognize speech using Google Speech Recognition
        print("Google Speech Recognition thinks you said:")
        text = recognizer.recognize_google(audio)
        redirect("/translate")

@app.route("/translate")
def translate():
    return render_template("translate.html", text=text)
if __name__ == "__main__":
    app.run(debug=True)