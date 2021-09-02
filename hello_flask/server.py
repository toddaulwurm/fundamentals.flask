from flask import Flask , render_template 
app = Flask(__name__)    

@app.route('/')        
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')         
def dojo():
    return 'Dojo!'

@app.route('/say/<string:word>')
def say(word):
    return f'Hi {word.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    word = word + " "
    return f"{word*num} " + " "

@app.route('/<other>')
def sorry(other):
    return f"Sorry! No response. Try Again"










if __name__=="__main__":   
    app.run(debug=True)   

