
# coding: utf-8

# In[6]:


import sys
from moviepy.editor import *


# In[9]:


def extractAudio(videofile,audiofile):
    video = VideoFileClip(videofile)
    audio = video.audio
    audio.write_audiofile(audiofile)


# In[10]:



#VideoFile="/Users/indumanimaran/Documents/Hackathon/HackSC/GCP/video_file.mp4"
#AudioFile="audioFile.mp3"

#extractAudio(VideoFile,AudioFile)

