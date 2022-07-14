class Urna:
  def __init__(self, candidatos: list):
    self.candidatos = candidatos

  def votar(self, codigo: str):
    for candidato in self.candidatos:
      if codigo == candidato.codigo:
        candidato.adicionarVoto()