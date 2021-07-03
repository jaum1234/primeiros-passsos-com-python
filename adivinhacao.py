print("*********************************\n")
print("Bem vindo ao jogo de adivinhaçao!");
print("\n*********************************\n")

numero_secreto = 42;

tentativa = 1;
total_tentativas = 3;

while (tentativa <= total_tentativas):

    print("Tentativa ", tentativa, " de ", total_tentativas, end="\n\n");

    # A funçao input devolve uma string
    chute_str = input("Digite o seu numero: ");
    print(type(chute_str), "\nNote que a funçao input devolve uma string\n");

    # Conversao de string para int
    chute_int = int(chute_str);
    print(type(chute_int), "\nPor isso utilizamos a funçao int() para converter a string para um inteiro\n");
    

    print("Voce digitou: ", chute_int);
    print("O número secreto era: ", numero_secreto);

    acertou = chute_int ==  numero_secreto;
    maior = chute_int > numero_secreto;
    menor = chute_int < numero_secreto


    if (acertou):
        print("Voce acertou!");
        break
    else:
        if (maior):
            print("Voce errou... O seu chute foi maior que o numero secreto.");
        elif (menor):
            print("Voce errou... Seu chute foi menor que o numero secreto.", end="\n\n");

    tentativa += 1;
  


print("Fim de jogo.");