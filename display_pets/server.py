from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route('/create_pet', methods=["POST"])
def add_pet():
    mysql = connectToMySQL("pets")
    query = "INSERT INTO pets (name, type, uploaded_at) VALUES (%(name)s, %(type)s, NOW())"
    data = {
        "name": request.form["name"],
        "type": request.form["type"],
    }
    new_pet = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
