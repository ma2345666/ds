
from  tkinter import 


class App:
    def__init__(self, root):
       self.frame1 = Frame  (root)
       self.frame1.pack()
       Label(self.frame1,text="Conversão de Centimetro para Polegada",
       font=("Verdana", "14", "bold"), height=3). pack()
       
       label(self.frame1,text="Centimetro(s):").pach(side=LEFT)
       self.centimetros=Entry(self.frame1)
       self.centimetros.focus_force() 
       self.centimetros.pack(side=LEFT)
       Button(self.frame1,text="converter", command=self.converter)

       label(self.frame1,text="Polegada(s):").pack(side=LEFT)

       self.centimetro.focus_force()
       self.centimetro.pack(side=LEFT)