class Flauta:
    def __init__(self, material, tamanho):
        self.material = material  # material da flauta, por exemplo, madeira ou metal
        self.tamanho = tamanho    # tamanho da flauta, pode ser 'curta', 'média' ou 'longa'

    def tocar(self):
        print(f"Tocando a flauta feita de {self.material} e tamanho {self.tamanho}.")
        print("Som da flauta: Fiiiiiii... ♪♪♪")

# Criando um objeto flauta
flauta1 = Flauta("madeira", "média")

# Chamando a função tocar
flauta1.tocar()
