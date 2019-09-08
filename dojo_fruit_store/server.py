from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print("Hello s" + request.form['first_name'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']

    return render_template("checkout.html", firstname_on_form = first_name, lastname_on_form = last_name, student_id_form = student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    