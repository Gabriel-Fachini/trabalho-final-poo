import PySimpleGUI as sg
import datetime
from PIL import Image, ImageTk

from sympy import content

TAMANHO_DE_TELA_MENU = (1190, 700)
TAMANHO_DE_TELA_QUIZ = (900, 350)
TAMANHO_DE_TELA_QUIZ_FINAL = (900, 450)

sg.theme('GreenMono')

class Candidato():
    
  def __init__(self, nome: str, idade: int, partido: str, numero: int, propostas: list):
    self.nome = nome
    self.idade = idade
    self.partido = partido
    self.numero = numero
    self.propostas = propostas
    self.numeroVotos = 0
    
  def adicionarVoto(self):
    self.numeroVotos = self.numeroVotos + 1
    
  def __str__(self) -> str:
        return '''
    -------------------------------------------
    Candidato {}:\n
    Idade: {}\n
    Partido: {}\n
    Numero: {}\n
    Propostas: {}\n
    -------------------------------------------
    '''.format(self.nome, self.idade, self.partido, self.numero, self.propostas)


#1 - Jessica, 2 - Matheus, 3 - Jefferson, 4 - Roberto
class Quiz():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, menu_layout):
        self.candidato_1 = candidato1
        self.pontos_cand_1 = 0
        self.texto_cand_1 = cria_texto_candidato(1)
        
        self.candidato_2 = candidato2
        self.pontos_cand_2 = 0
        self.texto_cand_2 = cria_texto_candidato(2)
        
        self.candidato_3 = candidato3
        self.pontos_cand_3 = 0
        self.texto_cand_3 = cria_texto_candidato(3)
        
        self.candidato_4 = candidato4
        self.pontos_cand_4 = 0
        self.texto_cand_4 = cria_texto_candidato(4)
        
        self.nmr_de_perguntas = 10
        self.texto_perguntas = armazena_perguntas()
        self.nmr_pergunta = armazena_texto_nmr_pergunta()
        
        roda_quiz(self, menu_layout)

def decide_pontos(nmr_pergunta, quiz, resposta):
    nmr_pergunta += 1
    
    if nmr_pergunta == 1:
        if resposta == 'Positivo':
            quiz.pontos_cand_3 += 1
            quiz.pontos_cand_1 -= 1
            quiz.pontos_cand_4 -= 1
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_3 -= 1
            quiz.pontos_cand_1 += 1
            quiz.pontos_cand_2 += 1
            quiz.pontos_cand_4 += 1
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_3 -= 2
            quiz.pontos_cand_1 += 2
            quiz.pontos_cand_2 += 2
            quiz.pontos_cand_4 += 2
    
    elif nmr_pergunta == 2:
        if resposta == 'Positivo':
            quiz.pontos_cand_3 += 2
            quiz.pontos_cand_4 =- 1
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_3 -= 1000 #impossivel ganhar
            quiz.pontos_cand_4 += 1 
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_3 -= 2000 #Muito mais impossivel ganhar
            quiz.pontos_cand_4 += 2  
        
    elif nmr_pergunta == 3:
        if resposta == 'Positivo':
            quiz.pontos_cand_4 -= 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_4 += 1
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_4 += 2   
                     
    elif nmr_pergunta == 4:
        if resposta == 'Positivo':
            quiz.pontos_cand_2 += 2
            quiz.pontos_cand_4 += 1
            quiz.pontos_cand_3 -= 1
            pass
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_2 -= 2
            quiz.pontos_cand_3 += 1
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_2 -= 4
            quiz.pontos_cand_3 += 2    
        
    elif nmr_pergunta == 5:
        if resposta == 'Positivo':
            quiz.pontos_cand_2 -= 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_2 += 2
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_2 += 4
          
    elif nmr_pergunta == 6:
        if resposta == 'Positivo':
            quiz.pontos_cand_4 += 2
            quiz.pontos_cand_1 -= 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_1 += 1
            quiz.pontos_cand_2 -= 2
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_1 += 2
            quiz.pontos_cand_2 -= 4
           
    elif nmr_pergunta == 7:
        if resposta == 'Positivo':
            quiz.pontos_cand_1 += 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo' or resposta == 'Muito Negativo':
            quiz.pontos_cand_1 -= 1000 #impossivel ganhar
               
    elif nmr_pergunta == 8:
        if resposta == 'Positivo':
            quiz.pontos_cand_1 += 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_1 -= 2
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_1 -= 4
            
    elif nmr_pergunta == 9:
        if resposta == 'Positivo':
            quiz.pontos_cand_3 += 2
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_3 -= 2
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_3 -= 4
        
    elif nmr_pergunta == 10:
        if resposta == 'Positivo':
            quiz.pontos_cand_1 += 1
            quiz.pontos_cand_2 -= 1
            quiz.pontos_cand_4 -= 1
        elif resposta == 'Neutro':
            return
        elif resposta == 'Negativo':
            quiz.pontos_cand_1 -= 1
        elif resposta == 'Muito Negativo':
            quiz.pontos_cand_1 -= 2
         
