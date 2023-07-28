def computador_escolhe_jogada(n, m):
    vence = True
    x = 1
    if (n-x) % (m+1) != 0 or m == x and m >= x:
        vence = True
        print("O computador tirou", x, "peça(s).")
        return(x)
    else:
        vence = False
    while not vence:
        x = x+1
        if (n-x) % (m+1) != 0 or m ==x and m >= x:
            vence = True
            print("O computador tirou", x, "peça(s).")
            return(x)
        
 
def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças você vai tirar?"))
    valido = True
    if (n-x) % (m+1) == 0 or m == x and m >= x:
        valido = True
        print("Você tirou", x, "peça(s).")
        return(x)
    else:
        valido = False
    while not valido:
        print("Oops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n, m)


def partida():
    n = int(input("Quantas peças iniciais?"))
    m = int(input("Qual o limite de peças por jogada?"))
    inicio = True
    x = 0
    if n % (m+1) != 0 or n == m and n >= m:
        inicio = True
        print("Computador começa!")
        while n > 0 and n >= m:
            x = computador_escolhe_jogada(n, m)
            n = n-x
            print("Agora resta(m)", n, "peça(s) no tabuleiro.")
            x = usuario_escolhe_jogada(n, m)
            n = n-x
            print("Agora resta(m)", n, "peça(s) no tabuleiro.")
            if n == 0:
                return print("Fim do jogo! o Computador ganhou!")
    else:
        inicio = False
        print("Você começa!")
        while n > 0:
            x = usuario_escolhe_jogada(n, m)
            n = n-x
            print("Agora resta(m)", n, "peça(s) no tabuleiro.")
            x = computador_escolhe_jogada(n, m)
            n = n-x
            print("Agora resta(m)", n, "peça(s) no tabuleiro.")
            if n == 0:
                return print("Fim do jogo! o Computador ganhou!")

            
        






    
