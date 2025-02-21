from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Website</h1><p><a href='/resume'>View My Resume</a></p><p><a href='/about'>About Me</a></p>"

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


