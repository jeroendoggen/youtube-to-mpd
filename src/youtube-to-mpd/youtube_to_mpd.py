"""
    YouTube to MPD
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os

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
        pass

    def print_start_info(self):
        print("Starting Youtube To MPD")
        print(" - Music folder: " + self.settings.music_folder)
        print(" - YouTube folder: " + self.settings.youtube_foldername)
        print(" - Create per-playlist folder: " + self.settings.create_subfolders)
        print(" - Create MPD playlist: " + self.settings.create_playlists)

    def print_end_info(self):
        print("Processing finished")
        print(" - Files downloaded: " + str(self.download_counter))
        print(" - Files converted: " + str(self.download_counter - self.errors))
        print(" - Time elapsed: " + str(self.time_passed))

    def exit_value(self):
        #"""TODO: Generate the exit value for the application."""
        if (self.errors == 0):
            return 0
        else:
            return 42
