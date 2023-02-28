from flask import Flask

app = Flask(__name__)


@app.route('/')

def mission():
    return '<h1>Миссия Колонизация Марса</h1>'

@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'

@app.route('/promotion')
def promotion():
    return '''<h1>Человечество вырастает из детства.</h1>
            <h1>Человечеству мала одна планета.</h1>
            <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
            <h1>И начнем с Марса!</h1>
            <h1>Присоединяйся!</h1>'''

@app.route('/image_mars')
def image_mars():
    return '''<img src="/static/data/image_mars.png" alt="здесь должна была быть картинка, но не нашлась">'''

def login():


app.run(port=8080)
