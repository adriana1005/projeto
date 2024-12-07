from funcoes.ler_documento import *


tweet_id = []  #0
airline_sentiment = []  #1
airline_sentiment_confidence = [] #2
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
        #print(linha)

        tweet_id.append(linha[0])
        airline_sentiment.append(linha[1])
        airline_sentiment_confidence.append(linha[2])
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

    return [tweet_id, airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, airline_sentiment_gold, retweet_count, text,
            tweet_coord, tweet_created, tweet_location, user_timezone]


print(separar_info()[2])
