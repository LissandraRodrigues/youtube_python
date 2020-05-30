# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve áudios e retorna as cinco palavras mais faladas no vídeo

# Importação.
import speech_recognition as sr

# Transcreve áudios e retorna quais foram as cinco palavra mais falada.
def transcribes(fileWAV):

    rec = sr.Recognizer()

    # Transcreve o áudio.
    with sr.AudioFile(fileWAV) as source:

        audio = rec.record(source)

        phrases = rec.recognize_google(audio, language = 'pt-BR')

    # Edita as frases geradas.
    editedPhrase = phrases.lower()

    editedPhrase = editedPhrase.split()

    uselessWords = []

    biggestFive = [(0, ''), (0, ''), (0, ''), (0, ''), (0, '')]

    file = open('uselessWords.txt', 'r')

    # Abre o arquivo que funciona como filtro, pois contém uma lista de palavras inúteis que devem ser descartadas.
    for line in file:

        uselessWords += [line.split('\n')[0]]

    file.close()

    # Para cada palavra da lista editedPhrase, o programa faz uma série de análises.
    for word in editedPhrase:

        counter = 0

        # Verifico se a palavra é inútil.
        if uselessWords.count(word) == 0:

            # Count retorna a quantidade de vezes que a palavra foi repetida.
            current = editedPhrase.count(word)

            counter_2 = len(editedPhrase) - 1

            # Apago a palavra analisada e todas as suas repetições.
            while counter_2 != 0:

                if editedPhrase[counter_2] == word:
                    editedPhrase.remove(editedPhrase[counter_2])

                counter_2 -= 1

            while counter != len(biggestFive):

                # Se a palavra for diferente de todas as outras já acrescentadas.
                if word != biggestFive[counter][1]:

                    # E for maior do que a menor palavra já inserida.
                    if current > biggestFive[0][0]:

                        # É deletada a menor palavra da lista
                        biggestFive.remove(biggestFive[0])

                        # E adicionada a nova palavra.
                        biggestFive.append((current, word))

                        # A lista é ordenada.
                        biggestFive.sort()

                    # E essa repetição é interrompida.
                    break

                counter += 1

    return biggestFive


