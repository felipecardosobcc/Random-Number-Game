from random import randint

num_sorteado = 0
num_escolhido = 1
tentativas = 0

def dica(a, b):
    if a > b:
        print("DICA: o número é maior.")
    elif a < b:
        print("DICA: o número é menor.")

print()
print("Este programa permite que você tente adivinhar que número entre 1 e 100 foi gerado.")
controle = input("Digite 'OK' para continuar:\n")
print()

if controle.lower() == "ok":
    num_sorteado = randint(1, 100)
    print("--Informe o nível de dificuldade do jogo--")
    print("="*42)
    print("FÁCIL -> Com dicas e chances ilimitadas.\nDIFÍCIL -> Com dicas e apenas 6 chances.\nHARDCORE -> Sem dicas e apenas 3 chances.")
    print("="*42)
    dificuldade = input("Digite 'F' para fácil, 'D' para difícil ou 'H' para hardcore:\n")
    print()
    if dificuldade.upper() == "F":
        num_escolhido = int(input('Tente adivinhar qual número foi gerado: '))
        if num_sorteado != num_escolhido:
            tentativas += 1
            print("Não desista !!! :)")
            dica(num_sorteado, num_escolhido)
            while num_sorteado != num_escolhido:
                num_escolhido = int(input('Tente outra vez: '))
                tentativas += 1
                dica(num_sorteado, num_escolhido)
            print()
            print(f'Você conseguiu na {tentativas}° tentativa!')
            print()
        else:
            tentativas += 1
            print("PARABÉNS! VOCÊ ACERTOU DE PRIMEIRA :D :D :D")
            print()
    elif dificuldade.upper() == 'D':
        num_escolhido = int(input('Tente adivinhar qual número foi gerado: '))
        if num_sorteado != num_escolhido:
            tentativas += 1
            print("Não desista !!! :)")
            dica(num_sorteado, num_escolhido)
            while num_sorteado != num_escolhido:
                num_escolhido = int(input('Tente outra vez: '))
                tentativas += 1
                dica(num_sorteado, num_escolhido)
                if tentativas == 6:
                    break
            if num_escolhido == num_sorteado: 
                print()
                print(f'Você conseguiu na {tentativas}° tentativa!')
                print()
            else:
                print()
                print(f'O número era {num_sorteado}')
                print("Suas chances acabaram. Você perdeu :(")
                print()
        else:
            tentativas += 1
            print("PARABÉNS! VOCÊ ACERTOU DE PRIMEIRA :D :D :D")
            print()
    elif dificuldade.upper() == 'H':
        while num_escolhido != num_sorteado:
            num_escolhido = int(input('ADIVINHE OU PERCA: '))
            if num_escolhido != num_sorteado:
                print("Mero mortal...")
                tentativas += 1
            else:
                print("VOCÊ ALCANÇOU A IMORTALIDADE !!!!")
            if tentativas == 3:
                break    
        if num_escolhido != num_sorteado:
            print(f'\nO número era {num_sorteado}')
            print("SUAS 3 TENTATIVAS FORAM INÚTEIS. PAGUE COM SUA ALMA!!!\n")
        else:
            print(("\nParabéns...você conquistou o título de deus, ex-mortal...\n").upper())
    else:
        print("Ops. Algo deu errado!")
else:
    print("Ops, algo deu errado!")