from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "some secret keyyyyy"



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")

    print(request.form)

    print(request.form["name"])
    print(request.form["email"])

    name = request.form["name"]
    email = request.form["email"]

    session['username'] = name
    session['username'] = email

    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    
    return redirect('/show')

@app.route("/show")
def show_user():

    print("Showing the User Info From the Form")

    print(request.form)

    print(session)

    return render_template("show.html")

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")













if __name__ == "__main__":
    app.run(debug=True)

