class TelaCadastro:
    def __init__(self, master, voltar_callback):
self.frame = tk.Frame(master)
self.frame.pack()
self.label = tk.Label(self.frame, text="Cadastro de Aluno")
self.label.grid(row=0, column=1)
tk.Label(self.frame, text="Nome:").grid(row=1, column=0)
self.nome_entry = tk.Entry(self.frame)