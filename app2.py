import tkinter as tk
from telaInicial import telaInicial


class App:
    def__init__(self, root):
       self.root = root
       self.root.title("Sistema de Cadastro")
       self.root.geometry("300x300")
       self.tela_inicial = None
       self.tela_cadastro = None
       self.mostrar_tela_inicial()

def mostrar_tela_inicial(self):
    self.limpar_tela()
    self.tela_inicial = TelaInicial(self.root, self.mostrar_tela_cadastro)

def mostrar_tela_cadastro(self):
    self.limpar_tela()

def mostrar_tela_inicial(self):
    self.limpar_tela()
    self.tela_inicial = TelaInicial(self.root, self.mostrar_tela_cadastro)

def mostrar_tela_cadastro(self):
 self.limpar_tela()
 self.tela_cadastro = TelaCadastro(self.root, self.mostrar_tela_inicial)

def limpar_tela(self):
  for widget in self.root.winfo_children():
  widget.destroy()
if __name__ == "__main__":
root = tk.Tk()
app = App(root)
root.mainloop()