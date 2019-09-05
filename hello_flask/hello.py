from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', phrase="Hey there", times=5)


@app.route('/play')
def display_three_boxes():
    return render_template('three_boxes.html')

@app.route('/play/<count>')
def display_num_boxes(count):
    return render_template('num_of_boxes.html',count = int(count))

@app.route('/play/<count>/<color>')
def display_colored_boxes(count, color):
    return render_template('colored_boxes.html', count = int(count), color = color)
    
if __name__ == "__main__":
    app.run(debug=True)
