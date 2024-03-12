"""
    This script downloads youtube video using the link provided by user in argument
    first argument: type of url : video or playlist
    second argument: url
"""
from pytube import YouTube, Playlist
from sys import argv
import os

# 0th argument is always program name
# 1st argument is first command line parameter
# 2nd argument is second command line parameter

link_type = argv [1]
link_url = argv[2]

download_dir_name = "yt-downloads"

def createOrCheckDir(download_dir_name):
    download_dir_path = os.getcwd()+"/"+download_dir_name
    if(not os.path.isdir(download_dir_path)):
        print(f"Downloads directory not Present! ")
        print(f"Creating directory with name: {download_dir_name}")
        os.makedirs(download_dir_name)
    else:
        print(f"Downloads directory is present.")
    return download_dir_path

def download(link_url, download_dir_name):
    download_dir_path = createOrCheckDir(download_dir_name)
    if str.lower(link_type) == "playlist":
        p = Playlist(link_url)
        for url in p.video_urls:
            downloadVideo(url, download_dir_path)
    elif str.lower(link_type) == "video":
        downloadVideo(link_url, download_dir_path)
    else:
        print(f"Invalid option entered for first argument!")


def downloadVideo(link_url, download_dir_path):
    # download_dir_path = createOrCheckDir(download_dir_name)
    try:
        yt = YouTube(link_url)
        print(f"Downloading video with title: {yt.title}")
        yt.streams.get_by_itag(22).download(output_path=download_dir_path)
        print(f"YouTube video downloaded successfully at {download_dir_path} and file name is {yt.title}.")
    except Exception as error:
        print(f"Error while downloading: {error}")
    pass

downloadVideo(link_url, download_dir_name)