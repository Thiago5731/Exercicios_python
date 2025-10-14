#Agenda de Contatos em JSON
#CRUD (criar, ler, atualizar e deletar contatos) salvando em arquivo .json.
#Aprendizado: manipulação de arquivos, dicionários e listas.

#para abrir arqivos json no python
"""with open("contatos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
"""
#para importar a biblioteca json e trabalhar com ela. 
import json

dados_json = """{
"catalogo": [
  {
    "nome": "Carla Menezes",
    "idade": 28,
    "telefone": "(11) 98234-5567"
  },
  {
    "nome": "João Pedro Silveira",
    "idade": 34,
    "telefone": "(21) 97588-1209"
  },
  {
    "nome": "Lucas Andrade",
    "idade": 22,
    "telefone": "(31) 99876-4432"
  },
  {
    "nome": "Fernanda Rocha",
    "idade": 30,
    "telefone": "(41) 98455-0033"
  },
  {
    "nome": "Marcos Vinícius Lima",
    "idade": 40,
    "telefone": "(51) 99122-8754"
  },
  {
    "nome": "Patrícia Gomes",
    "idade": 26,
    "telefone": "(71) 98777-4455"
  },
  {
    "nome": "Ricardo Azevedo",
    "idade": 38,
    "telefone": "(85) 99988-6677"
  },
  {
    "nome": "Sabrina Tavares",
    "idade": 24,
    "telefone": "(61) 99211-5599"
  }
]
}
"""

dados = json.loads(dados_json)
for usuarios in dados['catalogo']:
  #posso editar aqui o print para mudar as coisas usuarios['nomes']
  print(usuarios)

#importante. Para manipular qualquer arquivo que seja em json primeiro temos que converter para python. No caso desse exercicio fiz 
#localmente convertendo para um dicionario no proximo vou fazer um exercicio de abrir arquivos com with open. Então depois disso vou
#voltar para manipulação de json