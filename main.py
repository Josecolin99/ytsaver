# This code was based on: https://www.tiktok.com/@nextkoolhacks/video/7279420996585573637

# Python librarys
import os

# pytube library imports
from pytube import Playlist, YouTube
from pytube import exceptions

#? BASE_DIR represents the absolute path to the parent directory of the current script.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

folder = 'ignore_this/ELIMINAR'
download_folder = os.path.join(BASE_DIR, folder)
playlist = Playlist('https://www.youtube.com/playlist?list=PL_adZhO9fB0sO-tgDxLtC29wQ-T_Xs5Y2')
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