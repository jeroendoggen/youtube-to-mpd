#!/usr/bin/env bash
#
# Small script to create & install a Debian package

echo "Starting package build process"

python setup.py --command-packages=stdeb.command sdist_dsc

cd deb_dist/youtube-to-mpd-0.0.1/

dpkg-buildpackage -rfakeroot -uc -us

cd ..

sudo dpkg -i python-youtube-to-mpd_0.0.1-1_all.deb

