'''
Script for controlling audio playback volume over time
'''

import sys
import spotipy
import spotipy.util as util
import argparse
import datetime
import time
from pathlib import Path

def init_client(username):
    scopes = ['user-modify-playback-state', 'user-read-playback-state']

    token = util.prompt_for_user_token(username, scopes, client_id='3cc0709f8bc54bc99b23b027e793dcae', client_secret='02caf253fc4c4b65b341338300220085', redirect_uri='http://localhost:8080')
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

class Settings:
    def __init__(self):
        self.username = None
        self.start_volume = None
        self.ramp_time = None
        self.end_time = None
        self.max_volume = None
    
    def parse_from_file(self, file):
        for ln in file.open().readlines():
            split_ln = ln.rstrip().split(':')
            field_name = '_'.join([word.lower() for word in split_ln[0].split(' ')])
            self.__dict__[field_name] = split_ln[1][1:]
        return self
    
    def save_to_file(self, fil):
        with fil.open('w') as settings_fil:
            for field in self.__dict__.keys():
                field_formatted = ' '.join([word.title() for word in field.split('_')])
                settings_fil.write(f'{field_formatted}: {self.__dict__[field]}\n')

def volume_loop_inner(curve):

    time.sleep(60)

def volume_loop(curve):
    while curve.should_run():
        volume_loop_inner(curve)

def tune_volume():
    done_tuning = False
    while not done_tuning:
        pass

def setup_install():
    
    pass


def load_settings():
    settings_file = Path.cwd() / 'settings.txt'
    if settings_file.exists():
        return Settings().parse_from_file(settings_file)
    return setup_install()

def main(args):
    settings = load_settings()
    settings.save_to_file(Path.cwd() / 'settings.txt')

    spotify = init_client(args.username)

    curve = VolumeCurve(args)

    volume_loop(curve)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # if no args are passed
    # check if there is a config saved
    # if not, prompt for setup
    # if there is, run with that config

    parser.add_argument('--username', type=str, help='time in minutes between updates')
    parser.add_argument('--read-volume-mode', type=str, help='just reads the user\'s current spotify volume and exits. useful so you know your volume to change settings.')

    args = parser.parse_args()

    main(args)
