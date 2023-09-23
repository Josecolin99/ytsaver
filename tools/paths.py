import os
from constants import generals

def media_root(dir):
    return os.path.join(generals.BASE_DIR, 'assets', dir)
    