# importação da biblioteca Panda
import pandas as pd

#criação de um DataFrame

data = {'Nome': ['Joao', 'Maria', 'Rafael', 'Filipe', 'Joao5', 'Joao6', 'Joao7', 'Joao8', 'Joao9', 'Joao10'],
         'Idade': [60, 55, 25, 30, 31, 32, 33, 34, 35, 36],
         'Cidade': ['Rio de Janeiro', 'Alagoas', 'Brasília', 'Goiania', 'Goiania5', 'Goiania6', 'Goiania7', 'Goiania8', 'Goiania9', 'Goiania10']}

#linha de comando para passar o DATAFRAME para variável df
df= pd.DataFrame(data)

#apresentação na tela do DATAFRAME
print(df.head())
#fazendo calculos para idade com a função describe

# Calculando estatísticas descritivas apenas para a coluna 'Idade'
idade_descricao = df['Idade'].describe()

# Exibindo apenas o desvio padrão da idade
print("Desvio padrão da idade:", idade_descricao['std'])
print("A média da idade:", idade_descricao['mean'])