# YouTube to MPD

Front end for youtube-dl to auto add YouTube music to Music Player Daemon (MPD).

Features:
 * Download music from YouTube videos
 * Download music from YouTube playlists
 * Add them to mpd to allow easy playback

Upcoming features:
 * Create folders/mpd playlists for every YouTube playlist

## Install from the Python Package Index:
 * ``pip install youtube_to_mpd``. (Linux & Windows)
 * Package can be found here: http://pypi.python.org/pypi/youtube_to_mpd/

## Install from source:
 * run ``setup.py install`` (with root privileges)

## Usage:
 * Download a single song and add to MPD: ``python -m youtube_to_mpd -s SONGID`` (for example: DgQR0x5ljek)
 * Download a playlist and add to MPD: ``python -m youtube_to_mpd -p PLAYLISTID`` (for example: FLoLRVbYOEns6PTJtWo0Y_7g)

## Easy usage:
Configure:
 * Add the following to your ".bashrc": alias playlist:'python -m youtube_to_mpd -p'
 * Add the following to your ".bashrc": alias song:'python -m youtube_to_mpd -s'
 * Start a new console session

Then run:
 * ``song SONGID`` (for example: *song mIBTg7q9oNc*"
 * ``playlist LISTID`` (for example: *playlist RDmIBTg7q9oNc*"
 
## Limitations:
 * Currently under active development (early Alpha!)
 * Not feature complete at all!

## Dependencies:
 * youtube-dl: https://github.com/rg3/youtube-dl
 * Music Player Daemon: http://www.musicpd.org

## License:
If not stated otherwise "YouTube to MPD" is distributed in terms of the GPL software license.
See COPYING file in the distribution for details.

## Bug reports:
 * Jeroen Doggen <jeroendoggen@gmail.com>
 * Post issues to GitHub https://github.com/jeroendoggen/youtube-to-mpd/issues.