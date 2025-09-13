from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Rota para exibir o formulário
@app.route('/')
def index():
    perfil = {
        "nome": "Cesar",
        "idade": 19,
        "cargo_atual": "Auxiliar Administrativo",
        "anos_experiencia": 1
    }
    return render_template("index.html", perfil=perfil)

# Rota para receber e salvar o JSON
@app.route('/save-json', methods=['POST'])
def save_json():
    data = request.get_json()
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify({"message": "Dados salvos com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)