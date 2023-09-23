# This code was based on: https://www.tiktok.com/@nextkoolhacks/video/7279420996585573637

# Python librarys
import os

# pytube library imports
from pytube import Playlist, YouTube
from pytube import exceptions

# Import Constants
from constants import generals as const_general
#? BASE_DIR represents the absolute path to the parent directory of the current script.

def save_playlist(folder: str, url: str):
    #!Agregar un verificador regex del folder destino
    download_folder = os.path.join(const_general.BASE_DIR, folder)
    print(download_folder)
    playlist = Playlist(url)
    count = 1
    for video in playlist:
        print('Starting download of:')
        print(YouTube(video).title)
        try:
            YouTube(video).streams.get_audio_only().download(download_folder)
        except exceptions.AgeRestrictedError:
            print('Video con restriccion de edad')
        except Exception as ex:
            print(ex)
        print('FINISHED'.center(50, '='))
        count += 1

    print()
    print('TOTAL DE DESCARGAS')
    print(count)

# CodedByColin