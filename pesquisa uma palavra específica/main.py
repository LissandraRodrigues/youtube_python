# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Programa que faz download de um vídeo do Youtube em MP4, converte para WAV,
# separa em partes menores, transcreve o que foi falado no vídeo e
# mostra a quantidade de vezes que a palavra que usuário inseriu foi falada.

# Importações.
from downloadVideo import *
from parts import *
from single import *
from split_audio import *

# Programa principal.
def main():

    print('\nQual palavra você deseja procurar no vídeo?')

    # Pega do usuário a palavra que será procurada.
    searchedWord = input('Digite aqui: ').lower()

    # Link do vídeo que será feito o download.
    link = 'COLOQUE O LINK DO VÍDEO AQUI'

    # Cria um arquivo WAV do vídeo.
    video = downloadVideo(link)

    # Divide o vídeo em partes menores.
    videoParts = split_audio(video)

    # Se o vídeo tiver apenas uma parte.
    if videoParts == 0:

        result = single(searchedWord, video)

    # Caso o vídeo tenha mais partes.
    else:

        result = parts(searchedWord, videoParts)

    print('\nA palavra {} foi falada: {} vezes no vídeo!'.format(searchedWord, result))

main()