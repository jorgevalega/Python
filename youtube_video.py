from pytube import YouTube
import pandas as pd
import os

url = input("ingrese la url correspondiente: ")

def descargar_youtube(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=False).first()
    destino = "videos"
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    return new_file

# Descargar audio 
video_file = descargar_youtube(url)
