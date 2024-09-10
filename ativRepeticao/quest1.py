soma = 0# inicializano uma variável
total = 0
for contador in range(50, 71):
    if contador % 2 == 0:
        soma = soma + contador # soma +=contador
        total = total + 1# total +=1

        print(f"A soma de todos os pares é {soma} e a média é {soma / total}")
