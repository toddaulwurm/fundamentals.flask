from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def playground(num):
    return render_template(num)

@app.route('/<other>')
def sorry():
    return f"Sorry! No response. Try Again"