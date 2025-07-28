from transacao import Transacao

""" movimentacao1 = Transacao("salario de 07/2025",2000.0,"Receita")
movimentacao2 = Transacao ("conta de luz de 07/2025",2000.0,"Despesa")

print(movimentacao1)
print(movimentacao2)
 """
descricao = input("Forneça uma descrição de nova transação:")
valor = float(input("Informe o valor da transação:"))
tipo = input("Tipo da transação:")

movimentacao3 = Transacao(descricao,valor,tipo)
print(movimentacao3)