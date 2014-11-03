YouTube to MPD
==============

Front end for youtube-dl to auto add YouTube music to Music Player Daemon (MPD).

 - Download music from YouTube videos
 - Download music from YouTube playlists
 - Add them to Music Player Daemon to allow easy playback

Usage:
------
 - Download a single song and add to MPD::

    python -m youtube_to_mpd -s SONGID

 - Download a playlist and add to MPD::

    python -m youtube_to_mpd -p PLAYLISTID

Dependencies:
-------------
 - youtube-dl_
 - MPD_

Limitations:
------------
 - Only tested on Debian
 - 'settings.conf' file needs to be in your path
 
.. _youtube-dl: https://github.com/rg3/youtube-dl
.. _MPD: http://www.musicpd.org