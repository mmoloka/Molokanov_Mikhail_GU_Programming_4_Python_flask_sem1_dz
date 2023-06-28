from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base/')
def base():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртка'}
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run()
