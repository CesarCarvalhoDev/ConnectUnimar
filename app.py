from flask import Flask, request, jsonify
import requests
from flask import render_template
import openai
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Rota para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para receber e salvar o JSON
@app.route('/save-json', methods=['POST'])
def save_json():
    data = request.get_json()
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify({"message": "Dados salvos com sucesso!"})
# Caminho do arquivo JSON no servidor
JSON_PATH = "data.json"  # ajuste para o seu diretório

@app.route('/trilha-cursos', methods=['GET'])
def trilha_cursos():
    try:
        # Lê o JSON diretamente do diretório
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Monta o prompt dinamicamente
        prompt = f"""
        Você é um assistente de carreira inteligente.
        Receba os dados do usuário: {data}.
        Analise interesses, habilidades, objetivos e cursos disponíveis.
        Sugira uma trilha de cursos personalizada.
        Explique o motivo de cada curso e a ordem recomendada.
        Retorne em JSON estruturado com 'trilha': [
            {{ "curso": "string", "motivo": "string", "ordem": integer }}
        ].
        """

        # Chamada à API do OpenAI
        response = openai.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {"role": "system", "content": "Você é um assistente de carreira."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result_text = response.choices[0].message.content

        # Retorna o resultado da IA
        return jsonify({"resultado_ia": result_text})

    except FileNotFoundError:
        return jsonify({"error": f"Arquivo JSON não encontrado em {JSON_PATH}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)