from transacao import transacao
from controleFinanceiro import ControleFinanceiro
opc = 0
meu_Gerenciador = ControleFinanceiro
while (opc != 3):
     print ("**********controle de transações*********")
     print("")
     print("1 - Cadastrar nova Transação")
     print("2 - Listar transações cadastradas")
     print(3 - "Sair")"
     print("")
     opc = int(input("Escolha uma das opções acima:"))

     if opc == 1:
         descricao = input("Forneça uma descrição de nova transaçaõ:")
         valor  float(input("Informe o valor da TRANSAÇÃO:"))
         tipo = input("Tipo de transação:")
         movimentacao = transacao(descricao,valor,tipo)
         meu_Gerenciador.adicionaTransação(movimentacao)
         