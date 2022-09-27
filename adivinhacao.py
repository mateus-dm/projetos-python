import random

def jogar():

    introducao()
    numero_secreto = random.randrange(1, 100)
    total_de_tentativas = escolher_dificuldade()
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos #toda vez que o usuário erra um chute, a diferença entre o número do chute e o número random é diminuída da quantidade total de pontos. 

    print("Fim do jogo")

def introducao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def escolher_dificuldade():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas  

if (__name__ == "__main__"):
    jogar()