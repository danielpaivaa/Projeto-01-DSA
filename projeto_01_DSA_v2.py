import random
from unidecode import unidecode
from os import system, name

#Função que limpa a tela a cada exacução
def Limpa_tela():
    
    #Caso o sistema seja Windows
    if name == 'nt':
        _= system('cls')

    #Caso seja Mac ou Linux
    else:
        _= system('clear')

def Gerador_de_palavra_secreta():

    tema = random.choice(['animais', 'frutas', 'nomes', 'objetos', 'paises'])

    with open(f'./Palavras/lista_{tema}.txt', encoding='UTF-8') as file:
        palavra = (random.choice(file.readlines()).strip())
    return tema, palavra

def Mostra_forca(chances):
    estagio = [
        """
        --------
        |      |
        |      O
        |     \\|/
        |     / \\
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |     / 
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |     
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |     
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |     
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     
        |     
        |
        -
        """,
        """
        --------
        |      |
        |      
        |     
        |     
        |
        -
        """
    ]
    return estagio[chances]
    
def game():

    Limpa_tela()

    print('\nBem-vindo ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')

    #Lista de paravras secretas
    tema, palavra_secreta = Gerador_de_palavra_secreta()
    palavra_secreta = palavra_secreta.lower()

    #Define o número de "tracinhos" que aparecerá
    letras_certas = ['_' for letra in palavra_secreta]

    #Número de tentativas
    num_tentativas = 6

    #Letras erradas
    letras_erradas = []


    while num_tentativas > 0:

        Limpa_tela()
        print('\nDica:', tema)
        print(Mostra_forca(num_tentativas))
        print(' '.join(letras_certas))
        print('\nChances restantes:', num_tentativas)
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativas = input('\nDigite uma letra: ').lower()

        if tentativas in unidecode(palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                
                if tentativas == letra:
                    letras_certas[index] = tentativas
                index += 1
                
        else:
            num_tentativas -= 1
            letras_erradas.append(tentativas)

        if "_" not in letras_certas:
            print('\nParabén! Você venceu, a palavra era:', palavra_secreta)
            break
    if "_" in letras_certas:
        print(Mostra_forca(num_tentativas))
        print('\nQue pena, você perdeu, a palavra era:', palavra_secreta)

#Bloco main
if __name__ == "__main__":
    game()
    print('\nParabéns! Você está aprendendo programação em Python com a DSA. :D\n')

