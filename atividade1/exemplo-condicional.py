valor = int(input("Informe um valor numérico:"))

if valor >= 50:
    print(f"O número {valor} é maior igual a 50\n")

# elif é o mesmo que else if, junção dos dois
elif valor >= 30 and valor < 50:
    print(f"O número {valor} está entre 30 e 50\n")

else:
    print(f"O número {valor} é menor que 50\n")