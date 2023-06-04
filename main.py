                        #ATENÇÃO - LISTA DE PROBLEMAS A SER RESOLVIDOS
#1 VERIFICAR ERRO NA JOGADA DO BOT AO ESCOLHER A MESMA POSIÇÃO
#2 ALÉM DA CONDIÇÃO DE PARADA JÁ IMPLEMENTADA(TERMINAR AO PREENCHER O TABULEIRO)
    #2.1 EMPATE, QUEM GANHOU E QUEM PERDEU
#3 TRATAR A ENTRADA DO USUÁRIO PARA NÚMEROS ENTRE 1 E 9
import random

#função que criar a matriz e preenche de 1 a 9
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
    # VERIFICAÇÃO PARA SABER SE DEVE TERMINAR O LAÇO WHILE, TERMINA SE NÃO TIVER MAIS NÚMEROS DE 1 A 9
    if 1 in matriz[0] or 2 in matriz[0] or 3 in matriz[0] or \
            4 in matriz[1] or 5 in matriz[1] or 6 in matriz[1] or \
            7 in matriz[2] or 8 in matriz[2] or 9 in matriz[2]:
        return True
    else:
        return False

def jogadas(matriz):
    teste = True
    i = 0
    while teste:
        #jogada do bot
        if i % 2 == 0:
            opcaoJogardorBot = random.randint(1, 9)
            print("Jogada do Computador (", opcaoJogardorBot, " ", i, ")")
            match opcaoJogardorBot:
                case 1:
                    if matriz[0][0] != "O" and matriz[0][0] != "X":
                        matriz[0][0] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 2:
                    if matriz[0][1] != "O" and matriz[0][1] != "X":
                        matriz[0][1] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 3:
                    if matriz[0][2] != "O" and matriz[0][2] != "X":
                        matriz[0][2] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 4:
                    if matriz[1][0] != "O" and matriz[1][0] != "X":
                        matriz[1][0] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 5:
                    if matriz[1][1] != "O" and matriz[1][1] != "X":
                        matriz[1][1] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 6:
                    if matriz[1][2] != "O" and matriz[1][2] != "X":
                        matriz[1][2] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 7:
                    if matriz[2][0] != "O" and matriz[2][0] != "X":
                        matriz[2][0] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 8:
                    if matriz[2][1] != "O" and matriz[2][1] != "X":
                        matriz[2][1] = "O"
                    else:
                        print("nova jogada do bot")
                        i -= 1
                case 9:
                    if matriz[2][2] != "O" and matriz[2][2] != "X":
                        matriz[2][2] = "O"
                    else:
                        print("nova jogada do bot")
                    i -= 1
            teste = condicoesParada(matriz)
            tabuleiro(matriz)
            i += 1
        #jogada do usuário
        if i % 2 != 0:
            opcaoJogardor = int(input("Digite seu movimento entre 1 a 9: "))
            print("Sua jogada (", opcaoJogardor, " ", i, ")")
            match opcaoJogardor:
                case 1:
                    if matriz[0][0] != "O" and matriz[0][0] != "X":
                        matriz[0][0] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 2:
                    if matriz[0][1] != "O" and matriz[0][1] != "X":
                        matriz[0][1] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 3:
                    if matriz[0][2] != "O" and matriz[0][2] != "X":
                        matriz[0][2] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 4:
                    if matriz[1][0] != "O" and matriz[1][0] != "X":
                        matriz[1][0] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 5:
                    if matriz[1][1] != "O" and matriz[1][1] != "X":
                        matriz[1][1] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 6:
                    if matriz[1][2] != "O" and matriz[1][2] != "X":
                        matriz[1][2] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 7:
                    if matriz[2][0] != "O" and matriz[2][0] != "X":
                        matriz[2][0] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 8:
                    if matriz[2][1] != "O" and matriz[2][1] != "X":
                        matriz[2][1] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case 9:
                    if matriz[2][2] != "O" and matriz[2][2] != "X":
                        matriz[2][2] = "X"
                    else:
                        print("posição já escolhida, tente novamente.")
                        i -= 1
                case _:
                    print("Número incorreto! Tente novamente, Escolha a posição entre 1 a 9")
                    i -= 1
            teste = condicoesParada(matriz)
            tabuleiro(matriz)
            i += 1
jogadas(matriz())