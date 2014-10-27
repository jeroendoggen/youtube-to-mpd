# YouTube to MPD

Frontend for youtube-dl to auto add youtube music to mpd

Features:
 * Download music from youtube videos
 * Download music from youtube playlists
 * Add them to mpd to allow easy playback

Upcoming features:
 * Create folders/mpd playlists for every youtube playlist
 
## Install:
 * will soon be available: (for now install from source "sudo setup.py install")
 * Install using pip: ``pip install youtube_to_mpd. (Linux & Windows)
 * Python Package available in the Python Package Index at: http://pypi.python.org/pypi/youtube_to_mpd/
 
## Usage:
 * Download a single song and add to MPD: "python -m youtube_to_mpd -s SONGID" (for example: DgQR0x5ljek)
 * Download a playlist and add to MPD: "python -m youtube_to_mpd -p PLAYLISTID" (for example: FLoLRVbYOEns6PTJtWo0Y_7g)

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