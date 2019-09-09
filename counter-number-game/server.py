from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('counter.html', count=session['count'])


@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    # We only increment by 1 since reloading the page also increments
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')


@app.route('/game')
def index_for_game():
    if 'message' not in session:
        session["message"] = ""
    if 'number' not in session:
        session['number'] = random.randrange(1, 101)
    return render_template("game.html", message=session['message'])


@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['number'])
    if guess == session['number']:
        session['message'] = "you win!"
    if guess > session['number']:
        session['message'] = 'Too high guess lower'
    elif guess < session['number']:
        session['message'] = 'Too low guess higer'
    return redirect('/game')


@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/game')


app.run(debug=True)