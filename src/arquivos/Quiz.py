import PySimpleGUI as sg
#from menu_inicial import menu_inicial
#from Candidato import Candidato

TAMANHO_DE_TELA = (1000, 500)
#COR_DE_FUNDO = 'black'

class Quiz():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, TAMANHO_DE_TELA, COR_DE_FUNDO):
        self.candidato1 = candidato1
        self.pontos_cand_1 = 0
        self.texto_cand_1 = cria_texto_candidato(1)
        
        self.candidato2 = candidato2
        self.pontos_cand_2 = 0
        self.texto_cand_2 = cria_texto_candidato(2)
        
        self.candidato3 = candidato3
        self.pontos_cand_3 = 0
        self.texto_cand_3 = cria_texto_candidato(3)
        
        self.candidato4 = candidato4
        self.pontos_cand_4 = 0
        self.texto_cand_4 = cria_texto_candidato(4)
        
        self.nmr_de_perguntas = 10
        self.texto_perguntas = armazena_perguntas()
        self.nmr_pergunta = armazena_texto_nmr_pergunta()
        
        roda_quiz(self, TAMANHO_DE_TELA, COR_DE_FUNDO)
        
        
def cria_texto_candidato(nmr_candidato):
        if nmr_candidato == 1:
            pass
        elif nmr_candidato == 2:
            pass
        elif nmr_candidato == 3:
            pass
        elif nmr_candidato == 4:
            pass
        else:
            print("Numero de candidato invalido")
    
def armazena_perguntas():
    perguntas = [
        "Q1. O que você acha da atual situação do país?",
        "Q2. Você concorda que o esporte é essencial para todos?",
        "Q3. Você concorda com a política internacional do Brasil diante as guerras?",
        "Q4. Você concorda que a falta de água é um problema crítico e mundial?",
        "Q5. Você costuma tomar muitos banhos na semana?",
        "Q6. Você concorda que a ciência deve ser o cerne do ensino público?",
        "Q7. Você concorda que o as universidades públicas servem para balbúrida dos estudantes?",
        "Q8. Você possui mais de 1,95 de altura?",
        "Q9. Você acha as taxas de importações abusivas?",
        "Q10. Você concorda que o governo se intromete demais em nossas vidas?",
    ]
    return perguntas 

def armazena_texto_nmr_pergunta():
    nmr_pergunta = [
        "---> Questão 1 <---",
        "---> Questão 2 <---",
        "---> Questão 3 <---",
        "---> Questão 4 <---",
        "---> Questão 5 <---",
        "---> Questão 6 <---",
        "---> Questão 7 <---",
        "---> Questão 8 <---",
        "---> Questão 9 <---",
        "---> Questão 10 <---",
    ]
    return nmr_pergunta 

def volta_menu(window):
    window['-FIRST_LAYOUT-'].update(visible=True)
    window['-LAYOUT_INTERNO-'].update(visible=False)

def roda_quiz(quiz, TAMANHO_DE_TELA, COR_DE_FUNDO):
    layout_interno = [[sg.Graph(TAMANHO_DE_TELA,
                        (0, TAMANHO_DE_TELA[1]),
                        (TAMANHO_DE_TELA[0], 0),
                        key='-GRAPH-')]]
                    
    #Comecando da primeira pergunta
    pergunta_atual = 0
    first_layout = [[sg.Text(quiz.nmr_pergunta[pergunta_atual], font="Courier 40", size=(None, 2), expand_x=True)],
                    [sg.Text(quiz.texto_perguntas[pergunta_atual], font="Courier 20", size =(None,1))],
                    [sg.Button("POSITIVO", key='-POSITIVO-', font="Courier 24"),
                    sg.Button("NEGATIVO", key='-NEGATIVO-', font="Courier 24"),
                    sg.Button("NEUTRO", key='-NEUTRO-', font="Courier 24"),
                    sg.Button("NÃO SEI RESPONDER", key='-N_S_R-', font="Courier 24")],
                    [sg.Text("", size=(None, 2))],
                    [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-BACK_TO_MENU-', font="Courier 24")],
                    [sg.Text("", size=(None, 2))]]
    
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
        if event == '-BACK_TO_MENU-' and sg.popup_yes_no('Você realmente deseja voltar?') == 'Yes':
            volta_menu(window)
            
        if (event == sg.WIN_CLOSED) and sg.popup_yes_no('Você realemnte deseja sair?') == 'Yes':
            window.close()
        
    #for i in range(quiz.nmr_de_perguntas):
       # pergunta = quiz.perguntas[i]
       # print(pergunta)
        #somar respostas 'sim'
    


    
    
