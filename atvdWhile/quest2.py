 contador_impar = 0

 while true:
    valor = int(input("Digite um valor numérico (digite 0 para parar): "))
    if valor == 0:
        break
    if valor % 2 != 0:
        contador_impar += 1

print(f"os números ímpares são: {contador_impar}")