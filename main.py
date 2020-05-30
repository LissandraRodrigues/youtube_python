# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Programa que faz download de um vídeo do Youtube em MP4, converte para WAV,
# separa em partes menores, transcreve o que foi falado no vídeo e
# cria um CSV que contém o link e as cinco palavras mais falada no vídeo.

# Importações.
from downloadVideo import *
from parts import *
from single import *
from split_audio import *

# Programa principal.
def main():

    # Link do vídeo que será feito o download.
    link = 'COLOQUE O LINK DO VÍDEO AQUI'

    # Cria um arquivo WAV do vídeo.
    video = downloadVideo(link)

    # Divide o vídeo em partes menores.
    videoParts = split_audio(video)

    # Se o vídeo tiver apenas uma parte.
    if videoParts == 0:

        single(link, video)

    # Caso o vídeo tenha mais partes.
    else:

        parts(link, videoParts)

main()