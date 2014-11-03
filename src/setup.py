"""Setup file for YouTube to MPD

Define the options for the "youtube_to_mpd" package
Create source Python packages (python setup.py sdist)
Create binary Python packages (python setup.py bdist)

"""
from distutils.core import setup

from youtube_to_mpd import __version__


with open('README.rst') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(name='youtube_to_mpd',
      version=__version__,
      description='YouTube to MPD',
      long_description=LONG_DESCRIPTION,
      author='Jeroen Doggen',
      author_email='jeroendoggen@gmail.com',
      url='https://github.com/jeroendoggen/youtube_to_mpd',
      packages=['youtube_to_mpd'],
      package_data={'youtube_to_mpd': ['*.py', '*.conf']},
      license='GPLv3',
      platforms=['Linux'],
      )
