from flask import Flask , render_template 
app = Flask(__name__)    

@app.route('/')        
def index():
    return render_template("index.html", y=8, x=8)

@app.route('/<int:y>')         
def y(y):
    return render_template("index.html", y=y, x=8)

@app.route('/<int:y>/<int:x>')         
def yandx (y, x):
    return render_template("index.html", y=y, x=x)


@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"


if __name__ == "__main__":
    app.run(debug=True)