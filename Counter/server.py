from flask import Flask , render_template, redirect, request, session
app = Flask(__name__)
app.secret_key= "wefg"    



@app.route('/')        
def index():
    visits=0
    return render_template("index.html")

@app.route('/calc', methods=['POST'])
def calculate():
    visits = request.form["visits"]
    session["visits"] = visits
    visits += 1
    return redirect('/')


@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"


if __name__ == "__main__":
    app.run(debug=True)