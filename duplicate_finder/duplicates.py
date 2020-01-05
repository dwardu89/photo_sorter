import logging
import getopt
import hashlib
import ntpath
import os
import shutil
import sys
import time
from os import listdir
from os.path import isfile, isdir, join

from PIL import Image

__author__ = "edwardvella"

file_types = []
logger = logging.getLogger("sorter")


def exif_info2time(ts):
    """
    changes EXIF date ('2005:10:20 23:22:28') to number of seconds since 1970-01-01
    Borrowed from http://code.activestate.com/recipes/550811-jpg-files-redater-by-exif-data/
    """
    tpl = time.strptime(ts + "UTC", "%Y:%m:%d %H:%M:%S%Z")
    return time.mktime(tpl)


def get_date_from_exif(file_path):
    im = Image.open(file_path)
    if hasattr(im, "_getexif"):
        try:
            exifdata = im._getexif()
            dt_value = exifdata[0x9003]
            exif_time = exif_info2time(dt_value)
            logger.debug(exif_time)
            return exif_time
        except (KeyError, TypeError):
            logger.debug(os.path.getmtime(file_path))
    return int(os.path.getmtime(file_path).time())


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def matches_file_type(f, file_types):
    if len(file_types) > 0:
        for file_type in file_types:
            if f.endswith("." + file_type):
                return True
        return False
    return True


def get_files(folder, recursive):
    if folder == ".":
        folder = os.getcwd()
    file_paths = [
        join(folder, f)
        for f in listdir(folder)
        if isfile(join(folder, f)) and matches_file_type(f, file_types)
    ]
    if recursive:
        folder_paths = [
            join(folder, f) for f in listdir(folder) if isdir(join(folder, f))
        ]
        for folder_path in folder_paths:
            files_to_append = get_files(folder_path, recursive)
            file_paths.extend(files_to_append)
    return file_paths


def hash_file(file_path):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(file_path, "rb") as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def flatten(input_array):
    result_array = []
    for element in input_array:
        if isinstance(element, str):
            result_array.append(element)
        elif isinstance(element, list):
            result_array += flatten(element)
    return result_array

def remove_singles(file_set):
    duplicated = dict()
    for k in file_set.keys():
        if len(file_set[k]) > 1:
            duplicated[k] = file_set[k]
    return duplicated

def print_duplicates(duplicates):
    for dupe in duplicates:
        print(dupe)

def find_duplicates(folder, recursive):
    file_paths = get_files(folder, recursive)
    duplicates = dict()
    for file_path in file_paths:
        file_hash = hash_file(file_path)
        if file_hash in duplicates.keys():
            duplicates[file_hash].append(file_path)
        else:
            duplicates[file_hash] = [file_path]
    duplicates = remove_singles(duplicates)
    print(len(duplicates))
    print_duplicates(duplicates)
    return duplicates

def delete_duplicates(folder, recursive):
    duplicates = find_duplicates(folder, recursive)
    for key in duplicates.keys():
        current_duplicate = duplicates[key]
        for i in range(1, len(current_duplicate)):
            os.remove(current_duplicate[i])
