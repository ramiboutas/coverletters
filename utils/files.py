import os

def delete_path_file(path):
    if os.path.isfile(path):
       os.remove(path)
