import os
import shutil


def clear_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            shutil.rmtree('%s/%s' % (root, dir))
        for file in files:
            os.remove('%s/%s' % (root, file))
