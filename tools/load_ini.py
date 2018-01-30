import json
import os


def load_ini(path):
    if not os.path.exists(path):
        return dict()
    fr = open(path, 'r')
    ini = dict()
    for line in fr:
        if line.strip() == '':
            continue
        slices = line.strip().split('=')
        ini[slices[0]] = json.loads(slices[1])
    fr.close()
    return ini
