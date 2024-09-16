while true:
    nome = input("Digite um nome (nome e sobrenome): ")
    if len(nome) >15:
        prit("nome aceito!")
        break
    else:
        print("o nome deve ter mais de 15 letras. tente novamente.")


    #função len pesquisa: retorna o número de caracteres no string 