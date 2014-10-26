"""
    YouTube to MPD
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""

import sys
import signal

from youtube_to_mpd import YoutubeToMPD


def run():
    """Run the main program"""
    signal.signal(signal.SIGINT, signal_handler)
    converter = YoutubeToMPD()
    converter.run()
    return(converter.exit_value())

def signal_handler(signal, frame):
        sys.exit(0)

if __name__ == "__main__":
    sys.exit(run())
