import os, csv


path = "C:\\CodePython\\Mymodulles\\archive (1)\\"
file_name = 'Tweets.csv'
full_path = os.path.join(path, file_name)

lista = []


def ler_documento():

    with open(full_path, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = csv.reader(file, delimiter=',', quotechar='"', skipinitialspace=True)  # Trata das vírgulas internas

        for linha in conteudo:
            lista.append(linha)

    return lista


ler_documento()