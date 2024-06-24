import customtkinter as ctk
from pytube import YouTube
import pandas as pd
import os

# Criar janela principal
janela = ctk.CTk()
janela.geometry("450x200")
janela.title("Baixar vídeo")
janela.resizable(width=False, height=False)


entry = ctk.CTkEntry(master=janela, placeholder_text="Digite ou cole o link para baixar o vídeo aqui", width=320)
entry.pack(pady=30, padx=20)


def submit_input():
    input_text = entry.get()
    yt = YouTube(input_text)
    video = yt.streams.filter(only_audio=False).first()
    destino = "videos"
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    return new_file

submit_button = ctk.CTkButton(master=janela, text="Baixar", command=submit_input)
submit_button.pack(pady=10)

# Iniciar o loop principal do aplicativo
janela.mainloop()