# python -m youtube_dl -f bestaudio --extract-audio --audio-format wav --audio-quality 0 --yes-playlist 'https://www.youtube.com/watch?v=gXHtoHW9JMo&list=PL5yc3mTudpLz9zYk80EDnT8aw8a9hXzx_'
# use ^ to download entire playlist
# but for now only experimenting with few videos
import speech_recognitioin as sr
from os import path

for filename in os.listdir(direct1ory):
    if filename.endswith(".wav"):
         # print(os.path.join(directory, filename))