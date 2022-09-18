from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pages/resume')
def pages():
    return render_template('pages/resume/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
