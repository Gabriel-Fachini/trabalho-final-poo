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
      
      