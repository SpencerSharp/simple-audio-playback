'''
Script for controlling audio playback volume over time
'''

import sys
import spotipy
import spotipy.util as util
import argparse
import datetime
import time

def init_client():
    scope = 'user-modify-playback-state'

    token = util.prompt_for_user_token(username, scope, client_id='3cc0709f8bc54bc99b23b027e793dcae', client_secret='02caf253fc4c4b65b341338300220085', redirect_uri='http://localhost:8080')
    sp = None
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        raise
    
    return sp

class VolumeCurve:
    def __init__(self, args):
        self.start_time = datetime.datetime.now()
        self.start_scaleup = None
        self.end_scaleup = None
        self.end_time = None
        self.start_volume = None
        self.max_volume = None
    
    def get_volume_for_time():
        percent_into_duration = 0
    
    def should_run(self):
        return True

def volume_loop_inner(curve):

    time.sleep(60)

def volume_loop(curve):
    while curve.should_run():
        volume_loop_inner(curve)

def tune_volume():
    done_tuning = False
    while not done_tuning:


def setup_install():




def main(args):
    spotify = init_client()

    curve = VolumeCurve(args)

    volume_loop(curve)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # if no args are passed
    # check if there is a config saved
    # if not, prompt for setup
    # if there is, run with that config

    parser.add_argument('--username', type=str, help='time in minutes between updates')
    parser.add_argument('--duration', type=str, help='time in minutes between updates')
    parser.add_argument('--run-until', type=str, help='time in minutes between updates')
    parser.add_argument('--config', type=str, help='path to config file')
    parser.add_argument('--save-config', type=bool, help='if the config used to run this script should be saved locally.')
    parser.add_argument('--edit-config', type=bool, help='edit your config.')
    parser.add_argument('--test-mode', type=str, help='run in test mode. just sets the volume to whatever you pass in for "start-volume" and exits.')
    parser.add_argument('--start-volume', type=str, help='run in test mode. just sets the volume to whatever you pass in and exits.')

    args = parser.parse_args()

    main(args)
