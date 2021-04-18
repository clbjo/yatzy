from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercrutkee'
socketio = SocketIO(app)


#-------------------- Web Pages --------------------#


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


#-------------------- SocketIO --------------------#


@socketio.on('my event')
def handle_message(data):
    print('received message: ' + str(data))


#-------------------- Startup --------------------#


if __name__ == '__main__':
    socketio.run(app, debug=True)

