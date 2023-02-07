import random
import os

# LEITURA DA QUANIDADE DE VIDAS:
vidas = int(input("Informe O numero de vidas: ")) 
while vidas <= 0:
    vidas = int(input("O número de vidas deve ser maior ou igual a 1: "))

# LEITURA DA QUANTIDADE DE PALAVRAS:
qtd = int(input("Digite a quantidade de palavras: "))
while qtd <= 0:
    qtd = int(input("A quantidade de palavras deve ser maior ou igual a 1: "))

# LIMPA O CLI:
try:
    os.system('cls')
except:
    os.system('clear')