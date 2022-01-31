import imp
from flask import Flask, render_template, request, redirect, session
import random
from jinja2 import Undefined  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Wow"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def ninja_gold():
    if session.get('history') is None:
        session['history'] = []
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/process_money', methods=['POST'])
def process_money():
    print ("Got Survey!")
    print(request.form['venue'])
    player_choice = request.form['venue']
    if player_choice == 'farm':
        payout = random.randint(10,20)
        session['gold'] += payout
        session['latest'] = f'{player_choice} payed out {payout}'
        session['history'].insert(0, session['latest'])
    elif player_choice == 'cave':
        payout = random.randint(5,10)
        session['gold'] += payout
        session['latest'] = f'{player_choice} payed out {payout}'
        session['history'].insert(0, session['latest'])
    elif player_choice == 'house':
        payout = random.randint(2,5)
        session['gold'] += payout
        session['latest'] = f'{player_choice} payed out {payout}'
        session['history'].insert(0, session['latest'])
    elif player_choice == 'casino':
        payout = random.randint(-50,50)
        session['gold'] += payout
        session['latest'] = f'{player_choice} payed out {payout}'
        session['history'].insert(0, session['latest'])
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.