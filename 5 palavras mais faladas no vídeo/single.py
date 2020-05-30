# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve o áudio do vídeo analisado e
# gera um CSV contendo as cinco palavras mais faladas no vídeo.

# Importações.
from createfileCSV import *
from transcribes import *

import os

# Transcreve cada parte do vídeo e gera o CSV.
def single(link, video):

        # Pega a tag principal.
        tags = transcribes(video)

        # Adiciona o link e a tag ao CSV.
        createfileCSV(link, tags[0][1], tags[1][1], tags[2][1], tags[3][1], tags[4][1])

        # Apaga o WAV.
        os.remove(video)

