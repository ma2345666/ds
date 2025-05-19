import tkinter as tk
class TelaInicial:
  def __init__(self, master, ir_para_cadastro):
    self.frame = tk.Frame(master)
    self.frame.pack()
    self.label = tk.Label(self.frame, text="Bem-vindo ao sistema!")
    self.label.pack(pady=10)
    self.botao = tk.Button(self.frame, text="Cadastrar Aluno", command=ir_para_cadastro)
    self.botao.pack()