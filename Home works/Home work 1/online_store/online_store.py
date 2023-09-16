from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.get('/suit/')
def suit():
    return render_template('suit.html')


@app.get('/t-shirts/')
def t_shirts():
    return render_template('t-shirts.html')


if __name__ == '__main__':
    app.run()