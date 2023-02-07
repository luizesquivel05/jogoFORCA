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
    
# LEITURA DA LISTA DE PALAVRAS:
listaPalavras = list()
i = 1
while i <= qtd:
    palavra = str(input(f"Digite a {i} º palavra:  ")).upper()
    listaPalavras.append(palavra)
    i += 1

# LIMPA O CLI:
try:
    os.system('cls')
except:
    os.system('clear')
    
continuacao = "SIM"

while continuacao:
    palAleatoria = random.choice(listaPalavras) # escolhe uma palavra da lista de palavras
    palDescrypt = list() # palavra descriptograda
    palCrypt = list() # palavra criptograda
    
    # pega palavra descriptografada:
    for i in palAleatoria:
        palDescrypt.append(i)
        
    # criptografia da palavra:
    for i in range(0, len(palAleatoria)):
        palCrypt.append("-")
    print("".join(palCrypt))