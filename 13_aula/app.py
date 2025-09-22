
class app:
    def __init__(self, root):
        self.frame1 = Frame(root)
        self.frame1.pack()
        Label(self.frame1,text="Conversão de Centímetros para Polegada ",
        font=("Verdana","14","bold"), height=3).pack()

        Label(self.frame1,text="Centímetro(s):").pack(side=LEFT)
        self.centimetro=Entry(self.frame1)
        self.centimetro.focus_force()
        Button(self.frame1,text="Converter",command=self.converter)

        Label(self.frame1,text="Polegada(s):").pack(side=LEFT)

        self.centimetro.focus_force()
        self.centimetro.pack(side=LEFT)
            