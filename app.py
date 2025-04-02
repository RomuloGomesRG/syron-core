from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SYRON está online e pronto para receber comandos."

@app.route('/comando', methods=['POST'])
def comando():
    dados = request.get_json()
    comando_recebido = dados.get('comando', '').lower()
    resposta = interpretar_comando(comando_recebido)
    return jsonify({'resposta': resposta})

def interpretar_comando(texto):
    if "agenda" in texto:
        return "Abrindo sua agenda."
    elif "tarefa" in texto:
        return "Registrando nova tarefa."
    elif "desligar" in texto:
        return "Comando para desligar o sistema recebido."
    else:
        return "Comando não reconhecido, Rômulo."

if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta, debug=True)
