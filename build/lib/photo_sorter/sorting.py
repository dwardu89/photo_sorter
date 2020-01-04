import logging
import getopt
import imghdr
import ntpath
import os
import shutil
import sys
import time
from os import listdir
from os.path import isfile, isdir, join

from PIL import Image

__author__ = 'edwardvella'

file_types = ['jpeg']
logger = logging.getLogger("sorter")

def exif_info2time(ts):
    """
    changes EXIF date ('2005:10:20 23:22:28') to number of seconds since 1970-01-01
    Borrowed from http://code.activestate.com/recipes/550811-jpg-files-redater-by-exif-data/
    """
    tpl = time.strptime(ts + 'UTC', '%Y:%m:%d %H:%M:%S%Z')
    return time.mktime(tpl)


def get_date_from_exif(file_path):
    im = Image.open(file_path)
    if hasattr(im, '_getexif'):
        try:
            exifdata = im._getexif()
            dt_value = exifdata[0x9003]
            exif_time = exif_info2time(dt_value)
            logger.debug(exif_time)
            return exif_time
        except (KeyError, TypeError):
            logger.debug(os.path.getmtime(file_path))
            return int(os.path.getmtime(file_path))
    return int(os.path.getmtime(file_path)).time()


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def is_image_file(file):
    return imghdr.what(file) in file_types


def get_image_files(folder, recursive):
    if folder == '.':
        folder = os.getcwd()
    file_paths = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    if recursive:
        folder_paths = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]
        for folder_path in folder_paths:
            files_to_append = get_image_files(folder_path, recursive)
            file_paths.extend(files_to_append)
    return [f for f in file_paths if is_image_file(f)]


def move_file_to_folder(file_path, destination_folder):
    if destination_folder == '.':
        destination_folder = os.getcwd()
    creation_date = time.gmtime(os.path.getmtime(file_path))

    final_path = join(destination_folder, time.strftime('%Y/%m/%d', time.gmtime( get_date_from_exif(file_path))))

    logger.debug(final_path)
    logger.debug(path_leaf(file_path))
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    final_path = join(final_path, path_leaf(file_path))
    shutil.move(file_path, final_path)


def sort(folder, outputfolder, recursive):
    file_paths = get_image_files(folder, recursive)
    for file_path in file_paths:
        move_file_to_folder(file_path, outputfolder)
