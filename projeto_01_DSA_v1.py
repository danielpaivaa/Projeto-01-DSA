import random
from os import system, name

#Função que limpa a tela a cada exacução
def Limpa_tela():
    
    #Caso o sistema seja Windows
    if name == 'nt':
        _= system('cls')

    #Caso seja Mac ou Linux
    else:
        _= system('clear')
   
def game():

    Limpa_tela()

    print('\nBem-vindo ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')

    #Lista de paravras secretas
    palavras_secreta = ['celular', 'banana', 'casa', 'vaca', 'computador']

    #Escolhe uma palavra aleatoriamente da lista
    palavra = random.choice(palavras_secreta)

    #Define o número de "tracinhos" que aparecerá
    letras_certas = ['_' for letra in palavra]

    #Número de tentativas
    num_tentativas = (len(palavra))

    #Letras erradas
    letras_erradas = []


    while num_tentativas > 0:

        print(' '.join(letras_certas))
        print('\nChances restantes: ', num_tentativas)
        print('Letras erradas: ', ' '.join(letras_erradas))

        tentativas = input('\nDigite uma letra: ').lower()

        if tentativas in palavra:
            index = 0

            for letra in palavra:
                
                if tentativas == letra:
                    letras_certas[index] = tentativas
                index += 1
                
        else:
            num_tentativas -= 1
            letras_erradas.append(tentativas)

        if "_" not in letras_certas:
            print('\nVocê venceu, a palavra era:', palavra)
            break
    if "_" in letras_certas:
        print('\nVocê perdeu, a palavra era:', palavra)

#Bloco main
if __name__ == "__main__":
    game()
    print('\nParabéns! Você está aprendendo programação em Python com a DSA. :D\n')

