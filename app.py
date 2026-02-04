from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="templates")

# 🔥 Explicit static route (THIS FIXES IT)
@app.route("/static/<path:filename>")
def static(filename):
    return send_from_directory("static", filename)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
