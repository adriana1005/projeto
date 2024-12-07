from funcoes.separarinformacao import *
import matplotlib.pyplot as plt

nulo = 0
intervalo1 = 0  #0.0 to 0.1
intervalo2 = 0  #0.11 to 0.2
intervalo3 = 0  #0.21 to 0.3
intervalo4 = 0  #0.31 to 0.40
intervalo5 = 0  #0.41 to 0.5
intervalo6 = 0  #0.51 to 0.6
intervalo7 = 0  #0.61 to 0.7
intervalo8 = 0  #0.71 to 0.8
intervalo9 = 0  #0.81 to 0.9
intervalo10 = 0  #0.91 to 1.00
valores = []

def airline_sentiment_confidencef():
    global nulo, intervalo1, intervalo2, intervalo3, intervalo4, intervalo5
    global valores, intervalo6, intervalo7, intervalo8, intervalo9, intervalo10

    dados = airline_sentiment_confidence.pop(0)
    for i in range(len(dados)):
        dados[i] = float(dados[i])  #passar elementos string para float
        if dados == '':
            nulo += 1
        elif 0.0 <= dados[i] <= 0.1:
            intervalo1 += 1
        elif 0.11 <= dados[i] <= 0.2:
            intervalo2 += 1
        elif 0.21 <= dados[i] <= 0.3:
            intervalo3 += 1
        elif 0.31 <= dados[i] <= 0.4:
            intervalo4 += 1
        elif 0.41 <= dados[i] <= 0.5:
            intervalo5 += 1
        elif 0.51 <= dados[i] <= 0.6:
            intervalo6 += 1
        elif 0.61 <= dados[i] <= 0.7:
            intervalo7 += 1
        elif 0.71 <= dados[i] <= 0.8:
            intervalo8 += 1
        elif 0.81 <= dados[i] <= 0.9:
            intervalo9 += 1
        elif 0.91 <= dados[i] <= 1.0:
            intervalo10 += 1
    valores.append(nulo)
    valores.append(intervalo1)
    valores.append(intervalo2)
    valores.append(intervalo3)
    valores.append(intervalo4)
    valores.append(intervalo5)
    valores.append(intervalo6)
    valores.append(intervalo7)
    valores.append(intervalo8)
    valores.append(intervalo9)
    valores.append(intervalo10)

    return valores


airline_sentiment_confidencef()


def grafico_sentiment_confidence():
    valores = airline_sentiment_confidencef()
    print(valores)
    categorias = ['nulo', '0.0 to 0.1', '0.11 to 0.2', '0.21 to 0.3', '0.31 to 0.40', '0.41 to 0.5', '0.51 to 0.6', '0.61 to 0.7', '0.71 to 0.8', '0.81 to 0.9', '0.91 to 1.00' ]

    plt.bar(categorias, valores)  #criação do gráfico de barras
    plt.xlabel('Categorias')
    plt.ylabel('Valores')

    plt.show() #exibir o gráfico
    plt.title('Gráfico de Barras com Matplotlib')

grafico_sentiment_confidence()
