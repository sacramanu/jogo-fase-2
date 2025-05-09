import random

def escolher_dificuldade():
    print("escolha a dificuldade:)")
    print("fácil (30 tentativas)")
    print("médio (15 tentativas)")
    print("difícil (5 tentativas)")

dificuldade_valida= False

escolher_dificuldade= ()

while not dificuldade_valida:
    dificuldade= input("digite a dificuldade:fácil,médio ou difícil: ")
    if dificuldade =="fácil":
        tentativas = 30
        penalidade = 10
        dificuldade_valida = True
    elif dificuldade =="médio":
        tentativas = 15
        penalidade = 20
        dificuldade_valida= True 
    elif dificuldade =="difícil":
        tentativas = 5
        penalidade = 30
        dificuldade_valida = True
    else:
        print("escolha invalida, tente novamente:")

numero_secreto = random.randint (10,100)
pontuacao = 100

print("\nJogo iniciado!Good luck bitch!")

while tentativas > 0:
    print(f"\ntentativas restantes: {tentativas}")
    print (f"pontuação atual: {pontuacao}")

    entrada_valida = False
    while not entrada_valida:
        try:
            chute = int (input("digite um numero entre 10 e 100"))
            if 10 <= chute <=100:
                entrada_valida= True
            else:
                print("numero fora do intervalo,tente novamente")
        except ValueError:
                print("entrada invalida digite um numero inteiro")
    if chute ==numero_secreto:
        print(f"\nParabéns! voce acertou({numero_secreto})")
        print (f"Pontuaçao final: {pontuacao}")
        break
    else:
        print ("errado!")
        pontuacao -= penalidade 
        tentativas-= 1

    if tentativas ==0:
        print(f"\nFim de jogo. O numero secreto era {numero_secreto}!")
        print("tente novamente")


        



