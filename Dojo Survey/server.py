from flask import Flask , render_template, redirect, request, session
app = Flask(__name__)    
app.secret_key = "Wow"





@app.route('/')        
def index():
    return render_template("index.html")


@app.route('/survey', methods=['POST'])
def submit_form():

    print("Got Survey")

    print(request.form)
    print(request.form['name'])
    print(request.form['location'])
    print(request.form['language'])
    print(request.form['comments'])

    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]

    session["name"] = name
    session["location"]= location
    session["language"]= language
    session["comments"]= comments

    return redirect('/thanks')


@app.route('/thanks')
def thanks():
    print("Here is what you submitted")
    print(request.form)
    print(session)
    return render_template("show.html")



@app.route('/<other>')
def sorry(other):
    return f"Sorry! {other} not available! No response. Try Again"


if __name__ == "__main__":
    app.run(debug=True)