from flask import Flask, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercrutkee'
socketio = SocketIO(app)


#-------------------- Web Pages --------------------#


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


#-------------------- Game Logic --------------------#


from random import randint


def roll():
    values = [randint(1,6) if not keep else x for x, keep in zip(values, kept)]
    state.throwCounter += 1


#-------------------- SocketIO --------------------#


@socketio.event
def greeting():
    '''Emits the current state to a new client'''
    socketio.emit('update', {'values': [1,2,3,4,5]}, to=request.sid)


@socketio.event
def action(act):
    print(act)
    if act == 'roll':
        pass
        #roll()
    socketio.emit('update', {'dud': True})


#-------------------- Startup --------------------#


if __name__ == '__main__':
    socketio.run(app, debug=True)

