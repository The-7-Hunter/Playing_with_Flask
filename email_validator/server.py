from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
app = Flask(__name__)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/")
def index():
    mysql = connectToMySQL('valid_emails')
    emails = mysql.query_db('SELECT * FROM valid_emails;')

    return render_template("index.html", all_emails=emails)


@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
    	flash("Please enter a email")

    # no flash messages means all validations passed
    if not '_flashes' in session.keys():
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid email address!")
            return redirect("/")
        mysql = connectToMySQL("valid_emails")
        query = "INSERT INTO valid_emails (email) VALUES (%(email)s)"
        data = {
            "email": request.form["email"],
        }
        new_email = mysql.query_db(query, data)
        flash("%s successfully added!" %(request.form["email"]))
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)