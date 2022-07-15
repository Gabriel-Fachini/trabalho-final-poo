import PySimpleGUI as sg

TAMANHO_DE_TELA = (1350, 500)
COR_DE_FUNDO = 'black'

sg.theme('Dark Blue 4')

def volta_menu(window):
    window['-MAIN_MENU-'].update(visible=True)
    window['-GAME-'].update(visible=False)

def menu_inicial():
    
    layout_interno = [[sg.Graph(TAMANHO_DE_TELA,
                        (0, TAMANHO_DE_TELA[1]),
                        (TAMANHO_DE_TELA[0], 0),
                        background_color=COR_DE_FUNDO,
                        key='-GRAPH-')],
                     [sg.Button('Voltar ao Menu', key="-MENU-")]]
    
    layout_menu = [[sg.Text("Simulador de Urna Eletrônica", font="Courier 40")],
                   #[sg.Image(r"C:\Users\Gusta\OneDrive\Área de Trabalho\P.O.O\Proj_Final\src\assets\foto_urna.png")],
                        [sg.Text("", font="Courier 12")],
                        [sg.Text("-- Instruções de uso --", font="Courier 25", size =(None,2))],
                        [sg.Text("Aperte em 'URNA REAL' para simular uma votação com 30 pessoas", font="Courier 15", size =(None,2))],
                        [sg.Text("Aperte em 'SIMULAÇÃO DE VOTOS' para simular votos de 5 cidades diferentes aleatoriamente de maneira automática", font="Courier 15", size =(None,2))],
                        [sg.Text("Aperte em 'QUIZ' para responder a um quiz que, ao final, indicará qual o candidato que mais tem a ver com você", font="Courier 15", size =(None,3))],
                        [sg.Button("URNA REAL", key='-VOTO_UNICO-', font="Courier 24"),
                        sg.Button("SIMULAÇÃO DE VOTOS", key='-SIMULA_VOTOS-', font="Courier 24"),
                        sg.Button("QUIZ", key='-QUIZ-', font="Courier 24"),
                        sg.Button('SAIR', key='-QUIT-', font="Courier 24")]]
    
    layout = [[sg.pin(sg.Column(layout_menu, key='-MAIN_MENU-', size=TAMANHO_DE_TELA, element_justification='center')),
               sg.pin(sg.Column(layout_interno, key='-LY_MAIN_MENU-', visible=False))]]

    window = sg.Window('Simulador de Urna Eletrônica', layout, finalize=True, sbar_relief=True)
    
    while True:
        event, values = window.read()
        #print(event, values)
        #if event == ''
        if event == sg.WIN_CLOSED or event == '-QUIT-':
            break
        
    window.close()
    
menu_inicial()