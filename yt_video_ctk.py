import customtkinter as ctk
from pytube import YouTube
import pandas as pd
import os

# Criar janela principal
janela = ctk.CTk()
janela.geometry("450x200")
janela.title("Baixar vídeo")
janela.resizable(width=False, height=False)

# Criar a entrada principal para a url
# url_label = ctk.CTkLabel(janela, text="digite ou cole a url", font=("Helvetica", 30))
# url_label.pack(pady=20)

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


def baixar_youtube(entry):
    yt = YouTube(entry)
    video = yt.streams.filter(only_audio=False).first()
    destino = "videos"
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    return new_file

# Descargar video 
# video_file = baixar_youtube(entry)


# Criar um label para exibir a hora
# tempo_label = ctk.CTkLabel(janela, text="00:00:00", font=("Helvetica", 48))
# tempo_label.pack(pady=20)



# Botão Iniciar
# iniciar_botao = ctk.CTkButton(janela, text="Iniciar", command=iniciar)
# iniciar_botao.pack(side=ctk.LEFT, padx=20)



# Iniciar o loop principal do aplicativo
janela.mainloop()