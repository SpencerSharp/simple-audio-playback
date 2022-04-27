from __future__ import print_function
import sys
import spotipy
import spotipy.util as util

scope = 'user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id='3cc0709f8bc54bc99b23b027e793dcae', client_secret='02caf253fc4c4b65b341338300220085', redirect_uri='http://localhost:8080')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.volume(100)
else:
    print("Can't get token for", username)