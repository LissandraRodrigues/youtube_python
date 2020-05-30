# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que transcreve áudios e
# retorna a quantidade de vezes que a palavra que usuário inseriu foi falada.

# Importação.
import speech_recognition as sr

# Transcreve áudios e retorna quais foram as cinco palavra mais falada.
def transcribes(searchedWord, fileWAV):

    rec = sr.Recognizer()

    try:

        # Transcreve o áudio.
        with sr.AudioFile(fileWAV) as source:

            audio = rec.record(source)

            phrases = rec.recognize_google(audio, language = 'pt-BR')

        # Edita as frases geradas.
        editedPhrase = phrases.lower()

        editedPhrase = editedPhrase.split()

        current = editedPhrase.count(searchedWord)

    except:

        current = 0

    return current

