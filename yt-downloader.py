"""
    This script downloads youtube video using the link provided by user in argument
    Asks users for following inputs:
    1st input: YouTube URL
    2nd input: URL type (Video OR Playlist)
"""
from pytube import YouTube, Playlist
from sys import argv
import os

link_url = input("Enter YouTube URL: ")
link_type = input("Enter type of URL (Video OR Playlist): ")

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