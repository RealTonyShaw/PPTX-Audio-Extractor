import os
import zipfile
import glob
import shutil
from pathlib import Path


def modify_to_rar(path):
    if path.endswith('.pptx'):
        new_str = path[:-5] + '.zip'
        os.rename(path, new_str)
    else:
        print('File Type Error')


def decompress(path):
    zip_file = zipfile.ZipFile(path)
    tmp_decompression_path = path[:-4] + '_files'
    os.mkdir(tmp_decompression_path)
    os.chdir(tmp_decompression_path)
    zip_file.extractall()
    zip_file.close()


def extract_audio(path):
    files = glob.iglob(os.path.join(path + '/ppt/media', "*.m4a"))
    original_path = Path(path)
    savings_path = original_path.parent
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, savings_path)


def rm_cache(path):
    shutil.rmtree(path)


if __name__ == '__main__':