import random


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

def jogador(matriz):
    # ALTERAR LOOP PARA TRUE ENQUANTO A MATRIZ TIVER UM NÚMERO
    teste = True
    i = 0
    while teste:
        #jogada do bot
        # VERIFICAR SE O BOT ESTA ESCOLHENDO OUTRO NÚMERO, CASO ESTEJA OCUPADO
        if i % 2 == 0:
            opcaoJogardorBot = random.randint(1, 9)
            match opcaoJogardorBot:
                case 1:
                    if matriz[0][0] != "O" and matriz[0][0] != "X":
                        matriz[0][0] = "O"
                    else:
                        i -= 1
                case 2:
                    if matriz[0][1] != "O" and matriz[0][1] != "X":
                        matriz[0][1] = "O"
                    else:
                        i -= 1
                case 3:
                    if matriz[0][2] != "O" and matriz[0][2] != "X":
                        matriz[0][2] = "O"
                    else:
                        i -= 1
                case 4:
                    if matriz[1][0] != "O" and matriz[1][0] != "X":
                        matriz[1][0] = "O"
                    else:
                        i -= 1
                case 5:
                    if matriz[1][1] != "O" and matriz[1][1] != "X":
                        matriz[1][1] = "O"
                    else:
                        i -= 1
                case 6:
                    if matriz[1][2] != "O" and matriz[1][2] != "X":
                        matriz[1][2] = "O"
                    else:
                        i -= 1
                case 7:
                    if matriz[2][0] != "O" and matriz[2][0] != "X":
                        matriz[2][0] = "O"
                    else:
                        i -= 1
                case 8:
                    if matriz[2][1] != "O" and matriz[2][1] != "X":
                        matriz[2][1] = "O"
                    else:
                        i -= 1
                case 9:
                    if matriz[2][2] != "O" and matriz[2][2] != "X":
                        matriz[2][2] = "O"
                    else:
                        i -= 1
            print("jogada no bot\n",matriz)
        #jogada do usuário
        if i % 2 != 0:
            opcaoJogardor = int(input("Escolha uma posição entre 1 a 9: "))
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
                    #decremento de -1 para voltar para o mesmo jogador
                    i -= 1
            print("sua jogada\n",matriz)
        i += 1
        #VERIFICAÇÃO PARA SABER SE DEVE TERMINAR O LAÇO WHILE, TERMINA SE NÃO TIVER MAIS NÚMEROS DE 1 A 9
        #TENTE FAZER ESSA VERIFICAÇÃO COM O FOR
        if  1 in matriz[0] or 2 in matriz[0] or 3 in matriz[0] or \
            4 in matriz[1] or 5 in matriz[1] or 6 in matriz[1] or \
            7 in matriz[2] or 8 in matriz[2] or 9 in matriz[2]:
            teste = True
        else:
            teste = False
jogador(matriz())