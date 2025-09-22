from controleFinanceiro import ControleFinanceiro
from transacao import Transacao
opc =0
meu_Gerenciador = ControleFinanceiro()
while (opc != 3):
    print("***********Controle de Transações***********")
    print("")
    print("1 - Cadastrar transação")
    print("2 - Listar transações cadastradas")
    print("3 - Sair")
    opc = int(input("Escolha uma das operações acima:"))

    if opc == 1:
        descricao = input("Forneça uma descrição da nova transação:")
        valor = float(input("Informe o valor da transação:"))
        tipo = input("Tipo da transação:")
        movimentacao = Transacao(descricao,valor,tipo)
        meu_Gerenciador.adicionaTransacao(movimentacao) 

    if opc == 2:
        meu_Gerenciador.listarTransacoes()