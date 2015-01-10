from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
    return template('<b>Index</b>!')

if __name__ == '__main__':
    run(host='public IP', port=80)
