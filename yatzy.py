from urllib.parse import urlparse

from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room


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
states = {'asdf': {
    'values': [1,1,1,1,2],
    'counter': 0,
    'kept': [False, False, False, False, False] 
}}


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


# All sids are stored along with the room they belong to.
rooms = {}


# Emittable events
UPDATE = 'update'


@socketio.event
def join(url):
    '''
    url: The url from which the client made the connection contains the room for the socket.
    '''
    room = urlparse(url).path.split('/')[-1]
    join_room(room)
    rooms[request.sid] = room


@socketio.event
def action(act):
    print(act)
    if act == 'roll':
        pass
        #roll()
    socketio.emit(UPDATE, states['asdf'], room=rooms[request.sid])


#-------------------- Startup --------------------#


if __name__ == '__main__':
    socketio.run(app, debug=True)

