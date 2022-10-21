from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Привет AND"


if __name__=="__main__":
    app.run(debug=True)