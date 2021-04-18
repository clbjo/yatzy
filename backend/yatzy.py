from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercrutkee'
socketio = SocketIO(app)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    socketio.run(app, debug=True)

