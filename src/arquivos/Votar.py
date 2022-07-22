import PySimpleGUI as sg
from Candidato import Candidato
TAMANHO_DE_TELA = (1000, 500)

def verificacaoVoto(voto: str) -> bool:
  return voto.isdigit()

def verificaNumeroCandidatoExiste(listaCandidatos: list, voto: int) -> bool:
  for candidato in listaCandidatos:
    if voto == candidato.numero:
      return True

  return False

class Votar:
  def rodaVotacao(quiz, TAMANHO_DE_TELA, COR_DE_FUNDO):
    layout_interno = [[sg.Graph(TAMANHO_DE_TELA,
                        (0, TAMANHO_DE_TELA[1]),
                        (TAMANHO_DE_TELA[0], 0),
                        key='-GRAPH-')]]

    #Comecando da primeira pergunta
    first_layout = [
      [sg.Text('Digite o número do candidato', font="Courier 34", size =(None,1))],
      [sg.Text('que deseja votar:', font="Courier 34", size =(None,1))],
      [sg.Input(key='-NUMERO_CANDIDATO-')],
      [sg.Button('Confirma', key='-CONFIRMA-', font="Courier 24", tooltip='Aperte aqui para confirmar seu voto')],
      [sg.Text("", size=(None, 2))],
      [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-BACK_TO_MENU-', font="Courier 24")],
      [sg.Text("", size=(None, 2))]
    ]

    layout = [[sg.pin(sg.Column(first_layout, key='-FIRST_LAYOUT-', size=TAMANHO_DE_TELA, element_justification='center', expand_x=True)),
            sg.pin(sg.Column(layout_interno, key='-LAYOUT_INTERNO-', visible=False))]]

    window = sg.Window('Simulador de Urna Eletrônica - QUIZ', layout, finalize=True, enable_close_attempted_event=True)

    window.bind("<Key>", "+KEY+")
    window.bind("<KeyRelease>", "-KEY-")

    graph_elem = window['-GRAPH-']

    while True:
        event, values = window.read()
        print(event)
        print(values)

        if event == '-BACK_TO_MENU-' and sg.popup_yes_no('Você realmente deseja voltar?') == 'Yes':
          volta_menu(window)
        elif event == sg.WIN_CLOSED:
          print("Entrei_sair 3")
          break

def main():
  sg.theme('Dark Blue 3')
  voto = ''

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

  votarLayout = [
      [sg.Text('Digite o número do candidato', font="Courier 34", size =(None,1))],
      [sg.Text('que deseja votar:', font="Courier 34", size =(None,1))],
      [sg.Text('', key='-ERRO_VOTO-', font="Courier 18", text_color='white')],
      [sg.Input(key='-NUMERO_CANDIDATO-', font="Courier 24", size=(8, 20))],
      [sg.Text('', key='-ERRO_VOTO-', font="Courier 18", text_color='white')],
      [sg.Button('Confirma', key='-CONFIRMA-', font="Courier 24", tooltip='Aperte aqui para confirmar seu voto')],
      [sg.Text("", size=(None, 2))],
      [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-BACK_TO_MENU-', font="Courier 24")],
      [sg.Text("", size=(None, 2))]
  ]

  mostrarConfirmacaoLayout = [
    [sg.Text('Votação finalizada', font="Courier 24")],
    [sg.Text("", size=(None, 2))],
    [sg.Text('', key='-VOTO_CONFIRMADO-', font="Courier 48")],
    [sg.Text("", size=(None, 2))],
    [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-BACK_TO_MENU-', font="Courier 24")],
    [sg.Text("", size=(None, 2))]
  ]

  layoutFinal = [
    [
      sg.pin(sg.Column(votarLayout, key='-VOTAR-', size=TAMANHO_DE_TELA, element_justification='center', expand_x=True)),
      sg.pin(sg.Column(mostrarConfirmacaoLayout, key='-CONFIRMADO-', size=TAMANHO_DE_TELA, element_justification='center', visible=False)),
      sg.pin(sg.Column(layoutInterno, visible=False, element_justification='center'))
    ]
  ]

  janela = sg.Window('Simulador de Urna Eletrônica - VOTAÇÃO', layoutFinal, finalize=True)

  while True:
    eventos, valores = janela.read()

    if eventos == '-CONFIRMA-':
      voto = valores['-NUMERO_CANDIDATO-']
      if verificacaoVoto(voto) == False:
        janela['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red')

      elif verificaNumeroCandidatoExiste(listaCandidatos, int(voto)) == False:
        janela['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red')

      else:
        janela['-VOTAR-'].update(visible=False)
        janela['-VOTO_CONFIRMADO-'].update(voto)
        janela['-CONFIRMADO-'].update(visible=True)

    if eventos == '-BACK_TO_MENU-' or eventos =='-BACK_TO_MENU-0':
      break

    if eventos == sg.WINDOW_CLOSED:
      break

  janela.close()

main()