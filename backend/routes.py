from yatzy import app
print(app)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

