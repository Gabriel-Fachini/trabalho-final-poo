import PySimpleGUI as sg
from Quiz import Quiz
#from Urna import Urna
from Candidato import Candidato

TAMANHO_DE_TELA = (1190, 700)
COR_DE_FUNDO = 'black'

sg.theme('GreenMono')

def volta_menu(window):
    window['-MAIN_MENU-'].update(visible=True)
    window['-GAME-'].update(visible=False)

def menu_inicial():
    
    layout_interno = [[sg.Graph(TAMANHO_DE_TELA,
                        (0, TAMANHO_DE_TELA[1]),
                        (TAMANHO_DE_TELA[0], 0),
                        background_color=COR_DE_FUNDO,
                        key='-GRAPH-')]]
                     #[sg.Button('Voltar ao Menu', key="-MENU-")]]
    
    layout_menu = [[sg.Text("Simulador de Urna Eletrônica", font="Courier 40", size=(None, 2))],
                   #[sg.Image(r"C:\Users\Gusta\OneDrive\Área de Trabalho\P.O.O\Proj_Final\src\assets\foto_urna.png")],
                        [sg.Text("-- Instruções de uso --", font="Courier 25", size =(None,2))],
                        [sg.Text("Aperte em 'URNA REAL' para simular uma votação real para o próximo", font="Courier 20", size =(None,1))],
                        [sg.Text("presidente do Brasil.", font="Courier 20", size =(None,2))],
                        [sg.Text("Aperte em 'SIMULAÇÃO DE VOTOS' para simular votos de 5 cidades diferentes", font="Courier 20", size =(None,1))],
                        [sg.Text("aleatoriamente de maneira automática.", font="Courier 20", size =(None,2))],
                        [sg.Text("Aperte em 'QUIZ' para responder a um questionário que, ao final, indicará", font="Courier 20", size =(None,1))],
                        [sg.Text("qual o candidato que mais combina com você", font="Courier 20", size =(None,3))],
                        [sg.Button("URNA REAL", key='-VOTO_UNICO-', font="Courier 24"),
                        sg.Button("SIMULAÇÃO DE VOTOS", key='-SIMULA_VOTOS-', font="Courier 24"),
                        sg.Button("QUIZ", key='-QUIZ-', font="Courier 24"),
                        sg.Button('SAIR', key='-QUIT-', font="Courier 24")],
                        [sg.Text("", size=(None, 2))]]
    
    layout = [[sg.pin(sg.Column(layout_menu, key='-MAIN_MENU-', size=TAMANHO_DE_TELA, element_justification='center')),
               sg.pin(sg.Column(layout_interno, key='-LY_MAIN_MENU-', visible=False))]]

    window = sg.Window('Simulador de Urna Eletrônica', layout, finalize=True, enable_close_attempted_event=True)
    
    #Criacao de candidatos
    candidato1 = Candidato("Jessica Matos", 35, "Partido dos Negacionistas Gigantes (PNG)", 14, 
                           ["Acabar com faculdades públicas", 
                            "Vacinas não poderão ser exigidas em locais públicos e/ou privados", 
                            "Apoio federal para pessoas com mais de 1.95 de altura"])
    
    candidato2 = Candidato("Matheus Bragança", 43, "Partido dos Lavadores Aquafóbicos (PLA)", 19,
                           ["Diminuição de impostos nas lavagens a seco",
                            "Aumento dos impostos na água",
                            "Multa de R$3523,24 para quem for flagrado tomando mais de um banho por semana"])
    
    candidato3 = Candidato("Jefferson Moreira", 42, "Partido dos Adoradores de Tênis de Mesa", 12,
                           ["Tênis de mesa em cada escola pública é lei",
                            "Bolsa Raquete para cargos públicos", 
                            "Taxas de importação de madeira caem 49%"])
    
    candidato4 = Candidato("Roberto Autônomo", 51, "Partido dos Idealizadores Atômicos", 16,
                           ["Brasil entrará no Tratado Urgente para Proliferação de Armas Nucleares (TUPAN) imediatamente",
                            "Investimento de 78%/ do PIB Brasileiro em armas nucleares",
                            "Curso básico de atomística será exigido para entrada na escola infantil e fundamental"])
    
    #Inicio dos eventos da janela inicial
    while True:
        event, values = window.read()
        if event == '-QUIZ-':
            window['-MAIN_MENU-'].update(visible=False)
            window['-LY_MAIN_MENU-'].update(visible=True)
            Quiz(candidato1, candidato2, candidato3, candidato4, TAMANHO_DE_TELA, COR_DE_FUNDO)
        if (event == sg.WIN_CLOSED or event == '-QUIT-') and sg.popup_yes_no('Você realmente deseja sair?') == 'Yes':
            break
        
    window.close()
    
menu_inicial()