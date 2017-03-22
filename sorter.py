#!/usr/bin/python
import getopt
import imghdr
import os
import sys
import time
from os import listdir
from os.path import isfile, isdir, join
import shutil
import ntpath

__author__ = 'edwardvella'

file_types = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'bmp', 'png']


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def is_image_file(file):
    return imghdr.what(file) in file_types


def get_image_files(folder, recursive):
    if folder == '.':
        folder = os.getcwd()
    onlyfiles = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    if recursive:
        onlyfolders = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]
        for folder_to_parse in onlyfolders:
            files_to_append = get_image_files(folder_to_parse, recursive)
            onlyfiles.extend(files_to_append)
    return [f for f in onlyfiles if is_image_file(f)]


def move_file_to_folder(file_path, destination_folder):
    if destination_folder == '.':
        destination_folder = os.getcwd()
    creation_date = time.gmtime(os.path.getmtime(file_path))
    final_path = join(destination_folder, time.strftime('%Y/%m/%d', time.gmtime(os.path.getmtime(file_path))))
    print file_path
    print final_path
    print path_leaf(file_path)
    if not os.path.exists(final_path):
        print final_path
        os.makedirs(final_path)
    final_path = join(final_path, path_leaf(file_path))
    shutil.move(file_path, final_path)


def sort(folder, outputfolder, recursive):
    thefiles = get_image_files(folder, recursive)
    for file_path in thefiles:
        # creation_date = time.strftime('%Y/%m/%d', time.gmtime(os.path.getmtime(file_path)))
        move_file_to_folder(file_path, outputfolder)


def main(argv):
    """
    The main call for the sorter, in order to run this you need to follow the format.
    This has to be called from the command line 'python sorter.py -f <folder> -o <outputfolder> -r <recursive>'
    :param argv:
    :return: None
    """
    folder = ''
    outputfolder = ''
    recursive = False

    try:
        opts, args = getopt.getopt(argv, "h:f:o:r", ["help", "folder=", "outputfolder=", "recursive"])
    except getopt.GetoptError:
        print 'sorter.py -f <folder> -o <outputfolder> -r <recursive>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'sorter.py -f <folder> -o <outputfolder> -r <recursive>'
            sys.exit()
        elif opt in ("-f", "--folder"):
            folder = arg
        elif opt in ("-o", "--outputfolder"):
            outputfolder = arg
        elif opt in ("-r", "--recursive"):
            recursive = True
    sort(folder, outputfolder, recursive)


if __name__ == "__main__":
    main(sys.argv[1:])
