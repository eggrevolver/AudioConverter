from pydub import AudioSegment

from os import walk
from os.path import exists
from os.path import dirname
from os.path import splitext
from os import makedirs
from os.path import sep

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='base_dir', action='store')
parser.add_argument('-o', dest='output_dir', action='store')
parser.add_argument('-b', dest='bitrate', action='store')

args = parser.parse_args()

AUDIO_FILE_EXT_ALIASES = ['.mp3', '.mp4', '.m4a', '.wav', '.ogg', '.wma', '.flv', '.aac']

def file_paths(path):
    dirs = []
    current = path
    paths = []
    for (dirpath, dirnames, filenames) in walk(path):
        paths.extend([current + sep + file_name for file_name in filenames])
        dirs = [current + sep + dir_name for dir_name in dirnames]
        break

    if dirs is None or len(dirs) == 0:
        return paths
    else:
        for dir in dirs:
            sub_paths = file_paths(dir)
            if sub_paths is not None:
                paths.extend(sub_paths)
        return paths


def convert_list(paths):
    if exists(args.output_dir):
        raise FileExistsError(f'Directory {args.output_dir} already exists!')

    if paths is not None and len(paths) > 0:
        for path in paths:
            new_file_path = args.output_dir + sep + path[len(args.base_dir):]
            new_file_path, extension = splitext(new_file_path)

            if extension not in AUDIO_FILE_EXT_ALIASES:
                continue

            new_file_path = new_file_path + '.mp3'

            makedirs(dirname(new_file_path), exist_ok=True)
            file = AudioSegment.from_file(path, format=extension[1:])
            file.export(new_file_path, format='mp3', bitrate=args.bitrate)

paths = file_paths(args.base_dir)
convert_list(paths)

