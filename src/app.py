from flask import Flask, request, jsonify
from .model import Model
import json
import traceback
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False

model = Model()


@app.route('/dialog', methods=['POST'])
def check():
    try:
        data = request.data.decode('utf-8')
        data = json.loads(data)
        resp = model.dialog(str(data['chat']), str(data['name']))
        return jsonify({'response': resp}), 200

    except Exception as e:
        print(traceback.format_exc(), flush=True)
        return jsonify({"response": str(e)}), 500
