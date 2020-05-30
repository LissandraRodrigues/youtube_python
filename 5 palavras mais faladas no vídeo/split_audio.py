# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função que separa um áudio WAV em um conjunto de áudios menores com duração de 10 segundos.

# Importação.
from pydub import AudioSegment

# Divide o áudio em partes menores. 
def split_audio(file):
    
    # Pega o áudio.
    sound = AudioSegment.from_file(file)

    # Divide o vídeo a cada 10 segundos (10000 milissegundos).
    partsSound = len(sound) // 10000

    partsNumber = 0

    # Verifica se o video é maior que 1 minuto.
    if partsSound > 1:
        
        nameAudio = 'audio'
        
        extensionAudio = '.wav'  

        for currentPartNumber in range(1, partsSound + 1):

            if currentPartNumber == 1:  # Primeira parte do vídeo.

                # Define o nome do arquivo.
                path = nameAudio + str(currentPartNumber) + extensionAudio

                # Gera um vídeo com os primeiros 10 segundos.
                audio = sound[:10000]
                
                audio.export(path, format = 'wav')

                partsNumber += 1

            else:

                # Define o nome do arquivo.
                path = nameAudio + str(currentPartNumber) + extensionAudio

                # Gera vídeos com duração de 10 segundos.
                audio = sound[10000 * (currentPartNumber - 1):10000 * currentPartNumber]
                
                audio.export(path, format = 'wav')
                
                partsNumber += 1

    return partsNumber