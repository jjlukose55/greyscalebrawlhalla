import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join

def find_directory(target_dir, start_path='/'):
    for root, dirs, files in os.walk(start_path):
        if target_dir in dirs:
            return os.path.join(root, target_dir)
    return None
