# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve o áudio de cada parte do vídeo analisado e
# retorna a quantidade de vezes que a palavra que usuário inseriu foi falada.

# Importações.
from transcribes import *

import os

# Transcreve cada uma das partes do vídeo e gera o CSV.
def parts(searchedWord, parts):

    counter = 1

    times = 0

    # Enquanto a quantidade de vídeos for maior do que zero.
    while parts > 0:

        # Define o nome do áudio que será analisado.
        video = 'audio' + str(counter) + '.wav'

        # Soma a quantidade de vezes que a palavra que usuário inseriu foi falada.
        times += (transcribes(searchedWord, video))

        # Apaga o áudio
        os.remove(video)

        counter += 1

        parts -= 1

    # Deleta o vídeo base.
    os.remove('analyzedVideo.wav')

    # Retorna a quantidade de vezes que a palavra foi falada.
    return times


