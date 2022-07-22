from pydoc import visiblename
import PySimpleGUI as sg
from Candidato import Candidato

class Urna():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, window):
        self.lista_candidatos = [candidato1, candidato2, candidato3, candidato4]
        roda_urna(self, window)
    
def roda_urna(urna, window):
    iteracao_urna_menu(window, 0)
    
    voto = ''
    aux = 0
    
    while True:
        eventos, valores = window.read()
        print(eventos, valores)

        if eventos == '-CONFIRMA-':
            voto = valores['-NUMERO_CANDIDATO-1']
            if verificacaoVoto(voto) == False:
                window['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red', visible=True)

            elif verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto)) == False:
                window['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red', visible=True)

            else:
                candidato = verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto))
                window['-NOME_CANDIDATO_FINAL-'].update(candidato.nome)
                window['-IDADE_CANDIDATO_FINAL-'].update(candidato.numero)
                window['-P1_CANDIDATO_URNA_FINAL-'].update(candidato.propostas[0])
                window['-P2_CANDIDATO_URNA_FINAL-'].update(candidato.propostas[1])
                window['-P3_CANDIDATO_URNA_FINAL-'].update(candidato.propostas[2])
                window['-URNA_LY-'].update(visible=False)
                window['-URNA_LY_FIM-'].update(visible=True)
                
        if eventos == '-VE_CANDIDATO-':
            voto = valores['-NUMERO_CANDIDATO-1']
            if verificacaoVoto(voto) == False:
                window['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red', visible=True)
            elif verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto)) == False:
                window['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red', visible=True)
            else:
                candidato = verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto))
                window['-ERRO_VOTO-'].update(visible=False)
                atualiza_candidato(window, 0)
                window['-NOME_CANDIDATO_URNA-'].update(candidato.nome)
                window['-IDADE_CANDIDATO_URNA-'].update(candidato.idade)
                window['-NUMERO_CANDIDATO_URNA-'].update(candidato.numero)
                window['-P1_CANDIDATO_URNA-'].update(candidato.propostas[0])
                window['-P2_CANDIDATO_URNA-'].update(candidato.propostas[1])
                window['-P3_CANDIDATO_URNA-'].update(candidato.propostas[2])
                
        if eventos == '-VOLTA_URNA-':
            iteracao_urna_candidato(window)
                    
        if eventos == '-VOLTA_MENU-' or eventos =='-VOLTA_MENU-3' or eventos == '-VOLTA_MENU-4' or eventos == '-VOLTA_MENU-5':
            iteracao_urna_menu(window, 1)
            break

        if eventos == sg.WINDOW_CLOSED:
            aux = 1
            break

    if aux == 1:
        window.close()
        
def verificacaoVoto(voto):
      return voto.isdigit()

def verificaNumeroCandidatoExiste(listaCandidatos, voto):
  for candidato in listaCandidatos:
    if voto == candidato.numero:
        return candidato

  return False


def iteracao_urna_menu(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-URNA_LY-'].update(visible=True)
    elif troca == 1:
        window['-MENU_LY-'].update(visible=True)
        window['-URNA_LY-'].update(visible=False)
        window['-URNA_LY_FIM-'].update(visible=False)
        window['-URNA_LY_CANDIDATO-'].update(visible=False)
        
def iteracao_urna_candidato(window):
    window['-URNA_LY_CANDIDATO-'].update(visible=False)
    window['-URNA_LY-'].update(visible=True)
        
def atualiza_candidato(window, troca):
    if troca == 0:
        window['-URNA_LY-'].update(visible=False)
        window['-URNA_LY_CANDIDATO-'].update(visible=True)
    elif troca == 1:
        window['-URNA_LY_CANDIDATO-'].update(visible=True)
        window['-URNA_LY-'].update(visible=False)