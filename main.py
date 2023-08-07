# ATENÇÃO - LISTA DE PROBLEMAS A SER RESOLVIDOS
# 2 ALÉM DA CONDIÇÃO DE PARADA JÁ IMPLEMENTADA
# 2.1 EMPATE(FALTA)
import random

# função que criar a matriz e preenche de 1 a 9
def matriz():
    # forma simplificada -> matrizJogo = [[""] * 3 for _ in range(3)]
    cont = 1
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(cont)
            cont += 1
        matriz.append(linha)
    return matriz

#função que monta o tabuleiro
def tabuleiro(matriz):
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("|" + 2 * " ", matriz[0][0], 2 * " " + "|" + 2 * " ", matriz[0][1], 2 * " " + "|" + 2 * " ", matriz[0][2], 2 * " " + "|")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("|" + 2 * " ", matriz[1][0], 2 * " " + "|" + 2 * " ", matriz[1][1], 2 * " " + "|" + 2 * " ", matriz[1][2], 2 * " " + "|")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("|" + 2 * " ", matriz[2][0], 2 * " " + "|" + 2 * " ", matriz[2][1], 2 * " " + "|" + 2 * " ", matriz[2][2], 2 * " " + "|")
    print("|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")

#função que verificar as condicões de finalização do jogo
def condicoesParada(matriz):
    if  matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" or \
        matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" or \
        matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" or \
        matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" or \
        matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" or \
        matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" or \
        matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" or \
        matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
        print("Parabéns! Você ganhou.")
        input("Pressione ENTER para sair.")
        return False
    elif  matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" or \
        matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" or \
        matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" or \
        matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" or \
        matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" or \
        matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" or \
        matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" or \
        matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
        print("Você perdeu.")
        input("Pressione ENTER para sair.")
        return False

    else:
        return True
def jogadas(matriz):
    teste = True
    escolhaJogador = True
    while teste:
        #jogada do bot
        if escolhaJogador:
            opcaoJogardorBot = random.randint(1, 9)
            print("Jogada do Computador (", opcaoJogardorBot, ")")
            match opcaoJogardorBot:
                case 1:
                    if matriz[0][0] == 1:
                        matriz[0][0] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 2:
                    if matriz[0][1] == 2:
                        matriz[0][1] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 3:
                    if matriz[0][2] == 3:
                        matriz[0][2] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 4:
                    if matriz[1][0] == 4:
                        matriz[1][0] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 5:
                    if matriz[1][1] == 5:
                        matriz[1][1] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 6:
                    if matriz[1][2] == 6:
                        matriz[1][2] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 7:
                    if matriz[2][0] == 7:
                        matriz[2][0] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 8:
                    if matriz[2][1] == 8:
                        matriz[2][1] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
                case 9:
                    if matriz[2][2] == 9:
                        matriz[2][2] = "O"
                        escolhaJogador = False
                    else:
                        print("nova jogada do bot")
                        escolhaJogador = True
            tabuleiro(matriz)
        teste = condicoesParada(matriz)
        #finaliza o while se ocorrer uma vitória
        if teste == False:
            break
        #jogada do usuário
        if not escolhaJogador:
            jogadasPossiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            opcaoJogador = int(input("Digite seu movimento entre 1 a 9: "))
            while opcaoJogador not in jogadasPossiveis:
                opcaoJogardor = int(input("Movimento errado, escolha um número entre 1 a 9: "))
            print("Sua jogada (", opcaoJogador, ")")
            match opcaoJogador:
                case 1:
                    if matriz[0][0] == 1:
                        matriz[0][0] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 2:
                    if matriz[0][1] == 2:
                        matriz[0][1] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 3:
                    if matriz[0][2] == 3:
                        matriz[0][2] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 4:
                    if matriz[1][0] == 4:
                        matriz[1][0] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 5:
                    if matriz[1][1] == 5:
                        matriz[1][1] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 6:
                    if matriz[1][2] == 6:
                        matriz[1][2] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 7:
                    if matriz[2][0] == 7:
                        matriz[2][0] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 8:
                    if matriz[2][1] == 8:
                        matriz[2][1] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case 9:
                    if matriz[2][2] == 9:
                        matriz[2][2] = "X"
                        escolhaJogador = True
                    else:
                        print("posição já escolhida, tente novamente.")
                        escolhaJogador = False
                case _:
                    print("Número incorreto! Tente novamente, Escolha a posição entre 1 a 9")
                    escolhaJogador = False
            tabuleiro(matriz)
        teste = condicoesParada(matriz)
jogadas(matriz())