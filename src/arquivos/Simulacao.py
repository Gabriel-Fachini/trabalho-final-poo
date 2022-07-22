import PySimpleGUI as sg
import random
from Candidato import Candidato
TAMANHO_DE_TELA = (1000, 500)

def simulacaoVotacao(listaCandidatos: list):
  # for pessoa in range(212678954): # População do brasil
  for pessoa in range(1000000):
    index = random.randrange(0, 3)
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
    return None
  else:
    return vencedores[0]

def main():
  sg.theme('Dark Blue 3')

  listaCandidatos = []
  listaCandidatos.append(Candidato("Jessica Matos", 35, "Partido dos Negacionistas Gigantes (PNG)", 14,
                           ["Acabar com faculdades públicas",
                            "Vacinas não poderão ser exigidas em locais públicos e/ou privados",
                            "Apoio federal para pessoas com mais de 1.95 de altura"]))
  listaCandidatos.append(Candidato("Matheus Bragança", 43, "Partido dos Lavadores Aquafóbicos (PLA)", 19,
                           ["Diminuição de impostos nas lavagens a seco",
                            "Aumento dos impostos na água",
                            "Multa de R$3523,24 para quem for flagrado tomando mais de um banho por semana"]))
  listaCandidatos.append(Candidato("Jefferson Moreira", 42, "Partido dos Adoradores de Tênis de Mesa", 12,
                           ["Tênis de mesa em cada escola pública é lei",
                            "Bolsa Raquete para cargos públicos",
                            "Taxas de importação de madeira caem 49%"]))
  listaCandidatos.append(Candidato("Roberto Autônomo", 51, "Partido dos Idealizadores Atômicos", 16,
                           ["Brasil entrará no Tratado Urgente para Proliferação de Armas Nucleares (TUPAN) imediatamente",
                            "Investimento de 78%/ do PIB Brasileiro em armas nucleares",
                            "Curso básico de atomística será exigido para entrada na escola infantil e fundamental"]))

  layoutInterno = [
    [sg.Graph(TAMANHO_DE_TELA,
    (0, TAMANHO_DE_TELA[1]),
    (TAMANHO_DE_TELA[0], 0),
    key='-GRAPH-')]
  ]

  # teste = Image.open("urna.png")
  teste = open('urna.png', 'r')

  layoutIniciarSimulacao = [
    [sg.Image('urna.png', size=(300, 300))],
    [sg.Text('Para simular, aperte em iniciar.', font="Courier 24")],
    [sg.Text("", size=(None, 8))],
    [sg.Button('Iniciar', key='-INICIAR_SIMULACAO-', font="Courier 24")],
    [sg.Text("", size=(None, 8))],
    [sg.Button('<- Voltar', key='-BACK_TO_MENU-', font="Courier 24")]
  ]

  layoutResultadoSimulacao = [
    [sg.Text('Vencedor de uma simulação com 1', font='Courier 36')],
    [sg.Text('milhão de votos aleatórios:', font='Courier 36')],
    [sg.Text("", size=(None, 2))],
    [sg.Text('Nome:', key='-NOME-', font='Courier 24')],
    [sg.Text('Idade:', key='-IDADE-', font='Courier 24')],
    [sg.Text('Numero:',key='-NUMERO-', font='Courier 24')],
    # [sg.Text('Propostas:', key='-PROPOSTAS-',  font='Courier 24')],
    [sg.Text('Numero de votos:', key='-NUMERO_VOTOS-',  font='Courier 24')],
    [sg.Text("", size=(None, 4))],
    [sg.Button('<- Voltar', key='-BACK_TO_MENU-', font="Courier 24")]
  ]

  layoutFinal = [
    [
      sg.pin(sg.Column(layoutIniciarSimulacao, key='-SIMULACAO-', size=(600, 500), element_justification='center', expand_x=True)),
      sg.pin(sg.Column(layoutResultadoSimulacao, key='-RESULTADO-', size=TAMANHO_DE_TELA, element_justification='left', visible=False)),
      sg.pin(sg.Column(layoutInterno, visible=False, element_justification='center'))
    ]
  ]

  janela = sg.Window('Simulador de Urna Eletrônica - SIMULAÇÃO VOTAÇÃO', layoutFinal, finalize=True)

  while True:
    eventos, valores = janela.read()

    if eventos == '-INICIAR_SIMULACAO-':
      janela['-SIMULACAO-'].update(visible=False)
      janela['-RESULTADO-'].update(visible=True)
      vencedor = simulacaoVotacao(listaCandidatos)
      if vencedor != None:
        janela['-NOME-'].update('Nome:' + vencedor.nome)
        janela['-IDADE-'].update('Idade:' + str(vencedor.idade))
        janela['-NUMERO-'].update('Numero:' + str(vencedor.numero))
        # janela['-PROPOSTAS-'].update(vencedor.propostas)
        janela['-NUMERO_VOTOS-'].update('Numero de votos:' + str(vencedor.numeroVotos))


    if eventos == '-BACK_TO_MENU-' or eventos =='-BACK_TO_MENU-0':
      break

    if eventos == sg.WINDOW_CLOSED:
      break

  janela.close()

main()