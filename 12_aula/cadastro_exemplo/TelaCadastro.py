import tkinter as tk
from Aluno import Aluno
class TelaCadastro:
    def __init__(self, master, voltar_callback):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Cadastro de Aluno")
        self.label.grid(row=0, column=1)
        tk.Label(self.frame, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=1, column=1)
        tk.Label(self.frame, text="Idade:").grid(row=2, column=0)
        self.idade_entry = tk.Entry(self.frame)
        self.idade_entry.grid(row=2, column=1)
        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.grid(row=3, column=1)
        self.botao_voltar = tk.Button(self.frame, text="Voltar", command=voltar_callback)
        self.botao_voltar.grid(row=4, column=1)
        self.lista_label = tk.Label(self.frame, text="")
        self.lista_label.grid(row=5, column=0, columnspan=2)
        self.lista_alunos = []

    def cadastrar(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()

        if nome and idade.isdigit():
          aluno = Aluno(nome, int(idade))
          self.lista_alunos.append(aluno)
          self.nome_entry.delete(0, tk.END)
          self.idade_entry.delete(0, tk.END)
          self.exibir_lista()

    
    def exibir_lista(self):
        texto = "\n".join(str(a) for a in self.lista_alunos)
        self.lista_label.config(text=texto)