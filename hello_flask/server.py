from flask import Flask  
app = Flask(__name__)    

@app.route('/')        
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')         
def goodbye_world():
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

