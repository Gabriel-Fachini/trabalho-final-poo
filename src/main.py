from Candidato import Candidato

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

    if opcao == 3:
      funcionalidade3(listaCandidatos)

main()