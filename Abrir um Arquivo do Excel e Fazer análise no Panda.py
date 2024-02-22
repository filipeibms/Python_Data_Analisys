#importa a biblioteca do banda
import pandas as pd

#abrir arquivo do excel e mostrar os dados na tela

df = pd.read_excel('Pasta2.xlsx')

#mostrar dados obtidos do excel
print(df.head(12))

#calculo do desvio padrao de vendas
Desvio_padrao= df['Vendas'].describe()
Média_vendas= df['Vendas'].describe()

print("O desvio padrao das Vendas", Desvio_padrao['std'])

print("A média das Vendas", Média_vendas['mean'])