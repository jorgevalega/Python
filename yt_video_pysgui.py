import PySimpleGUI as sg
from pytube import YouTube
import pandas as pd
import os

layout = [
    [sg.Text("Digite ou cole o link para baixar o vídeo aqui")],
    [sg.InputText(key="url")],
    [sg.Button("Baixar Vídeo")],
    [sg.Text("", key="baixando")]
]

janela = sg.Window("Baixar vídeo do YouTube", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Baixar Vídeo":
         janela["baixando"].update("Espere até terminar de baixar o vídeo...")
    
    def baixar_video():
        url = valores['url']
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=False).first()
        destino = "videos"
        out_file = video.download(output_path=destino)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        return new_file
    
    baixar_video()
    




janela.close()

