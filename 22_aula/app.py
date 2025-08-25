# Importando o framework Flask
from flask import Flask

# Associando a execução do Flask à variável app
app = Flask(__name__)

# Criando a rota "raiz" e associando-a ao método home()
@app.route('/')
# Método home retorna uma mensagem que será exibida no navegador 
def home():
    return "Olá, mundo! Começando com o Framework Flask!"

# if que verifica se o arquivo atual é o principal
# Se verdadeiro, executa o app com flask
if __name__ == '__main__':
    app.run(debug=True)