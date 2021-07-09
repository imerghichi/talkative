from flask import Flask, render_template, request, redirect
import pyttsx3
from talkative.app.textForm import TextForm
import os

app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def hello_world():
    form = TextForm()
    return render_template("hello.html", form = form)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['textTospeech']
    friend = pyttsx3.init()
    friend.say(text)
    friend.runAndWait()
    friend.startLoop(False)
    return redirect('/')
