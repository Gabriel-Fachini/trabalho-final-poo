import PySimpleGUI as sg
import random
from Candidato import Candidato
TAMANHO_DE_TELA = (1000, 500)

class Simulacao():
    def __init__(self, candidato1, candidato2, candidato3, candidato4, window):
        self.lista_candidatos = [candidato1, candidato2, candidato3, candidato4]
        roda_simulacao(self, window)
        
def roda_simulacao(simulacao, window):

    iteracoes_simulacao(window, 0)
    aux = 0
    while True:
        eventos, valores = window.read()
        
        if eventos == '-INICIAR_SIMULACAO-':
            window['-SIMULACAO_LY_INICIO-'].update(visible=False)
            window['-SIMULACAO_LY_FINAL-'].update(visible=True)
            vencedor = simulacaoVotacao(simulacao.lista_candidatos)
            if vencedor != None:
                window['-NOME-'].update('Nome:' + vencedor.nome)
                window['-IDADE-'].update('Idade:' + str(vencedor.idade))
                window['-NUMERO-'].update('Numero:' + str(vencedor.numero))
                window['-NUMERO_VOTOS-'].update('Numero de votos:' + str(vencedor.numeroVotos))
            
            if eventos =='-VOLTA_MENU-7':
                iteracoes_simulacao(window, 3)
                break
            
        if eventos == '-4_ANOS_DEPOIS-':
            window['-NOME_CANDIDATO_HISTORIA-'].update(vencedor.nome)
            historia = texto_historia(vencedor.numero)
            window['-HISTORIA_DA_SIMULACAO-'].update(historia)
                
            iteracoes_simulacao(window, 1)
                
        if eventos =='-VOLTA_MENU-8':
            iteracoes_simulacao(window, 4)
            break
        
        if eventos =='-VOLTA_MENU-6':
            iteracoes_simulacao(window, 2)
            break
        
        if eventos =='-VOLTA_MENU-7':
            iteracoes_simulacao(window, 3)
            break

        if eventos == sg.WINDOW_CLOSED:
            aux = 1
            break

    if aux == 1:  
        window.close()
    
def iteracoes_simulacao(window, troca):
    #TROCA
    #0 -> menu para comeco da simulacao
    #1 -> simulacao para historia
    #2 -> do comeco da simulacao para menu
    #3 -> da simulacao para menu
    #4 -> da historia para menu
    
    if troca == 0:
        window['-MENU_LY-'].update(visible=False)
        window['-SIMULACAO_LY_INICIO-'].update(visible=True)
    elif troca == 1:
        window['-SIMULACAO_LY_FINAL-'].update(visible=False)
        window['-SIMULACAO_HISTORIA-'].update(visible=True)
    elif troca == 2:
        window['-SIMULACAO_LY_INICIO-'].update(visible=False)
        window['-MENU_LY-'].update(visible=True)
    elif troca == 3:
        window['-SIMULACAO_LY_FINAL-'].update(visible=False)
        window['-MENU_LY-'].update(visible=True)
    elif troca == 4:
        window['-SIMULACAO_HISTORIA-'].update(visible=False)
        window['-MENU_LY-'].update(visible=True)
    
def simulacaoVotacao(listaCandidatos):
      # for pessoa in range(212678954): # População do brasil
  for pessoa in range(1000000):
    index = random.randrange(0, 3)
    listaCandidatos[index].numeroVotos = listaCandidatos[index].numeroVotos + 1

  maiorNumeroDeVotos = 0
  for candidato in listaCandidatos:
    if candidato.numeroVotos > maiorNumeroDeVotos:
      maiorNumeroDeVotos = candidato.numeroVotos

  vencedores = []
  for candidato in listaCandidatos:
    if candidato.numeroVotos == maiorNumeroDeVotos:
      vencedores.append(candidato)

  if len(vencedores) > 1:
    print('Houve um empate! Empataram os candidatos:')
    for candidato in vencedores:
      print(candidato)
    return None
  else:
    return vencedores[0]

def texto_historia(nmr_candidato):
    nmr_candidato = int(nmr_candidato)
    historia = ''
    
    if nmr_candidato == 14:
        historia = "O país deixou de ser referência na área de pesquisa, além de passar a ser muito mal visto internacionalmente pela volta de diversas epidemias que eram dadas como controladas."
    elif nmr_candidato == 19:
       historia = "O país manteve seu nível de avanço, sem grandes mudanças, além de alcançar um padrão europeu de higiene."
    elif nmr_candidato == 12:
        historia = "No final de seu mandato, com o alto investimento o país se tornou um expoente no tênis de mesa, conquistando os últimos 2 campeonatos mundiais em todas as categorias. Nas outras diversas áreas, não houve grandes avanços."
    elif nmr_candidato == 16:
        historia = "Com o exacerbado investimento na segurança, principalmente na defesa nuclear, o Brasil passou a ser mal visto pelas potências e se tornou aliada de países como Coréia do Norte e Rússia, fazendo a nação sofrer e entrarem em segundo plano nos ações governamentais."
        
    return historia