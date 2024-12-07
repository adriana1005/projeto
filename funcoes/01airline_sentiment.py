from funcoes.separarinformacao import *

negative = 0
positive = 0
neutral = 0
erro = 0


def airline_sentimentf():
    airline_sentiment.pop(0)

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


airline_sentimentf()

