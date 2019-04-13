import subprocess

def extractAudio(videofile,audiofile):
    command = "ffmpeg -i "+videofile+" -ab 160k -ac 1 -ar 16000 -vn "+audiofile
    subprocess.call(command, shell=True)



#VideoFile="/Users/indumanimaran/Documents/Hackathon/HackSC/GCP/video_file.mp4"
#AudioFile="audioFile.wav"

#extractAudio(VideoFile,AudioFile)