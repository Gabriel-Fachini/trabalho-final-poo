import PySimpleGUI as sg
#from PIL import Image, ImageTk
import os

class Quiz():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, menu_layout):
        self.candidato_1 = candidato1
        self.pontos_cand_1 = 0
        self.texto_cand_1 = texto_candidato(1)
        
        self.candidato_2 = candidato2
        self.pontos_cand_2 = 0
        self.texto_cand_2 = texto_candidato(2)
        
        self.candidato_3 = candidato3
        self.pontos_cand_3 = 0
        self.texto_cand_3 = texto_candidato(3)
        
        self.candidato_4 = candidato4
        self.pontos_cand_4 = 0
        self.texto_cand_4 = texto_candidato(4)
        
        self.nmr_de_perguntas = 10
        self.texto_perguntas = armazena_perguntas()
        self.nmr_pergunta = armazena_texto_nmr_pergunta()
        
        roda_quiz(self, menu_layout)
        
#------------------------------------------>>>>

def roda_quiz(quiz, window):         
    #Comecando da primeira pergunta
    proxima_pergunta(window, quiz)
    iteracao_menu_quiz(window, 0)
    pergunta_atual = 1
    
    aux = 0
    
    while True:
        event, values = window.read()
        print(pergunta_atual)
        print(event)
        
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
            
            diretorio = os. getcwd()
            
            #size = (50, 50) #tamanho da imagem do candidato
            if(resultado == quiz.pontos_cand_1):
                window['-NOME_CANDIDATO-'].update("Jessica Matos")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_1)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_1.numero)
                
                caminho_foto = diretorio + "\images\candidato1_R.jpeg"
                window['-FOTO_CANDIDATO-'].update(source=caminho_foto)
                
            elif(resultado == quiz.pontos_cand_2):
                window['-NOME_CANDIDATO-'].update("Matheus Bragança")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_2)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_2.numero)
                
                caminho_foto = diretorio + "\images\candidato2_R.jpeg"
                window['-FOTO_CANDIDATO-'].update(source=caminho_foto)
                
            elif(resultado == quiz.pontos_cand_3):
                window['-NOME_CANDIDATO-'].update("Jefferson Moreira")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_3)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_3.numero)
                
                caminho_foto = diretorio + "\images\candidato3_R.jpeg"
                window['-FOTO_CANDIDATO-'].update(source=caminho_foto)
                
            elif(resultado == quiz.pontos_cand_4):
                window['-NOME_CANDIDATO-'].update("Roberto Autônomo")
                window['-TEXTO_CANDIDATO-'].update(quiz.texto_cand_4)
                window['-NUMERO_CANDIDATO-'].update(quiz.candidato_4.numero)
                
                caminho_foto = diretorio + "\images\candidato4_R.jpeg"
                window['-FOTO_CANDIDATO-'].update(source=caminho_foto)
            
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
    
def iteracao_menu_quiz(window, troca):
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-QUIZ_LY-'].update(visible=True)
    elif troca == 1:
        window['-MENU_LY-'].update(visible=True)
        window['-QUIZ_LY-'].update(visible=False)
        window['-QUIZ_LY_FIM-'].update(visible=False)

def proxima_pergunta(window, quiz, pergunta_atual=0):
    window['-NMR_PERGUNTA-'].update(quiz.nmr_pergunta[pergunta_atual])
    window['-TEXTO_PERGUNTA-'].update(quiz.texto_perguntas[pergunta_atual])  
    
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
            quiz.pontos_cand_3 -= 1000 #impossivel ganhar
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

def texto_candidato(nmr_candidato):
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