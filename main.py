'''
Created and Edited by: Ryan Farmer, President of Ryan Productions
Date & Time Published: 11/30/2021 @ 08:02 AM (EST)
Project Name: Homestead

Products Page - Python File

Oogabooga -Diego Nosko
'''

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/feedback")
def games():
    return render_template("feedback.html")

@app.route("/products")
def escape():
    return render_template("production.html")


if __name__ == "__main__":
    app.run(debug=True)