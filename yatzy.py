from urllib.parse import urlparse


from flask import Flask, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercrutkee'
socketio = SocketIO(app)


#-------------------- Game Logic --------------------#


from random import randint


def roll():
    values = [randint(1,6) if not keep else x for x, keep in zip(values, kept)]
    state.throwCounter += 1


#-------------------- Web Pages --------------------#


IMAGE_FOLDER = 'images'


# The keys are the socketio room names
states = {'asdf': {'values': [1,1,1,1,2]}}


@app.route('/')
@app.route('/index')
def index():
    #TODO flytta favicon till index.html
    return render_template('index.html')


@app.route('/play/<room>')
def play(room):
    image_data = []
    for i, value in enumerate(states[room]['values']):
        image_data.append({
            'index': i,
            'filename': f'{IMAGE_FOLDER}/{value}.png'
        })
    return render_template('play.html', image_data=image_data)


#-------------------- SocketIO --------------------#


#Emittable events
UPDATE = 'update'


@socketio.event
def greeting(room):
    print(room)


@socketio.event
def action(act):
    print(act)
    if act == 'roll':
        pass
        #roll()
    socketio.emit(UPDATE, states['asdf'])


#-------------------- Startup --------------------#


if __name__ == '__main__':
    socketio.run(app, debug=True)

