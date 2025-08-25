from transacao import Transacao
""" 
movimentacao1 = Transacao("Salário de 07/2025",2000.0,"Receita")
movimentacao2 = Transacao("Conta de Luz de 07/2025",200.0,"Despesa")

print(movimentacao1)
print(movimentacao2) """

# Pedir para o usuário cadastrar a transação
""" descricao = input("Forneça uma descrição da nova transação:")
valor = float(input("Informe o valor da transação:"))
tipo = input("Tipo da transação:")

movimentacao3 = Transacao(descricao,valor,tipo)

print(movimentacao3) """

""" 
Classe para gerenciar as transações do usuário, permitindo adicionar ou 
excluir transações.
"""

class ControleFinanceiro:
    def __init__(self):
        self._transacoes = []
    
    def adicionaTransacao(self, transacao: Transacao):
        if isinstance(transacao, Transacao):
            self._transacoes.append(transacao)
            print("Transação adicionada com sucesso")
        else:
            print("Erro! Apenas objetos do tipo Transacao podem ser adicionados")

    def listarTransacoes(self):
        if not self._transacoes:
            print("Nenhuma transação cadastrada!")
            return
        
        for transacao in self._transacoes:
            print(transacao)

