import os
import zipfile
import glob
import shutil
from pathlib import Path


def duplicate(path):
    shutil.copy2(path, path + '_cpy')
    return path + '_cpy'


def modify_to_rar(path):
    if path.endswith('.pptx_cpy'):
        new_str = path[:-9] + '.zip'
        os.rename(path, new_str)
        return new_str
    else:
        print('File Type Error')


def decompress(path):
    zip_file = zipfile.ZipFile(path)
    tmp_decompression_path = path[:-4] + '_files'
    os.mkdir(tmp_decompression_path)
    os.chdir(tmp_decompression_path)
    zip_file.extractall()
    zip_file.close()
    return tmp_decompression_path


# extract audios to the parent directory of current path
def extract_audio(path):
    files = glob.iglob(os.path.join(path + '/ppt/media', "*.m4a"))
    original_path = Path(path)
    savings_path = original_path.parent
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, savings_path)


def rm_cache(path):
    if path.endswith('.zip'):
        os.remove(path)
    else:
        shutil.rmtree(path)


def extract_from(path):
    duplication_path = duplicate(path)
    modification_path = modify_to_rar(duplication_path)
    decompression_path = decompress(modification_path)
    extract_audio(decompression_path)
    rm_cache(modification_path)
    rm_cache(decompression_path)
