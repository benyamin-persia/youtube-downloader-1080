# pip install ffmpeg-python

from pytube import *
import os
import ffmpeg

yt = YouTube(input('enter youtube link : '))
# for i in yt.streams.all():
#     print(i)
video = yt.streams.filter(res="720p").first().download()
v_name = video.title()+'.mp4'
os.rename(video, v_name)

audio = yt.streams.filter(only_audio=True).first().download()
a_name = video.title()+".mp3"
os.rename(audio, a_name)

input_video = ffmpeg.input(v_name)

input_audio = ffmpeg.input(a_name)

ffmpeg.concat(input_video, input_audio, v=1, a=1).output(v_name.replace(".Mp4","")).run()