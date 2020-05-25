#! /usr/bin/env python3

'''
findLargestFolder.py - find the folder in a directory tree
that uses the most disk space
'''

import os, sys
from pathlib import Path

def findLargestDir(start='.'):
    max_size = 0
    largest_folder = ''

    for folder_name, sub_folders, file_names in os.walk(Path.home()):
        folder_size = 0
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            if not os.path.islink(file_path):
                folder_size += os.path.getsize(file_path)

        if folder_size > max_size:
            max_size = folder_size
            largest_folder = folder_name

    return largest_folder, max_size

folder, max_size = findLargestDir()

print(f'The largest directory is {folder} ({max_size / 1000000000} gigabytes).')