def cria_texto_candidato(nmr_candidato):
        texto = ""
        if nmr_candidato == 1:
            texto = "Você se mostrou uma pessoa altamente preocupada em como o governo está atuando em nossas vidas.\n"
            texto += "A Jéssica Matos, do PNG (Partido dos Nacionalistas Gigantes), concorda com suas necessidades e também busca mudança!"
        elif nmr_candidato == 2:
            texto = "A água vem se tornando um ponto crítico nos dias atuais.Você concorda com Matheus Bragança e \
            busca melhorar a situação hídrica do nosso país, a frente do Partido dos Lavadores Aquafóbicos\
            (PLA)."
        elif nmr_candidato == 3:
            texto = "Você considera o esporte essencial na vida da população, exatamente o que o candidato Jefferson\
                    Moreira propõe, pelo Partido dos Adoradores do Tênis de Mesa (PATM), o esporte vai ser ponto\
                    essencial na governo."
        elif nmr_candidato == 4:
            texto = "Você se identifica com Roberto Autônomo, a segurança nacional está em voga e deve ser melhor\
            trabalhada em nosso país. Através do Partido dos Idealizadores  Atômicos (PIA), Roberto busca mudar\
            esse cenário."
        
        return texto
    
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
        "---> Questão 1 ",
        "---> Questão 2 ",
        "---> Questão 3 ",
        "---> Questão 4 ",
        "---> Questão 5 ",
        "---> Questão 6 ",
        "---> Questão 7 ",
        "---> Questão 8 ",
        "---> Questão 9 ",
        "---> Questão 10 ",
    ]
    return nmr_pergunta 

def proxima_pergunta(window, quiz, pergunta_atual=0):
    window['-NMR_PERGUNTA-'].update(quiz.nmr_pergunta[pergunta_atual])
    window['-TEXTO_PERGUNTA-'].update(quiz.texto_perguntas[pergunta_atual])

