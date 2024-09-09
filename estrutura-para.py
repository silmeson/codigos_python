'''
Essa estrutura de repetição é o mais comum em qualquer outra linguagem de programação

for (contador = 1; contador <=5; contador++){

}
'''
# 1 exemplo
for contador in range(1,5):
    print(contador)


print("-"*30)
#2 Exemplo
for contador in range(1,11,2):# 0 3 parâmetro irá aumentar o incremento dos valores que estão sendo exibidos
    print(contador)

print("-"*30)
#3 Exemplo - Números do maior para o menor
for contador in range(10,0,-1):
    print(contador, end="")# o comando end, informa 
