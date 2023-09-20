from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

hello_name = ''


@app.route('/', methods=['GET', 'POST'])
def form():
    global hello_name
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        if request.cookies.get(name) == mail:
            hello_name = name
            return redirect(url_for('hello'))
        response = make_response(render_template('form.html'))
        response.set_cookie(name, mail)
        return response
    return render_template('form.html')


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    global hello_name
    if hello_name == '':
        return redirect(url_for('form'))
    if request.method == 'POST':
        response = make_response(render_template('hello.html'))
        response.delete_cookie(hello_name)
        hello_name = ''
        return response
    return render_template('hello.html', name=hello_name)


if __name__ == '__main__':
    app.run(debug=True)