from flask import Flask, render_template, request, redirect, url_for, session
from kural import prep, findKural

app = Flask(__name__)
app.secret_key = "27eduCBA09"

@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "POST":
        texts = prep()
        userInput = request.form.get('uinp')
        kurals = findKural(userInput, texts)
        session['kurals'] = kurals
        session['title'] = userInput
        return redirect(url_for('kural'))
    return render_template("index.html")

@app.route("/kural", methods=["GET"])
def kural():
    kurals = session.get('kurals')
    title = session.get('title')
    return render_template("main.html",kurals=kurals, title=title)