def roda_quiz(quiz, window):
             
    #Comecando da primeira pergunta
    proxima_pergunta(window, quiz)
    iteracao_menu_quiz(window, 0)
    pergunta_atual = 1
    
    aux = 0
    
    while True:
        event, values = window.read()
        
        if event == '-VOLTA_MENU-':
            print("Entrei nesse")
            iteracao_menu_quiz(window, 1)
            break
        elif event == sg.WIN_CLOSED:
            print("Entrei_sair 3")
            aux = 1
            break
        
        elif(pergunta_atual < quiz.nmr_de_perguntas):
            if event == '-POSITIVO-':
                decide_pontos(pergunta_atual, quiz, 'Positivo')
                proxima_pergunta(window, quiz, pergunta_atual)
                pergunta_atual += 1
                
            elif event == '-NEUTRO-':
                decide_pontos(pergunta_atual, quiz, 'Neutro')
                proxima_pergunta(window, quiz, pergunta_atual)
                pergunta_atual += 1
                
            elif event == '-NEGATIVO-':
                decide_pontos(pergunta_atual, quiz, 'Negativo')
                proxima_pergunta(window, quiz, pergunta_atual)
                pergunta_atual += 1
                
            elif event == '-MUITO_NEGATIVO-':
                decide_pontos(pergunta_atual, quiz, 'Muito Negativo')
                proxima_pergunta(window, quiz, pergunta_atual)
                pergunta_atual += 1
                
            elif event == '-VOLTA_MENU-':
                iteracao_menu_quiz(window, 1)
                break
            
            elif event == sg.WIN_CLOSED:
                print("Entrei_sair 1")
                aux = 1
                break
            
        elif pergunta_atual == quiz.nmr_de_perguntas:
            pontuacoes=[quiz.pontos_cand_1, quiz.pontos_cand_2, quiz.pontos_cand_3, quiz.pontos_cand_4]
            pontuacoes.sort()
            resultado = pontuacoes[3]
            size = (50, 50) #tamanho da imagem do candidato
            if(resultado == quiz.pontos_cand_1):
                window['-NOME_CANDIDATO-'].update("Jessica Matos")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_1)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_1.numero)
                im = Image.open(r'.\assets\candidato1.jpeg')
                im = im.resize(size, resample=Image.BICUBIC)
                window['-FOTO_CANIDATO-'].update("Matheus Bragança")
                
            elif(resultado == quiz.pontos_cand_2):
                window['-NOME_CANDIDATO-'].update("Matheus Bragança")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_2)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_2.numero)
                im = Image.open(r'.\assets\candidato2.jpeg')
                im = im.resize(size, resample=Image.BICUBIC)
                window['-FOTO_CANIDATO-'].update("Matheus Bragança")
                
            elif(resultado == quiz.pontos_cand_3):
                window['-NOME_CANDIDATO-'].update("Jefferson Moreira")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_3)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_3.numero)
                im = Image.open(r'.\assets\candidato3.jpeg')
                im = im.resize(size, resample=Image.BICUBIC)
                window['-FOTO_CANIDATO-'].update("Matheus Bragança")
                
            elif(resultado == quiz.pontos_cand_4):
                window['-NOME_CANDIDATO-'].update("Roberto Autônomo")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_4)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_4.numero)
                im = Image.open(r'.\assets\candidato4.jpeg')
                im = im.resize(size, resample=Image.BICUBIC)
                window['-FOTO_CANIDATO-'].update("Matheus Bragança")
            
            elif event == '-VOLTA_MENU-':
                iteracao_menu_quiz(window, 1)
                break
            
            elif event == sg.WIN_CLOSED:
                print("Entrei_sair 2")
                aux = 1
                break
            
            window['-QUIZ_LY-'].update(visible=False)
            window['-QUIZ_LY_FIM-'].update(visible=True)
            pergunta_atual += 1
        
    if aux == 1:
        window.close()
        
#Atualizacoes de tela
# se troca == 0: menu -> nova tela
# se troca == 1: nova tela -> menu
def iteracao_menu_quiz(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-QUIZ_LY-'].update(visible=True)
    elif troca == 1:
        window['-MENU_LY-'].update(visible=True)
        window['-QUIZ_LY-'].update(visible=False)
        window['-QUIZ_LY_FIM-'].update(visible=False)
    
def iteracao_menu_urna(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-URNA_LY-'].update(visible=True)
    elif troca == 1:
        window['-URNA_LY-'].update(visible=False)
        window['-MENU_LY-'].update(visible=True)

def iteracao_menu_simulacao(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-SIMULACAO_LY-'].update(visible=True)
    elif troca == 1:
        window['-SIMULACAO_LY-'].update(visible=False)
        window['-MENU_LY-'].update(visible=True)

def menu_inicial():
    sleep_time = 10
    
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
                    [sg.Button('VOLTAR AO MENU PRINCIPAL', key='-VOLTA_MENU-', font="Courier 24", auto_size_button=True, button_color='#3065ac'), sg.Image(key='-FOTO_CANDIDATO-')],
                    [sg.Text("", size=(None, 1))]]
    
    #layout_urna = []
    
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
               sg.pin(sg.Column(layout_quiz_fim, key='-QUIZ_LY_FIM-', size=TAMANHO_DE_TELA_QUIZ_FINAL, element_justification='left', visible=False, expand_x=True, expand_y=True))]]
               #sg.pin(sg.Column(layout_urna, key='-URNA_LY-', size=TAMANHO_DE_TELA, element_justification='center', visible=False)),
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
    
    #quiz_rodando = False
    #votacao_rodando = False
    #simulacao_rodando = False 
    
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
        elif event == sg.WIN_CLOSED or event == '-QUIT-':
            break
        
    window.close()

if __name__ == '__main__':
    menu_inicial()