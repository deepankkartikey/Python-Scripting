from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = '/Users/deepankkartikey/Downloads'
dest_dir_sfx = '/Users/deepankkartikey/Downloads/Sound'
dest_dir_music = '/Users/deepankkartikey/Downloads/Sound/Music'
dest_dir_video = '/Users/deepankkartikey/Downloads/Videos'
dest_dir_image = '/Users/deepankkartikey/Downloads/Images'
dest_dir_documents = '/Users/deepankkartikey/Downloads/Documents'
dest_dir_codefiles = '/Users/deepankkartikey/Downloads/CodeFiles'
dest_dir_misc = '/Users/deepankkartikey/Downloads/Others'

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mkv",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
# supported Code types
code_extensions = [".py", ".java", ".cpp", ".jsx", ".js", ".css", ".html"]

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    #  THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    #  .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_code_files(entry, name)
                # self.check_miscellaneous_files(entry, name)

    def check_audio_files(self, entry, name):  # Checks all Audio Files
        logging.info(f"Checking for Audio files ...")
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # ? 10Megabytes
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # Checks all Video Files
        logging.info(f"Checking for Video files ...")
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # Checks all Image Files
        logging.info(f"Checking for Image files ...")
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # Checks all Document Files
        logging.info(f"Checking for Document files ...")
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_code_files(self, entry, name):  # Checks all code Files
        logging.info(f"Checking for Code files ...")
        for code_extension in code_extensions:
            if name.endswith(code_extension) or name.endswith(code_extension.upper()):
                move_file(dest_dir_codefiles, entry, name)
                logging.info(f"Moved Code file: {name}")

    def check_miscellaneous_files(self, entry, name):  # Checks miscellaneous Files
        logging.info(f"Checking for Miscellaneous files ...")
        if len(name.split('.')) > 1:
            file_extension = name.split('.')[1]
            all_file_extensions = image_extensions + video_extensions + audio_extensions + code_extensions + document_extensions
            if file_extension.lower() not in all_file_extensions:
                move_file(dest_dir_misc, entry, name)
                logging.info(f"Moved Miscellaneous file: {name}")
        else:
            move_file(dest_dir_misc, entry, name)
            logging.info(f"Moved Miscellaneous file: {name}")


# Following code is take from watchdog website example
# 
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()