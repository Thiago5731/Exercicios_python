#exercio
# Escreva um programa em Python que:
# Crie uma lista vazia.
# Use o método append() para adicionar 5 números inteiros de sua escolha.
# Declare uma constante chamada POS que guarda um índice (por exemplo, 2).
# Exiba na tela o valor que está nesse índice da lista.
# Exiba também o primeiro e o último elemento da lista.

lista = []
for c in range(5):
    lista.append(int(input('Digite o um numero: ')))
print(f'Sua lista ficou assim: {lista}')
POS = int(input('Digite um indice: '))
print(f'O indice selecionado equivale ao valor: {lista[POS]}')
print(f'O primeiro valor da lista é: {lista[0]} e o ultimo é: {lista[4]}')