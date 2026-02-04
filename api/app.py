from flask import Flask, render_template

# Point Flask to the correct folders relative to this file
app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Keep this for local testing
if __name__ == "__main__":
    app.run()
    
