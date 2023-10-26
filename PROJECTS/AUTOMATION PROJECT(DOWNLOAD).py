from os import scandir, rename
from os.path import splitext, join, exists
from shutil import move
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep


# printimg all files in a directory
# source_dir = r"C:\Users\user\Downloads"
# with scandir(source_dir) as entries:
#     for entry in entries:
#         print(entry)



source_dir  = r"C:\Users\user\Downloads"
dest_dir_image = r"C:\Users\user\Pictures"


image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]



def make_union(dest, name):
    filename, extention = splitext(name)
    counter  = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extention}"
        counter+=1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_union(dest, name)
        oldname = join(dest, name)
        newname = join(dest, unique_name)
        rename(oldname, newname)
    move(entry, dest)



class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_image_files(entry, name)


    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"moved image file", {name})




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
