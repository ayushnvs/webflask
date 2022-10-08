from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/product/resume')
def resume():
    return render_template('product/resume/index.html')


@app.route('/product/reweb')
def reweb():
    return render_template('product/reweb/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
