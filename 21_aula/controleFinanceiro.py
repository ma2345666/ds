from transacao import Transacao
import csv
import os
class ControleFinanceiro:  
    """  
    Gerencia uma coleção de transações financeiras,  
    com capacidade de salvar e carregar de um arquivo CSV.  
    """  
    def __init__(self, nome_arquivo='transacoes.csv'):  
        """  
        Construtor da classe ControleFinanceiro.  
        """  
        self._transacoes = []  
        self._nome_arquivo  = nome_arquivo  
         # O encapsulamento é aplicado aqui. A lista de transações e o nome do arquivo  
         # são "protegidos" dentro do objeto.  
        self.carregaTransacoes()  # <-- NOVO: Carrega os dados ao iniciar

    def adicionaTransacao(self, transacao: Transacao):  
        """  
        Adiciona uma nova transação à lista e salva no arquivo.  
        """  
        if isinstance(transacao, Transacao):  
            self._transacoes.append(transacao)  
            self.salvaTransacoes()  # <-- NOVO: Salva a lista após adicionar  
            print("Transação adicionada e salva com sucesso !")  
        else:  
            print("Erro: Apenas objetos do tipo Transacao podem ser adicionados.")

    def listaTransacoes(self):  
        """  
        Exibe todas as transações registradas.  
        """  
        if not self._transacoes:  
            print("  nNenhuma transação registrada.")  
            return

        print(" ----- Extrato Financeiro  -----")  
        for transacao in self._transacoes:  
            print(transacao)  
        print("--------------------------")

    def calculaSaldo(self):  
        """  
        Calcula e retorna o saldo total (receitas  - despesas).  
        """  
        saldo  = 0.0  
        for transacao in self._transacoes:  
            if transacao.tipo.lower()  == 'receita':  
                saldo  += transacao.valor  
            else:  
                saldo  -= transacao.valor  
        return saldo

    def salvaTransacoes(self):  
        """  
        Salva a lista de transações em um arquivo CSV.  
        """  
        try:  
            with open(self._nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:  
                 # O cabeçalho do nosso CSV  
                cabecalho  =  ['nome', 'valor', 'categoria' ]  
                escritor  = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
                escritor.writeheader()  # Escreve o cabeçalho no arquivo  
                for transacao in self._transacoes:  
                     # Usamos vars() para converter os atributos do objeto em um dicionário  
                    escritor.writerow(vars(transacao))  
        except IOError as e:  
            print(f"Erro ao salvar o arquivo: {e}")

    def carregaTransacoes(self):  
        """  
        Carrega as transações de um arquivo CSV para a lista.  
        """  
         # Verifica se o arquivo existe antes de tentar abri-lo  
        if not os.path.exists(self._nome_arquivo):  
            print("Arquivo de transações não encontrado. Começando um novo.")  
            return  # Sai da função se o arquivo não existe

        try:  
            with open(self._nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:  
                leitor  = csv.DictReader(arquivo_csv)  
                self._transacoes  =  [ ]  # Limpa a lista atual antes de carregar  
                for linha in leitor:  
                     # Recria o objeto Transacao a partir dos dados do CSV  
                     # Precisamos converter o valor de volta para float  
                    transacao  = Transacao(  
                        nome=linha ['nome' ],  
                        valor=float(linha ['valor' ]),  
                        categoria=linha ['categoria' ]  
                    )  
                    self._transacoes.append(transacao)  
            print("Transações carregadas com sucesso !")  
        except FileNotFoundError:  
             # Esta exceção é um seguro extra, embora o os.path.exists já verifique  
            print("Arquivo de transações não encontrado. Começando um novo.")  
        except Exception as e:  
            print(f"Erro ao carregar o arquivo: {e}")  
             # Se o arquivo estiver corrompido, começamos do zero para evitar erros  
            self._transacoes  =  [ ]