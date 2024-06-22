from pytube import YouTube
import pandas as pd
import os

url = input("ingrese la url correspondiente: ")

def descargar_youtube(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    destino = "audios"
    out_file = audio.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

# Descargar audio 
audio_file = descargar_youtube(url)