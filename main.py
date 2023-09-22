from pytube import Playlist, YouTube
from pytube import exceptions

playlist = Playlist('https://www.youtube.com/playlist?list=PLPyj1P8a2S6WUEpf-SQIFMH1MUhEXVJ81')
for video in playlist:
    print('Starting download of:')
    print(YouTube(video).title)
    try:
        YouTube(video).streams.get_audio_only().download('C:/secret_files/Random/jimmy')
    except exceptions.AgeRestrictedError:
        print('Video con restriccion de edad')
    except Exception as ex:
        print(ex)
    print('FINISHED'.center(50, '='))