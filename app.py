from flask import Flask, redirect, render_template, send_file, request, send_from_directory
import speech_recognition as sr
import webbrowser as wb
app = Flask(__name__)
url = ""
app.config["CLIENT_IMAGES"] = "/"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        website = request.form.get("website")
        if website == "google":
            url = "https://www.google.com/search?q="
        elif website == "bing":
            url = "https://www.bing.com/search?q="
        elif website == "youtube":
            url = "https://www.youtube.com/results?search_query="
        elif website == "wikipedia":
            url = "https://en.wikipedia.org/wiki/"
        elif website == "reddit":
            url = "https://www.reddit.com/search/?q="
        elif website == "quora":
            url = "https://www.quora.com/search?q="
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Sphinx
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            get = r.recognize_google(audio)
            wb.get().open_new_tab(url+get)
            return render_template("index.html")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return render_template("404.html")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return render_template("404.html")


    