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

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def matches_file_type(f, file_types):
    logger.debug("File Types to check [{}]".format(file_types))
    if len(file_types) > 0:
        for file_type in file_types:
            if f.endswith("." + file_type):
                return True
        return False
    return True


def get_files(folder, recursive, file_types):
    if folder == ".":
        folder = os.getcwd()
    logger.debug("Listing files in [{}]".format(folder))
    logger.debug("Recursive? [{}]".format(recursive))
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
            files_to_append = get_files(folder_path, recursive, file_types)
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
    data = []
    for hash in duplicates:
        for file_path in duplicates[hash]:
            data.append([hash, file_path])

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        logger.info("".join(word.ljust(col_width) for word in row))


def find_duplicates(folder, recursive, file_types, verbose):
    if verbose:
        logger.setLevel(logging.DEBUG)
    file_paths = get_files(folder, recursive, file_types)
    duplicates = dict()
    for file_path in file_paths:
        file_hash = hash_file(file_path)
        if file_hash in duplicates.keys():
            duplicates[file_hash].append(file_path)
        else:
            duplicates[file_hash] = [file_path]
    duplicates = remove_singles(duplicates)
    logger.debug("Found [{}] duplicates".format(len(duplicates)))
    print_duplicates(duplicates)
    return duplicates


def delete_duplicates(folder, recursive, file_types, verbose):
    duplicates = find_duplicates(folder, recursive, file_types, verbose)
    for key in duplicates.keys():
        current_duplicate = duplicates[key]
        for i in range(1, len(current_duplicate)):
            os.remove(current_duplicate[i])
