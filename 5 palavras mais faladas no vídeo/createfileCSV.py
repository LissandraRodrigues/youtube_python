# 30/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Função responsável por escrever em um arquivo CSV o link do vídeo analisado
# e as cinco palavras mais faladas nesse vídeo.

# Importações
from tempfile import NamedTemporaryFile

import csv
import shutil
import os

# Adiciona o link e a tag em um arquivo CSV.
def createfileCSV(link, tag_1, tag_2, tag_3, tag_4, tag_5):

    # Define o cabeçalho do CSV.
    fieldnames = ['Link', 'Tag_1', 'Tag_2', 'Tag_3', 'Tag_4', 'Tag_5']

    # Define o nome do arquivo CSV.
    file = 'tags.csv'

    # Verificação se já existe o arquivo, caso não exista, o faz.
    if not os.path.isfile(file):

        # Faz o arquivo.
        makeFile = csv.writer(open(file, 'wb'))

        # Abre o arquivo.
        with open(file, 'w', newline = '') as csvfile:

            # Acrescenta o cabeçalho ao novo CSV.
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

            writer.writeheader()

    tempfile = NamedTemporaryFile(mode = 'w', delete = False)

    # Abre o arquivo.
    with open(file, 'r') as csvfile, tempfile:

        reader = csv.DictReader(csvfile, fieldnames = fieldnames)

        writer = csv.DictWriter(tempfile, fieldnames = fieldnames)

        # Para o que já estava inserido não ser apagado.
        for row in reader:

            row = {'Link': row['Link'],
                   'Tag_1': row['Tag_1'],
                   'Tag_2': row['Tag_2'],
                   'Tag_3': row['Tag_3'],
                   'Tag_4': row['Tag_4'],
                   'Tag_5': row['Tag_5']}

            writer.writerow(row)

        # Após escrever tudo o que já tinha, escreve a nova linha.
        row = {'Link': link,
               'Tag_1': tag_1,
               'Tag_2': tag_2,
               'Tag_3': tag_3,
               'Tag_4': tag_4,
               'Tag_5': tag_5}

        writer.writerow(row)

    shutil.move(tempfile.name, file)