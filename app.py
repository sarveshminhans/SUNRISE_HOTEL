from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# DO NOT REMOVE THIS
if __name__ == "__main__":
    app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


