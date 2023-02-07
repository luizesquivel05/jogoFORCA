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
    
    # faz as rodadas com base na quantidade de vidas:
    acertou = False # para quando acertar a palavra.
    vidasPERDIDAS = 0 # verifica quantas vidas foram perdidas
    while acertou == False and vidasPERDIDAS < vidas:
        letra = input("Digite uma letra: ").upper() # tentativa
        
        if letra in palDescrypt:
            for i in range(0, len(palAleatoria)):
                if letra == palDescrypt[i]:
                    palCrypt[i] = letra # muda a letra na palavra criptografada
        else:
            vidasPERDIDAS += 1 # perde uma vida
            print("Essa letra não existe na palavra.")
        print("".join(palCrypt))
    
        acertou = True # tenta afirmar que a palavra está certa.
        
        # verificação se a afirmação acima está certa:
        for i in range(0, len(palAleatoria)):
            if palCrypt[i] == "-" :
                acertou = False
                
    # finalização do jogo.
    if palDescrypt == palCrypt:
        print("Parabéns! você ganhou o jogo!")
    else:
        print("Infelizmente, você perdeu!")
    listaPalavras.remove(palAleatoria) # remove a palavra atual da lista de palavras
    if len(listaPalavras) >= 2:
        if str(input("Deseja continuar o jogo? S para SIM e N para NAO: ")).upper() == "S":
            # LIMPA O CLI:
            try:
                os.system('cls')
            except:
                os.system('clear')
        else:
            break
    else:
        break
print("FIM DE JOGO! OBRIGADO POR JOGAR CONOSCO")