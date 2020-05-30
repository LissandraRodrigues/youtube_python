# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve o áudio do vídeo analisado e
# mostra a quantidade de vezes que a palavra que usuário inseriu foi falada.

# Importações.
from transcribes import *

import os

# Transcreve cada parte do vídeo e diz se a palavra foi encontrada.
def single(searchedWord, video):

        # Pega a quantidade de vezes que uma palavra foi falada.
        result = transcribes(searchedWord, video)

        # Apaga o WAV.
        os.remove(video)

        return result
