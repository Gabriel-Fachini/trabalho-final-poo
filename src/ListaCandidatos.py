import PySimpleGUI as sg
from Candidato import Candidato
TAMANHO_DE_TELA = (1300, 500)

class ListaCandidatos():
  def __init__(self, candidato1, candidato2, candidato3, candidato4, window):
    self.lista_candidatos = [candidato1, candidato2, candidato3, candidato4]
    rodaLista(self.lista_candidatos, window)

def mudaCandidato(index: int, window, listaCandidatos):
  window['NOME'].update(listaCandidatos[index].nome)
  window['IDADE'].update(listaCandidatos[index].idade)
  window['PARTIDO'].update(listaCandidatos[index].partido)
  window['NUMERO'].update(listaCandidatos[index].numero)
  window['P1'].update(listaCandidatos[index].propostas[0])
  window['P2'].update(listaCandidatos[index].propostas[1])
  window['P3'].update(listaCandidatos[index].propostas[2])

def iteracaoMenu(window, opcao):
  if opcao == 0:
    window['-MENU_LY-'].update(visible=False)
    window['-LISTA_CANDIDATOS-'].update(visible=True)

  if opcao == 1:
    window['-MENU_LY-'].update(visible=True)
    window['-LISTA_CANDIDATOS-'].update(visible=False)

def rodaLista(listaCandidatos, window):
  iteracaoMenu(window, 0)

  pagina = 0
  mudaCandidato(0, window, listaCandidatos)
  while True:
    eventos, valores = window.read()
    if eventos == '-ANT-':
      if pagina == 0:
        pagina = 3
      else:
        pagina = pagina - 1
      mudaCandidato(pagina, window, listaCandidatos)

    if eventos == '-PROX-':
      pagina = (pagina + 1) % 4
      mudaCandidato(pagina, window, listaCandidatos)

    if eventos == '-BACK_TO_MENU-' or eventos =='-BACK_TO_MENU-0':
      iteracaoMenu(window, 1)
      break

    if eventos == sg.WINDOW_CLOSED:
      break

  window.close()