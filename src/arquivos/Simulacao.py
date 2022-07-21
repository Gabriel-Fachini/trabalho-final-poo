import PySimpleGUI as sg
TAMANHO_DE_TELA = (1000, 500)

class Simulacao:
  def rodaSimulacao(TAMANHO_DE_TELA):
    layout_interno = [[sg.Graph(TAMANHO_DE_TELA,
                        (0, TAMANHO_DE_TELA[1]),
                        (TAMANHO_DE_TELA[0], 0),
                        key='-GRAPH-')]]

    #Comecando da primeira pergunta
    first_layout = [
      [sg.Text('Para simular a votação, basta apertar', font="Courier 34", size =(None,1))],
      [sg.Text('o botão:', font="Courier 34", size =(None,1))],
      [sg.Button('Iniciar', key='-INICIAR-', font="Courier 24", tooltip='Aperte aqui para confirmar seu voto')],
    ]

    layout = [[sg.pin(sg.Column(first_layout, key='-FIRST_LAYOUT-', size=TAMANHO_DE_TELA, element_justification='center', expand_x=True)),
            sg.pin(sg.Column(layout_interno, key='-LAYOUT_INTERNO-', visible=False))]]

    window = sg.Window('Simulador de Urna Eletrônica - QUIZ', layout, finalize=True, enable_close_attempted_event=True)

    window.bind("<Key>", "+KEY+")
    window.bind("<KeyRelease>", "-KEY-")

    graph_elem = window['-GRAPH-']

    while True:
        event, values = window.read()
        if event == '-POSITIVO-':
            pass
        if event == 'NEGATIVO':
            pass
        if event == 'NEUTRO':
            pass
        if event == 'N_S_R':
            pass
        # if event == '-BACK_TO_MENU-' and sg.popup_yes_no('Você realmente deseja voltar?') == 'Yes':
        #     volta_menu(window)

        if (event == sg.WIN_CLOSED) and sg.popup_yes_no('Você realemnte deseja sair?') == 'Yes':
            window.close()

    #for i in range(quiz.nmr_de_perguntas):
       # pergunta = quiz.perguntas[i]
       # print(pergunta)
        #somar respostas 'sim'