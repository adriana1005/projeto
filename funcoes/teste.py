import matplotlib.pyplot as plt

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Criação do gráfico de barras
plt.bar(categorias, valores)

# Adicionando rótulos e título
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras com Matplotlib')

# Exibindo o gráfico
plt.show()