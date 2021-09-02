from flask import Flask, render_template 
app = Flask(__name__)    

@app.route('/')        
def index():
    return render_template("new.html", num=5)

@app.route('/<int:num>')        
def playground():
    return render_template("new.html", int)

@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"



if __name__=="__main__":   
    app.run(debug=True)   
