#exercicio65
resposta = 'S'
soma = quantidade = media = 0
while resposta in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += 1
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar(s/n): ')).upper().strip()[0]
media = soma/quantidade
print (f'Você digitou: {quantidade} e a media é: {media}') 
print (f'O maior foi: {maior} e o menor foi: {menor}')