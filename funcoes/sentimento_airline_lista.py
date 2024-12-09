
from funcoes.separarinformacao import *


separar_info() #Chamar a função das listas


def lista_zip():
    '''Criar lista de tuplas para a parte de analisar
    os sentimentos dos comentários pela airline para fazer as percentagens'''
    #print(len(airline_pop()))
    #print(len(sentiment))
    lista_res = list(zip(airline, airline_sentiment))


    return lista_res



'''FALTA: criar função para analisar e fazer as percentagens 
dos sentimentos em função à airline(PODE SER DENTRO DA OUTRA)'''

lista_zip()

