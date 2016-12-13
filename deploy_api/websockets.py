from flask.ext.socketio import emit
from flask.ext.socketio import join_room, leave_room

from . import socketio
from .views import broadcast_vote_count

@socketio.on('connect', namespace='/deploy_api')
def ws_connect():
    pass

@socketio.on('disconnect', namespace='/deploy_api')
def ws_disconnect():
    pass


@socketio.on('join', namespace='/deploy_api')
def on_join(data):
    vote = data['vote']
    join_room(vote)
    broadcast_vote_count(vote)

