animais = ['Cachorro', 'gato', 'ovelha']
print(type(animais)) #exibindo o tipo da variável

print(animais)

print('-'*50)
for elementos in animais:
    print(elementos)

#1etapa: atualização de dados
print('-'*50)
animais[0] = "coelho"
print(animais)

#2 etapa: inserir itens na lista
print('-'*50)
#forma1 - usando append
animais.append("cavalo")#irá inserir um novo item no final da lista
print(animais)

#forma2 - usando insert
animais.insert(1,"pássaro")
print(animais)


#3 etapa: excluir itens na lista
#forma1 - usando pop
animais.pop() #irá excluir sempre o último item
print(animais)

#forma2 - usando pop() com índice
animais.pop(0) #escolhendo qual índice quero excluir
print(animais)

#forma3 - usando remove
animais.remove("ovelha") #irá remover o item pelo seu conteúdo
print(animais)
