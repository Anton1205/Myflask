from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/audi')
def audi():
    return render_template('audi.html')


@app.route('/vw')
def vw():
    return render_template('vw.html')


@app.route('/porsche')
def porsche():
    return render_template('porsche.html')


@app.route('/adds')
def adds():
    return render_template('adds.html')


if __name__ == '__main__':
    app.run(debug=True)