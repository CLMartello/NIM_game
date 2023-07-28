#essa função vai definir toda vez que o computador jogar
def computador_escolhe_jogada(n, m):
    vence = True
    x = 1
    if n <= m:
        vence = True
        x = n
        print("O computador tirou", x, "peça(s).")
        return(x)
    if (n-x) % (m+1) == 0 and m >= x:
        vence = True
        print("O computador tirou", x, "peça(s).")
        return(x)
    else:
        vence = False
    while not vence:
        x = x+1
        if (n-x) % (m+1) == 0 and m >= x:
            vence = True
            print("O computador tirou", x, "peça(s).")
            return(x)
        
#essa função vai definir toda vez que o usuario jogar
def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças você vai tirar?"))
    valido = True
#mudei aqui para deixar só x dif de zero, para ver se melhora minha pontuação
#como estava está registrado no jogonim sem numero
    if x != 0:
        valido = True
        print("Você tirou", x, "peça(s).")
        return(x)
    else:
        valido = False
    while not valido:
        print("Oops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n, m)

#essa função faz a partida em si, irá pedir os valores iniciais e irá organizar
#a vez de cada jogador
def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    inicio = True
    x = 0
    if m == 0:
        print("O limite de peças por jogada não pode ser zero! Você perdeu!")
    else:
        if n % (m+1) != 0 or n == m and n >= m:
            inicio = True
            print("Computador começa!")
            while n > 0:
                x = computador_escolhe_jogada(n, m)
                n = n-x
                print("Agora resta(m)", n, "peça(s) no tabuleiro.")
                if n > m:
                    x = usuario_escolhe_jogada(n, m)
                    n = n-x
                    print("Agora resta(m)", n, "peça(s) no tabuleiro.")
                if n == 0:
                    return print("Fim do jogo! o Computador ganhou!")
        else:
            inicio = False
            print("Você começa!")
            while n > 0 and n >= m:
                x = usuario_escolhe_jogada(n, m)
                n = n-x
                print("Agora resta(m)", n, "peça(s) no tabuleiro.")
                if n > 0:
                    x = computador_escolhe_jogada(n, m)
                    n = n-x
                    print("Agora resta(m)", n, "peça(s) no tabuleiro.")
                if n == 0:
                    return print("Fim do jogo! o Computador ganhou!")

#essa função irá estabelecer o campeonato, dando os nomes e jogando 3 partidas
def campeonato():
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
#até o final da rodada 2 funciona bem, mostra que foi o computador que ganhou
    print("**** Rodada 3 ****")
    partida()
#após essa partida, ele simplesmente fecha a janela, não mostra as frases finais
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")
#não sei se ele mostra muito rápido e fecha ou se ele só não mostra

#essa função dá início ao jogo, explica e pergunta se o usuario quer jogar uma
#única partida ou um campeonato
def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    a = int(input("Qual você escolhe?"))
#se o jogador escolher 1, inicio irá puxar a função de partida única
    if a == 1:
        partida()
#se o jogador escolher 2, inicio irá puxar a função campeonato com 3 partidas
    if a == 2:
        campeonato()
#se o jogador escolher qualquer coisa diferente de 1 ou de 2, inicio irá
#reiniciar até o jogador escolher um número válido
    if a != 1 and a != 2:
        return inicio()

#esse comando inicia o jogo quando o programa é colocado para correr
inicio()