from funcoes.separarinformacao import *


def airline_sent_pop():      #Função para retirar o primeiro elemento da lista
    '''Trabalhar lista dos sentimentos dos tweets
    ex: 'negative' , 'positive', 'neutro' '''
    airline_sentiment.pop(0)
    return airline_sentiment


def airline_sentimentf():
    negative = 0
    positive = 0
    neutral = 0
    erro = 0

    for i in range(len(airline_sentiment)):
        airline_sentiment[i] = airline_sentiment[i].strip().lower()

        if airline_sentiment[i] == 'negative':
            negative += 1
        elif airline_sentiment[i] == 'positive':
            positive += 1
        elif airline_sentiment[i] == 'neutral':
            neutral += 1
        else:
            erro += 1
            print(airline_sentiment[i])
    print(f'{erro}  erro')
    print(f'{negative}  negative')
    print(f'{positive}  positive')
    print(f'{neutral} neutral')

    return [erro, negative, positive, neutral]

