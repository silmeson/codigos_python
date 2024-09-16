while True:
    login1 = input("Informe o seu login: ")
    senha1 = input("Informe sua senha: ")

    if login1 != senha1:
        while True:
            login2 = input("Informe seu login: ")
            senha2 = input("Inform sua senha: ")

            if login2 != login1 and login2 != senha2:
                break
            else:
                print("Login e senha são iguais ou login1 é igual ao login2")
        break
    else:
        print("Login1 e senha1 são iguais")