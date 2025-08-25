class Transacao:
   def __init__(self,nome,valor,categoria):
      
           self.nome = nome
           self.valor = valor
           self.categoria = categoria
       
        
   def __str__(self):
        return f"Transação: {self.nome} | Valor: R$ {self.valor} | Tipo: {self.categoria}"