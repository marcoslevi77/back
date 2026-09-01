from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mensagens = [
    "Você é minha Princesa",
    "Você é Dinâmica",
    "Você é uma mulher Incrível",
    "Você é Radiante",
    "Você é Bela",
    "Você é Amável",
    "Você é uma mulherGuerreira",
    "Você é Talentosa",
    "Você é Encantadora",
    "Você é Bondosa",
    "Você é uma namorada Extraordinária",
    "Você é Simpática",
    "Você é Ótima",
    "Você é Cativante",
    "Você é Fiel",
    "Você é Verdadeira",
    "Você é arte Impecável",
    "Você é Fascinante",
    "Você é uma Deusa",
    "Você é Esforçada",
    "Você é minha Companheira",
    "Você é Amorosa",
    "Você é um céu Deslumbrante",
    "Você é Divertida",
    "Você é Alegre",
    "Você é meu Universo",
    "Você é Carinhosa",
    "Você é Estilosa",
    "Você é uma Jóia",
    "Você é Maravilhosa",
    "Você é Iluminada",
    "Você é Digníssima",
    "Você é uma mulher Encantadora",
    "Você é Afetuosa",
    "Você é Brincalhona",
    "Você é Formosa",
    "Você é Sincera",
    "Você é Feliz",
    "Você é Fascinante",
    "Você é Admirável",
]


elogios = [
    {'id': i + 1, 'mensagem': msg}
    for i, msg in enumerate(mensagens)
]

@app.route('/elogios', methods=['GET'])
def get_elogios():
    return jsonify(elogios)

@app.route('/elogios/<int:id>', methods=['GET'])
def get_elogio(id):
    for elogio in elogios:
        if elogio['id'] == id:
            return jsonify(elogio)
    else:
        return jsonify({'message': 'Elogio não encontrado'}), 404

@app.route('/elogios', methods=['POST'])
def create_elogio():
    data = request.get_json()
    if not data or 'mensagem' not in data:
        return jsonify({'message': 'Mensagem é obrigatória'}), 400

    new_id = len(elogios) + 1
    new_elogio = {'id': new_id, 'mensagem': data['mensagem']}
    elogios.append(new_elogio)
    return jsonify(new_elogio), 201


if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)

