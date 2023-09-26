import os
import sys
from constants import generals

def media_root(sub_path):
    if getattr(sys, 'frozen', False):
        # Estamos ejecutando como un ejecutable empaquetado con PyInstaller
        base_dir = sys._MEIPASS
    else:
        # Estamos ejecutando en un entorno de desarrollo normal
        base_dir = generals.BASE_DIR

    return os.path.join(base_dir, 'assets', sub_path)