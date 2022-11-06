import numpy as np
import pandas as pd

#Questão 1
#a
dfPaises = pd.read_csv('paises.csv', delimiter = ';') #carregando o dataset usando o pandas
paisesOceania = dfPaises['Country'][dfPaises['Region'].str.contains('OCEANIA')] #paises da oceania
print(paisesOceania)

#b
print(len(paisesOceania)) #quantidade de paises da oceania

#Questão 2
mediaAlfabetizacao = dfPaises['Literacy (%)']
print(mediaAlfabetizacao.mean()) #media da alfabetização do Planeta

#Questão 3
maiorPop = dfPaises[['Country','Region']][dfPaises['Population'] == max(dfPaises['Population'])] #paises e população
print(maiorPop)

#Questão 4
dfPaises['Country'][dfPaises['Coastline (coast/area ratio)'] == 0].to_csv('noCoast.csv', sep=';', header = False) #salvando em um novo arquivo csv os paises sem costa
