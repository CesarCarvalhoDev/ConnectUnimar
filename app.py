from flask import Flask, request, jsonify, render_template
import json
from operator import itemgetter

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

@app.route('/resultado')
def resultado():
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Exemplo de mapeamento de cursos por área
    cursos = {
        "gestao": "Administração Estratégica",
        "marketing": "Marketing Digital",
        "financas": "Finanças Corporativas",
        "tecnologia": "Introdução à Programação",
        "vendas": "Técnicas de Vendas",
        "inovacao": "Gestão da Inovação",
        "rh": "Gestão de Pessoas",
        "estrategia": "Planejamento Estratégico",
        "operacoes": "Gestão de Operações"
    }

    # Junta interesses e habilidades para ranquear
    ranking = []
    for area, valor in data["interesses"].items():
        prioridade = valor
        if area in data["habilidades"]:
            prioridade += data["habilidades"][area]  # se existir habilidade igual
        ranking.append({
            "area": area,
            "curso": cursos.get(area, area.title()),
            "prioridade": prioridade
        })

    # Ordena por prioridade e pega os 5 maiores
    ranking = sorted(ranking, key=itemgetter('prioridade'), reverse=True)[:5]
    # Atribui prioridade de 5 a 1
    for i, item in enumerate(ranking):
        item["nivel"] = 5 - i

    return render_template("resultado.html", perfil=data["perfil"], ranking=ranking)

if __name__ == '__main__':
    app.run(debug=True)