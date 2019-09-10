from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("form.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    if len(request.form['name']) < 1:
        flash("Please enter a name")
    if len(request.form['email']) < 1:
        flash("Please enter a vaild email")

    # no flash messages means all validations passed
    if not '_flashes' in session.keys():
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['language'] = request.form['language']
        return redirect('/show')
    return redirect("/")


@app.route('/show')
def show_user():
    return render_template("response.html")


if __name__ == "__main__":
    app.run(debug=True)
