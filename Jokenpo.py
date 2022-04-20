import random
import os

listaJogada = ['0', '2', '5']

print()
print("-------- Jokenpo --------")
print()
print("Digite o nome do jogador:")
print()
jogador1 = input()
jogador2 = "Boot"
os.system('cls')

print()
print("-------- Jokenpo --------")
print()
print(f"Nome do jogador numero 1: {jogador1}")
print(f"Nome do jogador numero 2: {jogador2}")
print()

# Laço de repetição para possibilitar um novo jogo.
fim = False
while fim == False:

    rodadas = int(input("Digite o número de rodadas: "))
    os.system('cls')

    # Laço de repetição para verificar se existe um vencedor.
    pontosJogador1 = 0
    pontosJogador2 = 0
    j1 = ''
    j2 = ''
    vencedor = False
    while vencedor == False:
        print()
        print("-------- Jokenpo --------")
        print()
        print("        Rodadas: %i"  %rodadas)
        print()
        print(f"'{jogador1}' {str(pontosJogador1)} X {str(pontosJogador2)} '{jogador2}'")
        print()
        print("Digite '0' para PEDRA")
        print("Digite '2' para TESOURA")
        print("Digite '5' para PAPEL")
        print()
        
        # Condição para validar a entrada correta do usuario.
        print(f"Jogada de '{jogador1}': ")
        j1 = input()
        if j1 == "0" or j1 == "2" or j1 == "5":
            j2 = random.choice(listaJogada)
            print(f"Jogada de '{jogador2}': ")
            print(j2)
            print()
        else:
            print()
            print("Opção incorreta.")

        # Logica usada para determinar o vencedor de cada rodada.
        # Em caso de empate não será computado uma rodada.
        if j1 == '0' and j2 == '2' or  j1 == '2' and j2 == '5' or j1 == '5' and j2 == '0':
            print(jogador1 , "venceu!")
            pontosJogador1 = pontosJogador1 + 1  
        elif j2 == '0' and j1 == '2' or  j2 == '2' and j1 == '5' or j2 == '5' and j1 == '0':
            print(jogador2 , "venceu")
            pontosJogador2 = pontosJogador2 + 1
        elif j1 == '0' and j2 == '0' or  j1 == '2' and j2 == '2' or j1 == '5' and j2 == '5':
            print ("empate")
        
        print()
        print("Pressione 'Enter' para continuar.")
        input()
        os.system('cls')    

        # Logica usada para determinar o vencedor do jogo.
        # No caso das rodadas serem um numero 'par', o jogo fará rodadas de desempate.
        if pontosJogador1 > (rodadas/2):
            vencedor = True
            print()
            print("PARABENS!", jogador1, " ganhou o jogo!")
            print()
            print("Deseja jogar novamente?")
            print("Presisone 'S' se deseja jogar novamente.")
            revanche = input().upper()
            if revanche == 'S':
                fim = False
            else:
                fim = True
                print()
                print ("Fim de jogo!")    
                print()  
        elif pontosJogador2 > (rodadas/2):
            vencedor = True
            print()
            print (f"Infelizmente o {jogador2} ganhou o jogo.") 
            print()
            print ("Boa sorte da próxima vez!")
            print()
            print("Deseja jogar novamente?")
            print("Presisone 'S' se deseja jogar novamente.")
            revanche = input().upper()
            if revanche == 'S':
                fim = False
            else:
                fim = True
                print()
                print ("Fim de jogo!") 
                print()
                
        print()