from flask import Flask , render_template, redirect, session
app = Flask(__name__)
app.secret_key= "wefg"    


@app.route('/')
def index():
    if "sum" not in session:
        session["sum"] = 1
    else:
        session['sum'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()     #got this from the internet, but otherwise wouldn't have used a built in method.
    return redirect('/')

@app.route('/<other>')
def sorry(other):
    return f"Sorry! {other} not available! No response. Try Again"

if __name__ == "__main__":
    app.run(debug=True)