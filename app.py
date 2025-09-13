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

@app.route('/trilha-cursos', methods=['POST'])
def trilha_cursos():
    # Verifica se o arquivo JSON foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']

    try:
        # Lê o conteúdo do JSON
        data = json.load(file)

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

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)