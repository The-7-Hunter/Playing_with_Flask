from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/azozletstest'
db = SQLAlchemy(app)

class Account(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable = False, unique = True)
    age = db.Column(db.String(45), nullable = False)
#     # created_at = db.Column(default=datetime.datetime.now())
#     # updated_at = db.Column(default=datetime.datetime.now())
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<Account %r>' % self.name

@app.route('/')                           
def index():
    # pet = Pets('Boboy', 'Dog')
    # db.session.add(pet)
    # db.session.commit()
    friends = Account.query.all()    
    return render_template('index.html', all_friends = friends)

# @app.route('/add_pet', methods=["POST"])
# def add_pet():
#     pet = Pets(request.form['name'], request.form['type'])
#     db.session.add(pet)
#     db.session.commit()
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True)