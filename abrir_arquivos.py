#abrir arquivos python
#open 
#manipulação de arquivos

#open("aqui devemos passar a localização, a naõ ser que esteja na mesma pasta, assim é so o nome""modos como abrir ")
#modos: 
#r = leitura
#w = escrita (sobre escreve o arquivo)
#a = anexar(adicionar ao final)
#x = criação exclusiva 

arquivo = open('contatos.txt', 'w', encoding='utf-8') #metodo para abrir um arquivo 
arquivo.write('Roberto - 3215432')

#não aceita aencuações a não ser que eu coloque encoding='utf-8'

arquivo.close()#metodo para fechar arquivo (sempre fechar quando finalizar a edição)

# eu tmb posso abrir com with assim ele fecha automatico quando acaba
with open('contatos.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Jose - 7392146798')

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    nomes = arquivo.read()
    arquivo.seek(0)
    nomes_lista = arquivo.readlines()
    print(nomes)
    print(nomes_lista) #estou colocando cada linha do arquivo em uma lista
#se eu colocar 'r+' posso ler e escrever e w+ cria um arquivo se não tiver, diferente do outro. 
#se print vai ver que não tem nada na lista porque o cursor foi para o final do arquivo 
#para fazer o ponteiro mostrar tem que colocar arquivo.seek(0)