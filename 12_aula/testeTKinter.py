import tkinter as tk
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("300x200")
label = tk.Label(janela,text="Texto da janela principal")
label.pack(pady=30)
janela.mainloop()
