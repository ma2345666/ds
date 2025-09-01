from flask import Flask, render_template, request, redirect, url_for
from classes import Transacao, ControleFinanceiro

# Cria a aplicação Flask
app = Flask(__name__)

# Cria uma instância de nosso gerenciador. Em uma aplicação real, isso seria gerenciado de forma mais complexa.
# Para este exemplo, uma instância global simplifica as coisas.
gerenciador = ControleFinanceiro()

@app.route('/')
def index():
    """
    Rota principal que exibe a lista de transações e o saldo. Uma rota é um caminho indicado pelo usuário no formato de URL da página, que ao ser chamada, exibe um conteúdo com alguma funcionalidade do App. No Flask, associamos um rota a um método como acima index()
    """
    # Acessa os dados através dos métodos e propriedades do nosso objeto
    transacoes = gerenciador.transacoes
    saldo = gerenciador.calculaSaldo()
    # Renderiza o template HTML, passando os dados para ele
    return render_template('index.html', transacoes=transacoes, saldo=saldo)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    """
    Rota para adicionar uma nova transação (receita ou despesa).
    """
    # Pega os dados enviados pelo formulário HTML
    tipo = request.form['categoria']
    descricao = request.form['nome']
    valor = float(request.form['valor'])
    
    # Cria um novo objeto Transacao com os dados do formulário
    nova_transacao = Transacao(nome=descricao, valor=valor, categoria=tipo)
    
    # Usa nosso objeto gerenciador para adicionar a transação
    gerenciador.adicionaTransacao(nova_transacao)
    
    # Redireciona o usuário de volta para a página inicial
    return redirect(url_for('index'))

# Garante que o servidor de desenvolvimento só rode quando o script for executado diretamente
if __name__ == '__main__':
    # O modo debug recarrega o servidor automaticamente a cada alteração no código
    app.run(debug=True)
