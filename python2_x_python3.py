pergunta = input("Voce sabe a diferença entre Python2 e Python3? (s/n): ");

if (pergunta == 's' or pergunta == 'sim'):
    print("\nFodasse, vou explixar mesmo assim :D");
    print(
        "Python3 -> print(\"texto\", sep=\"\", end=\"\")\n",
        "Python2 -> print \"texto\"\n\n"
        "Python3 -> input() devolve string\n",
        "Python2 -> input() converte o valor automaticamete para o tipo digitado. Desse modo era usado o raw_input(), que nao realizava a conversao automatimente\n\n"
        );
else:
    print("Entao vamos aprender :D");
    print("Python3 -> print(\"texto\", sep=\"\" end=\"\").\n",
        "Python2 -> print \"texto.\"\n\n"
        "Python3 -> input() devolve string.\n",
        "Python2 -> input() converte o valor automaticamete para o tipo digitado. Desse modo era usado o raw_input(), que nao realizava a conversao automatimente.\n\n"
        );
