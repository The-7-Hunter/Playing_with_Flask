from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('eight_by_eight.html')

@app.route('/4')
def render4rows():
    return render_template('eight_by_eight.html')


if __name__ == "__main__":
    app.run(debug=True)