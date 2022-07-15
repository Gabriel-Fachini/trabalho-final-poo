from Candidato import Candidato
import random

def funcionalidade1(listaCandidatos: list):
  voto = -1
  encontrado = False
  while encontrado != True:
    voto = int(input('Digite o código do candidato que deseja:\n'))
    for candidato in listaCandidatos:
      if candidato.numero == voto:
        confirmacao = None
        confirmacao = input('Você digitou o número do candidato {}. Deseja confirmar seu voto ?\nPara confirmar digite \'sim\' ou \'nao\'\n'.format(candidato.nome))
        if confirmacao == 'sim':
          candidato.numeroVotos = candidato.numeroVotos + 1
        encontrado = True

    if encontrado == False:
      print('Candidato não encontrado, por favor digite um número válido.')

  print('Voto registrado com sucesso!')

def funcionalidade2(listaCandidatos: list):
  # for pessoa in range(212678954): # População do brasil
  for pessoa in range(1000):
    index = random.randrange(0, 5)
    listaCandidatos[index].numeroVotos = listaCandidatos[index].numeroVotos + 1

  maiorNumeroDeVotos = 0
  for candidato in listaCandidatos:
    if candidato.numeroVotos > maiorNumeroDeVotos:
      maiorNumeroDeVotos = candidato.numeroVotos

  vencedores = []
  for candidato in listaCandidatos:
    if candidato.numeroVotos == maiorNumeroDeVotos:
      vencedores.append(candidato)

  if len(vencedores) > 1:
    print('Houve um empate! Empataram os candidatos:')
    for candidato in vencedores:
      print(candidato)
  else:
    print('O vencedor foi:')
    print(vencedores[0])


def funcionalidade3(listaCandidatos: list):
  for candidato in listaCandidatos:
    print(candidato)

def main ():
  listaCandidatos = []
  listaCandidatos.append(Candidato('gabriel', 21, 'PT', 1313, []))
  listaCandidatos.append(Candidato('fulano', 58, 'PSDB', 1548, []))
  listaCandidatos.append(Candidato('arnaldo', 46, 'PL', 1365, []))
  listaCandidatos.append(Candidato('renan', 47, 'PCB', 1457, []))
  listaCandidatos.append(Candidato('luiz', 63, 'PLB', 1652, []))
  listaCandidatos.append(Candidato('alvaro', 67, 'PT', 1495, []))

  opcao = 0
  while opcao != 5:
    print('1- Realizar simulação de votação')
    print('2- Realizar simulação de votação com dados aleatórios')
    print('3- Ver informações de todos os candidatos')
    print('4- Quizz candidatos')
    print('5- Sair')
    opcao = int(input('Digite o número correspondente a opção que deseja:\n'))

    if opcao == 1:
      funcionalidade1(listaCandidatos)

    if opcao == 2:
      funcionalidade2(listaCandidatos)

    if opcao == 3:
      funcionalidade3(listaCandidatos)

main()