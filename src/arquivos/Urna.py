from pydoc import visiblename
import PySimpleGUI as sg
from Candidato import Candidato

class Urna():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, window):
        self.lista_candidatos = [candidato1, candidato2, candidato3, candidato4]
        roda_urna(self, window)
    
def roda_urna(urna, window):
    iteracao_urna_quiz(window, 0)
    
    voto = ''
    aux = 0
    
    while True:
        eventos, valores = window.read()
        print(eventos, valores)

        if eventos == '-CONFIRMA-':
            print("Entrei if 1")
            voto = valores['-NUMERO_CANDIDATO-1']
            if verificacaoVoto(voto) == False:
                print("Entrei if 2")
                window['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red', visible=True)

            elif verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto)) == False:
                print("Entrei if 3")
                window['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red', visible=True)

            else:
                print("Entrei if 4")
                window['-URNA_LY-'].update(visible=False)
                window['-VOTO_CONFIRMADO-'].update(valores['-NUMERO_CANDIDATO-1'])
                window['-URNA_LY_FIM-'].update(visible=True)
                
        if eventos == '-VE_CANDIDATO-':
            voto = valores['-NUMERO_CANDIDATO-1']
            if verificacaoVoto(voto) == False:
                print("Entrei if 2")
                window['-ERRO_VOTO-'].update('Insira apenas números!', background_color='red', visible=True)
            elif verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto)) == False:
                print("Entrei if 3")
                window['-ERRO_VOTO-'].update('Candidato não encontrado!', background_color='red', visible=True)
            else:
                candidato = verificaNumeroCandidatoExiste(urna.lista_candidatos, int(voto))
                print("Entrei if 9")
                window['-ERRO_VOTO-'].update(visible=False)
                atualiza_candidato(window, 0)
                window['-NOME_CANDIDATO_URNA-'].update(candidato.nome)
                window['-IDADE_CANDIDATO_URNA-'].update(candidato.idade)
                window['-NUMERO_CANDIDATO_URNA-'].update(candidato.numero)
                window['-P1_CANDIDATO_URNA-'].update(candidato.propostas[0])
                window['-P2_CANDIDATO_URNA-'].update(candidato.propostas[1])
                window['-P3_CANDIDATO_URNA-'].update(candidato.propostas[2])
                    
        if eventos == '-VOLTA_MENU-' or eventos =='-VOLTA_MENU-3' or eventos == '-VOLTA_MENU-4':
            print("Entrei if 5")
            iteracao_urna_quiz(window, 1)
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


def iteracao_urna_quiz(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-URNA_LY-'].update(visible=True)
    elif troca == 1:
        window['-MENU_LY-'].update(visible=True)
        window['-URNA_LY-'].update(visible=False)
        window['-URNA_LY_FIM-'].update(visible=False)
        window['-URNA_LY_CANDIDATO-'].update(visible=False)
        
def atualiza_candidato(window, troca):
    if troca == 0:
        window['-URNA_LY-'].update(visible=False)
        window['-URNA_LY_CANDIDATO-'].update(visible=True)
    elif troca == 1:
        window['-URNA_LY_CANDIDATO-'].update(visible=True)
        window['-URNA_LY-'].update(visible=False)