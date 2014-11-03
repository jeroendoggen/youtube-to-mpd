"""
    YouTube to MPD
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


import ConfigParser
import argparse
import sys

class Actions:
    create_subfolders = False
    create_playlists = False


class Settings:
    """ Contains all the tools to analyse Blackboard assignments """
    config_file = "settings.conf"
    Config = ConfigParser.ConfigParser()
    playlist = None
    song = None
    music_folder = None
    youtube_foldername = None

    parser = argparse.ArgumentParser(
        prog="youtube_to_mpd",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="YouTube to MPD commandline arguments:",
        epilog="Report bugs to jeroendoggen@gmail.com.")

    def __init__(self):
        self.read_config_file(self.config_file)
        self.cli_arguments()

    def config_section_map(self, section):
        """ Helper function to read config settings """
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
                sys.exit(1)
        return dict1

    def read_config_file(self, filename):
        """ Read the config  """
        try:
            self.Config.read(filename)
            self.music_folder = str(self.config_section_map("Config")['music_folder'])
            self.youtube_foldername = str(self.config_section_map("Config")['youtube_foldername'])
            self.create_subfolders = self.Config.getboolean('Config', 'create_subfolders')
            self.create_playlists = self.Config.getboolean('Config', 'create_playlists')

        except AttributeError:
            #TODO: this does not work!! (AttributeError or KeyError needed? both?)
            print("Error while processing config file")
            sys.exit(1)

    def cli_arguments(self):
        """Configure a read all the cli arguments."""
        self.configure_cli_arguments()
        self.get_cli_arguments()

    def configure_cli_arguments(self):
        """Configure all the cli arguments."""
        self.parser.add_argument("-f", metavar="music_folder",
          help="Folder where the music will be saved")
        self.parser.add_argument("-p", metavar="playlist",
          help="Playlist ID (without the http://youtube.com/... part)")
        self.parser.add_argument("-s", metavar="song",
          help="Song ID (without the http://youtube.com/... part)")

        self.parser.add_argument('--create_subfolders', action='store_true', help='Start the virtual machines')
        self.parser.add_argument('--create_playlists', action='store_true', help='Stop the virtual machines')

    def get_cli_arguments(self):
        """Read all the cli arguments."""
        args = self.parser.parse_args()
        if (args.f is not None):
            self.music_folder = args.f
        if (args.p is not None):
            self.playlist = args.p
        if (args.s is not None):
            self.song = args.s

        if (args.create_subfolders is True):
            self.actions.create_subfolders = True
        if (args.create_playlists is True):
            self.actions.create_playlists = True

