from funcoes.separarinformacao import *
'''Trabalhar a lista de dados dos nomes das airlines'''

separar_info()

nomes_airlines = []

def nomes_airlinesf():

    '''Criar lista com os nomes das airlines, para saber quantas existem'''
    for i in range(len(airline)):
        airline[i] = airline[i].strip()
        if airline[i] in nomes_airlines:
            continue
        else:
            nomes_airlines.append(airline[i])
    print(nomes_airlines)
    return nomes_airlines


nomes_airlinesf()
