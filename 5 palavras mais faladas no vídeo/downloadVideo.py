# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que, por meio do link inserido, faz download de um vídeo do Youtube em MP4 e converte para WAV.

# Importações.
from pydub import AudioSegment
from pytube import YouTube

import os

# Retorna um vídeo em formato WAV.
def downloadVideo(link):

    video = YouTube(link)

    # Pega o vídeo em extensão MP4.
    video.streams.filter(file_extension = 'mp4').all()

    # Define o nome do arquivo.
    name = 'analyzedVideo'

    video.streams.get_by_itag(140).download(filename = name)

    # Define a extensão do arquivo.
    videoMP4 = name + '.mp4'

    mp4_version = AudioSegment.from_file(videoMP4, 'mp4')

    # Define a extensão do arquivo.
    videoWAV = name + '.wav'

    # Converte o vídeo MP4 em WAV.
    mp4_version.export(videoWAV, format = 'wav')

    # Deleta a versão MP4 do vídeo.
    os.remove(name + '.mp4')

    return videoWAV

