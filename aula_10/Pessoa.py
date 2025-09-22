class Pessoa:
    nome = ""
    cpf = ""
    data_nasc = ""
    telefone = ""
    email = ""

    # CONSTRUTOR
    def __init__(self, nome,cpf,email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def apresentarSe(self):
        print (f"Olá, sou uma pessoa! Meu nome é {self.nome}")
    
    
