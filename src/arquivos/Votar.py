import PySimpleGUI as sg
TAMANHO_DE_TELA = (1000, 500)

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
        if event == '-POSITIVO-':
            pass
        if event == 'NEGATIVO':
            pass
        if event == 'NEUTRO':
            pass
        if event == 'N_S_R':
            pass

        if event == '-BACK_TO_MENU-' and sg.popup_yes_no('Você realmente deseja voltar?') == 'Yes':
          volta_menu(window, 0)

        elif event == sg.WIN_CLOSED:
            print("Entrei_sair 3")
            break

def volta_menu(window, troca):
    if troca == 0:
        window['-BACK_TO_MENU-'].update(visible=False)
        window['-GRAPH-'].update(visible=True)
    elif troca == 1:
        window['-BACK_TO_MENU-'].update(visible=True)
        window['-GRAPH-'].update(visible=False)