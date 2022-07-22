import PySimpleGUI as sg
from Candidato import Candidato

class Urna():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, menu_layout):
        self.lista_candidatos = [candidato1, candidato2, candidato3, candidato4]
        roda_urna(self, menu_layout)
    
def roda_urna(urna, window):
    iteracao_urna_quiz(window, 0)
    
    while True:
        eventos, valores = window.read()
        print(eventos, valores)

        if eventos == '-CONFIRMA-':
            voto = valores['-NUMERO_CANDIDATO-']
        if verificacaoVoto(voto) == False:
            window['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red')

        elif verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto)) == False:
            window['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red')

        else:
            window['-VOTAR-'].update(visible=False)
            window['-VOTO_CONFIRMADO-'].update(voto)
            window['-CONFIRMADO-'].update(visible=True)

        if eventos == '-BACK_TO_MENU-' or eventos =='-BACK_TO_MENU-0':
            iteracao_urna_quiz(1)

        if eventos == sg.WINDOW_CLOSED:
            break

        window.close()
        
def verificacaoVoto(voto: str):
      return voto.isdigit()

def verificaNumeroCandidatoExiste(listaCandidatos, voto):
  for candidato in listaCandidatos:
    if voto == candidato.numero:
      return True

  return False

def iteracao_urna_quiz(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-URNA_LY-'].update(visible=True)
    elif troca == 1:
        window['-MENU_LY-'].update(visible=True)
        window['-URNA_LY-'].update(visible=False)
        window['-URNA_LY_FIM-'].update(visible=False)