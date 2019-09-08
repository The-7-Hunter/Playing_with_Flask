from flask import Flask, render_template, request, redirect  # added request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("form.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    language_from_form = request.form['language']
    comment_from_form = request.form['']
    return render_template("response.html", name_on_template=name_from_form, email_on_template=email_from_form, language_on_template=language_from_form)


if __name__ == "__main__":
    app.run(debug=True)
