from funcoes.ler_documento import *


tweet_id = []  #0
airline_sentiment = []  #1
sentiment_c = [] #2
negativereason = [] #3
negativereason_confidence = [] #4
airline = [] #5
airline_sentiment_gold = [] #6
name = []  #7
negativereason_gold = []  #8
retweet_count = [] #9
text = [] #10
tweet_coord =[] #11
tweet_created = [] #12
tweet_location = [] #13
user_timezone = [] #14


def separar_info():

    for linha in lista:

        if len(linha) != 15:
            print(lista.index(linha))
            print(len(linha))
            print(linha)
            continue

        tweet_id.append(linha[0])
        airline_sentiment.append(linha[1])
        sentiment_c.append(linha[2])
        negativereason.append(linha[3])
        negativereason_confidence.append(linha[4])
        airline.append(linha[5])
        airline_sentiment_gold.append(linha[6])
        name.append(linha[7])
        negativereason_gold.append(linha[8])
        retweet_count.append(linha[9])
        text.append(linha[10])
        tweet_coord.append(linha[11])
        tweet_created.append(linha[12])
        tweet_location.append(linha[13])
        user_timezone.append(linha[14])

    tweet_id.pop(0)
    airline_sentiment.pop(0)
    sentiment_c.pop(0)
    negativereason.pop(0)
    negativereason_confidence.pop(0)
    airline.pop(0)
    airline_sentiment_gold.pop(0)
    retweet_count.pop(0)
    text.pop(0)
    tweet_coord.pop(0)
    tweet_created.pop(0)
    tweet_location.pop(0)
    user_timezone.pop(0)


    return [tweet_id, airline_sentiment, sentiment_c, negativereason, negativereason_confidence, airline,
            airline_sentiment_gold, retweet_count, text, tweet_coord, tweet_created, tweet_location, user_timezone]


print(separar_info()[1])