from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def initial_render():
    return "Hey there!  Head to localhost:5000/play to go to the Playground!"


@app.route("/play")
def play():
    return render_template("index.html", repeat=3, colorChange="aqua")


@app.route("/play/<int:num_boxes>")
def num(num_boxes):
    repeat = num_boxes
    return render_template("index.html", repeat=repeat, colorChange="aqua")


@app.route("/play/<int:num_boxes>/<color_change>")
def box_color(num_boxes, color_change):
    repeat = num_boxes
    colorChange = color_change
    return render_template("index.html", repeat=repeat, colorChange=colorChange)


if __name__ == "__main__":
    app.run(debug=True)
