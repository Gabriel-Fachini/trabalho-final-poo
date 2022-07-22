import PySimpleGUI as sg
import datetime
from Candidato import Candidato
from Quiz import Quiz
from Urna import Urna

TAMANHO_DE_TELA_MENU = (1190, 700)
TAMANHO_DE_TELA_QUIZ = (900, 350)
TAMANHO_DE_TELA_QUIZ_FINAL = (900, 450)
TAMANHO_DE_TELA_URNA = (800, 600)

sg.theme('GreenMono')

def main():
    sleep_time = 10
    
    # Criacao de layouts
    layout_quiz = [[sg.Text("", font="Courier 35", size=(None, 1), key='-NMR_PERGUNTA-')],
                    [sg.Text("", font="Courier 20", size =(56,2), key='-TEXTO_PERGUNTA-')],
                    [sg.Button("POSITIVO", key='-POSITIVO-', font="Courier 24"),
                    sg.Button("NEUTRO", key='-NEUTRO-', font="Courier 24"),
                    sg.Button("NEGATIVO", key='-NEGATIVO-', font="Courier 24"),
                    sg.Button("MUITO NEGATIVO", key='-MUITO_NEGATIVO-', font="Courier 24")],
                    [sg.Text("", size=(None, 2))],
                    [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-VOLTA_MENU-', font="Courier 24", auto_size_button=True, button_color='#3065ac')],
                    [sg.Text("", size=(None, 2))]]
    
    layout_quiz_fim = [[sg.Text("Você deu match com: ", font="Courier 30", size=(None, 1)), sg.Text("", font="Courier 30", size=(None, 1), key='-NOME_CANDIDATO-')],
                    [sg.Text("", font="Courier 20", size =(55,6), key='-TEXTO_CANDIDATO-'), sg.Text("VOTE", font="Courier 25", size =(None,1))],
                    [sg.Text("Para apoiar, vote:", font="Courier 25", size =(None,1)), sg.Text("", font="Courier 25", size =(None,1), key='-NUMERO_CANDIDATO-')],
                    [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-VOLTA_MENU-', font="Courier 24", auto_size_button=True, button_color='#3065ac'), sg.Image(source="", size=(50,70),key='-FOTO_CANDIDATO-')],
                    [sg.Text("", size=(None, 1))]]
    
    layout_urna = [
      [sg.Text('Digite o número do candidato', font="Courier 34", size =(None,1))],
      [sg.Text('que deseja votar:', font="Courier 34", size =(None,1))],
      [sg.Text('', key='-ERRO_VOTO-', font="Courier 18", text_color='white')],
      [sg.Input(key='-NUMERO_CANDIDATO-', font="Courier 24", size=(8, 20))],
      [sg.Text('', key='-ERRO_VOTO-', font="Courier 18", text_color='white')],
      [sg.Button('Confirma', key='-CONFIRMA-', font="Courier 24", tooltip='Aperte aqui para confirmar seu voto')],
      [sg.Text("", size=(None, 2))],
      [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-VOLTA_MENU-', font="Courier 24", auto_size_button=True, button_color='#3065ac')],
      [sg.Text("", size=(None, 2))]
    ]
    
    layout_urna_confirmacao = [
        [sg.Text('Votação finalizada', font="Courier 24")],
        [sg.Text("", size=(None, 2))],
        [sg.Text('', key='-VOTO_CONFIRMADO-', font="Courier 48")],
        [sg.Text("", size=(None, 2))],
        [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-BACK_TO_MENU-', font="Courier 24")],
        [sg.Text("", size=(None, 2))]
    ]
    
    #layout_simulacao = []
    
    layout_menu_inicial = [[sg.Text("Simulador de Urna Eletrônica", font="Courier 40", size=(None, 1))],
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
    
    layout = [[sg.pin(sg.Column(layout_menu_inicial, key='-MENU_LY-', size=TAMANHO_DE_TELA_MENU, element_justification='center')),
               sg.pin(sg.Column(layout_quiz, key='-QUIZ_LY-', size=TAMANHO_DE_TELA_QUIZ, element_justification='left', visible=False, expand_x=True, expand_y=True)),
               sg.pin(sg.Column(layout_quiz_fim, key='-QUIZ_LY_FIM-', size=TAMANHO_DE_TELA_QUIZ_FINAL, element_justification='left', visible=False, expand_x=True, expand_y=True)),
               sg.pin(sg.Column(layout_urna, key='-URNA_LY-', size=TAMANHO_DE_TELA_URNA, element_justification='center', visible=False, expand_x=True, expand_y=True)),
               sg.pin(sg.Column(layout_urna_confirmacao, key='-URNA_LY_FIM-', size=TAMANHO_DE_TELA_URNA, element_justification='center', visible=False, expand_x=True, expand_y=True))]]
               #sg.pin(sg.Column(layout_simulacao, key='-SIMULACAO_LY-', size=TAMANHO_DE_TELA, element_justification='center', visible=False))]]

    window = sg.Window('Simulador de Urna Eletrônica', layout, finalize=True)
    
    #Criacao de candidatos
    candidato1 = Candidato("Jessica Matos", 35, "Partido dos Negacionistas Gigantes (PNG)", 14, 
                           ["Acabar com faculdades públicas", 
                            "Vacinas não poderão ser exigidas em locais públicos e/ou privados", 
                            "Apoio federal para pessoas com mais de 1.95 de altura"])
    
    candidato2 = Candidato("Matheus Bragança", 43, "Partido dos Lavadores Aquafóbicos (PLA)", 19,
                           ["Diminuição de impostos nas lavagens a seco",
                            "Aumento dos impostos na água",
                            "Multa de R$3523,24 para quem for flagrado tomando mais de um banho por semana"])
    
    candidato3 = Candidato("Jefferson Moreira", 42, "Partido dos Adoradores de Tênis de Mesa (PATM)", 12,
                           ["Tênis de mesa em cada escola pública é lei",
                            "Bolsa Raquete para cargos públicos", 
                            "Taxas de importação de madeira caem 49%"])
    
    candidato4 = Candidato("Roberto Autônomo", 51, "Partido dos Idealizadores Atômicos (PIA)", 16,
                           ["Brasil entrará no Tratado Urgente para Proliferação de Armas Nucleares (TUPAN) imediatamente",
                            "Investimento de 78%/ do PIB Brasileiro em armas nucleares",
                            "Curso básico de atomística será exigido para entrada na escola infantil e fundamental"])
    
    start = datetime.datetime.now()
    last_post_read_time = start
    
    #Inicio dos eventos da janela inicial
    while True:
        pre_read_time = datetime.datetime.now()
        processing_time = (pre_read_time - last_post_read_time).total_seconds()
        time_to_sleep = sleep_time - int(processing_time*1000)
        time_to_sleep = max(time_to_sleep, 0)
        
        event, values = window.read(time_to_sleep)
        if event == '-QUIZ-':
            Quiz(candidato1, candidato2, candidato3, candidato4, window)
        elif event == '-VOTO_UNICO-':
            Urna(candidato1, candidato2, candidato3, candidato4, window)
        elif event == sg.WIN_CLOSED or event == '-QUIT-':
            break
        
    window.close()

if __name__ == '__main__':
    main()