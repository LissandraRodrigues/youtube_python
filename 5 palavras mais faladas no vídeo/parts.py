# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve o áudio de cada parte do vídeo analisado e
# gera um CSV contendo as cinco palavras mais faladas no vídeo.

# Importações.
from transcribes import *
from createfileCSV import *

import os

# Transcreve cada uma das partes do vídeo e gera o CSV.
def parts(link, parts):

    # Lista que irá armazenar as tags de todas as partes do vídeo.
    tagsFinalList = []

    counter = 1

    # Enquanto a quantidade de vídeos for maior do que zero.
    while parts > 0:

        # Define o nome do áudio que será analisado.
        video = 'audio' + str(counter) + '.wav'

        # Pega as cinco palavras mais faladas de cada vídeo.
        tags = transcribes(video)

        sizeTags = len(tags) - 1

        # Enquanto a quantidade de tags novas for maior do que zero.
        while sizeTags >= 0:

            sizeTagsFinalList = len(tagsFinalList) - 1

            # Enquanto a quantidade de tags da lista final for maior do que zero.
            while sizeTagsFinalList >= 0:

                # Verifica se a tag nova já foi inserida anteriormente.
                # Caso tenha sido, atualiza o número de menções.
                if tags[sizeTags][1] == tagsFinalList[sizeTagsFinalList][1]:

                    # Armazeno o nome atual de tagsFinalList.
                    tagName = tagsFinalList[sizeTagsFinalList][1]

                    # Armazeno o valor atual de tagsFinalList.
                    newValue = (tagsFinalList[sizeTagsFinalList][0] + tags[sizeTags][0])

                    tags.remove(tags[sizeTags])

                    tagsFinalList.remove(tagsFinalList[sizeTagsFinalList])

                    tagsFinalList.append((newValue, tagName))

                    break

                sizeTagsFinalList -= 1

            sizeTags -= 1

        sizeFinal = len(tags)

        counter_2 = 0

        # Verifica se sobrou alguma palavra na lista tags.
        if sizeFinal != 0:

            # Se sobrou, adiciona à lista final.
            while counter_2 != sizeFinal:

                tagsFinalList += [(tags[counter_2])]

                counter_2 += 1

        # Apaga cada parte do vídeo.
        os.remove(video)

        counter += 1
        parts -= 1

    # Ordena a lista em ordem crescente.
    tagsFinalList.sort()

    # Inverte a lista.
    tagsFinalList.reverse()

    # Adiciona o link e as cinco primeiras tags ao CSV.
    createfileCSV(link,
                  tagsFinalList[0][1],
                  tagsFinalList[1][1],
                  tagsFinalList[2][1],
                  tagsFinalList[3][1],
                  tagsFinalList[4][1])

    # Deleta o vídeo base.
    os.remove('analyzedVideo.wav')

