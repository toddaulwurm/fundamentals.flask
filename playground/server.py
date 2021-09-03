from flask import Flask , render_template 
app = Flask(__name__)    

@app.route('/')        
def index():
    return render_template("index.html", blocks=0)

@app.route('/play')         
def play():
    return render_template("index.html", blocks=3)

@app.route('/play/<int:blocks>')         
def playcustom(blocks):
    return render_template("index.html", blocks=blocks)

@app.route('/play/<int:blocks>/<string:color>')         
def color(color):
    return render_template("index.html", blocks="color")

@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"


if __name__ == "__main__":
    app.run(debug=True)