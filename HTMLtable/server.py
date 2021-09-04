from flask import Flask , render_template 
app = Flask(__name__)    





@app.route('/')        
def index():
    return render_template("index.html")



@app.route('/table')
def table():
    users = [
        {'first' : 'Michael', 'last' : 'Choi'},
        {'first' : 'John', 'last' : 'Supsupin'},
        {'first' : 'Mark', 'last' : 'Guillen'},
        {'first' : 'KB', 'last' : 'Tonel'}
    ]
    return render_template("index.html", list=users)










@app.route('/<other>')
def sorry(other):
    return f"Sorry! ${other} not available! No response. Try Again"


if __name__ == "__main__":
    app.run(debug=True)