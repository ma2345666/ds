class Aluno:
    
    def __init__(self, nome, idade):  # Corrigido: 'nome' como parâmetro
        self.nome = nome  # Atribuindo o valor de 'nome' ao atributo da instância
        self.idade = idade

    def __str__(self):
        return f"Estudante: {self.nome} possui {self.idade} anos"  # Corrigido o uso do 'f' para f-string
