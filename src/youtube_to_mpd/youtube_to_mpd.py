"""
    YouTube to MPD
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os
import subprocess

from settings import Settings


class YoutubeToMPD:
    """ Contains all the tools to convert youtube content to MPD content"""
    time_passed = 0
    errors = 0
    download_counter = 0

    def __init__(self):
        self.settings = Settings()
        #self.setup = Setup(self.settings, self.logger)
        self.errors = 0

    def run(self):
        """ Run the program (call this from main) """
        self.print_start_info()
        self.convert()
        self.print_end_info()

    def convert(self):
        self.go_to_folder()
        self.download()

    def go_to_folder(self):
        if "~/" in self.settings.music_folder:
            self.settings.music_folder = self.settings.music_folder[2:]
        path = os.path.join(os.environ['HOME'], self.settings.music_folder)
        print(path)
        if (os.path.isdir(path)):
            os.chdir(path)
            path = os.path.join(path, self.settings.youtube_foldername)
            if (os.path.isdir(path)):
                os.chdir(self.settings.youtube_foldername)
                print(os.getcwd())
            else:
                print("Error opening YouTube folder")
                exit(0)
                #TODO create this folder when needed?
        else:
            print("Error opening music folder")
            exit(0)

    def download(self):
        if(self.settings.playlist) is not None:
            print("Starting playlist download")
            self.print_playlist_info()
            if (self.settings.create_subfolders is True):
                os.system("youtube-dl -q -ci --extract-audio -o '%(playlist)s/%(title)s.%(ext)s' --audio-format mp3  --audio-quality 0 http://www.youtube.com/playlist?list=" + self.settings.playlist)
            if (self.settings.create_subfolders is False):
                os.system("youtube-dl -q -ci --extract-audio -o '%(title)s.%(ext)s' --audio-format mp3  --audio-quality 0 http://www.youtube.com/playlist?list=" + self.settings.playlist)
        if(self.settings.song) is not None:
            print("Starting song download")
            self.print_song_info()
            os.system("youtube-dl -q -ci --extract-audio -o '%(title)s.%(ext)s' --audio-format mp3  --audio-quality 0 https://www.youtube.com/watch?v=" + self.settings.song)

    def print_song_info(self):
        subprocess.Popen("youtube-dl -e https://www.youtube.com/watch?v=" + self.settings.song, shell=True)

    def print_playlist_info(self):
        subprocess.Popen("youtube-dl -e http://www.youtube.com/playlist?list=" + self.settings.playlist, shell=True)

    def print_start_info(self):
        print("Starting Youtube To MPD")
        print(" - Music folder: " + self.settings.music_folder)
        print(" - YouTube folder: " + self.settings.youtube_foldername)
        print(" - Create per-playlist folder: " + str(self.settings.create_subfolders))
        #print(" - Create MPD playlist: " + str(self.settings.create_playlists))

    def print_end_info(self):
        print("Processing finished")
        #print(" - Files downloaded: " + str(self.download_counter))
        #print(" - Files converted: " + str(self.download_counter - self.errors))
        #print(" - Time elapsed: " + str(self.time_passed))

    def exit_value(self):
        #"""TODO: Generate the exit value for the application."""
        if (self.errors == 0):
            return 0
        else:
            return 42
