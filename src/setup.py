"""Setup file for YouTube to MPD

Define the options for the "youtube-to-mpd" package
Create source Python packages (python setup.py sdist)
Create binary Python packages (python setup.py bdist)

"""
from distutils.core import setup

from youtube-to-mpd import __version__


with open('README.txt') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(name='youtube-to-mpd',
      version=__version__,
      description='YouTube to MPD',
      long_description=LONG_DESCRIPTION,
      author='Jeroen Doggen',
      author_email='jeroendoggen@gmail.com',
      url='https://github.com/jeroendoggen/youtube-to-mpd',
      packages=['youtube-to-mpd'],
      package_data={'youtube-to-mpd': ['*.py', '*.conf']},
      license='MIT',
      platforms=['Linux'],
      )
