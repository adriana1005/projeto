from funcoes.airline_sentiment import airline_sent_pop
from funcoes.airline import airline_pop

#airline = airline_pop()
#sentiment = airline_sent_pop()






def lista_zip():
    '''Criar lista de tuplas para a parte de analisar
    os sentimentos dos comentários pela airline para fazer as percentagens'''
    #print(len(airline_pop()))
    #print(len(sentiment))
    lista_res = list(zip(airline_pop(), airline_sent_pop()))


    print(lista_res)

    return lista_res

'''FALTA: criar função para analisar e fazer as percentagens 
dos sentimentos em função à airline(PODE SER DENTRO DA OUTRA)'''

lista_zip()
