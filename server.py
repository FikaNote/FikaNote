from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
    return template('<b>Index</b>!')

run(host='fikanote.herokuapp.com', port=80)
