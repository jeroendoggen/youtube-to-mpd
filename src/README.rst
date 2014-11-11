YouTube to MPD
==============
Front end for youtube-dl to auto add YouTube music to Music Player Daemon (MPD).
 - Download music from YouTube videos
 - Download music from YouTube playlists
 - Add them to Music Player Daemon to allow easy playback

Usage:
------
Download a single song and add to MPD::
 - *python -m youtube_to_mpd -s SONGID*
Download a playlist and add to MPD::
 - *python -m youtube_to_mpd -p LISTID*

Easy usage:
-----------
Configure:
 - Add the following to your ".bashrc": alias playlist:'python -m youtube_to_mpd -p'
 - Add the following to your ".bashrc": alias song:'python -m youtube_to_mpd -s'
 - Start a new console session
Then run:
 - *song SONGID* (for example: *song mIBTg7q9oNc*"
 - *playlist LISTID* (for example: *playlist RDmIBTg7q9oNc*"

Dependencies:
-------------
 - youtube-dl_
 - MPD_

Limitations:
------------
 - Developed and tested on Debian Wheezy
 - Make sure you put the "settings.conf" file in your current path (issue #5)
 
.. _youtube-dl: https://github.com/rg3/youtube-dl
.. _MPD: http://www.musicpd.org