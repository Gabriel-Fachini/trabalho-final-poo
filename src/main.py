from Candidato import Candidato

def main ():
  teste = Candidato('gabriel', 21, 'PT', 1313, [])
  print(teste)


  print('1- Realizar simulação de votação')
  print('2- Realizar simulação de votação com dados aleatórios')
  print('3- Ver informações de todos os candidatos')
  print('4- Quizz candidatos')
  input('Digite o número correspondente a opção que deseja:\n')

main()