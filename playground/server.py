from flask import Flask , render_template 
app = Flask(__name__)    

@app.route('/')        
def index():
    return render_template("index.html")

@app.route('/play/<int:blocks>')         
def blocks(blocks):
    return '${blocks}'


@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"