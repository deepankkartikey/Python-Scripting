"""
    This script downloads youtube video using the link provided by user in argument
"""
from pytube import YouTube
from sys import argv
import os

# 0th argument is always program name
# 1st argument is first command line parameter
videoLink = argv[1]

try:
    yt = YouTube(videoLink)

    # print("Title: ", yt.title)
    # print(yt.streams.filter(file_extension='mp4', progressive=True))

    downloadDirName = "yt-downloads"
    downloadDirPath = os.getcwd()+"/"+downloadDirName
    if(not os.path.isdir(downloadDirPath)):
        os.makedirs(downloadDirName)

    print(f"Downloading video with title: {yt.title}")

    yt.streams.get_by_itag(22).download(output_path=downloadDirPath)

    # video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    # video.download(downloadDirPath)

    print(f"YouTube video downloaded successfully at {downloadDirPath} and file name is {yt.title}.")

except Exception as error:
    print(f"Error while downloading: {error}")