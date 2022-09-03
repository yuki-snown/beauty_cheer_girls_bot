from flask import Flask, request, jsonify
from .model import Model
import re
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
        chat = str(data['chat'])
        name = str(data['name'])
        resp = model.dialog(chat, name)
        resp = re.findall(f'<{name}>(.*)</s>', resp)[0]
        return jsonify({'response': resp}), 200

    except Exception as e:
        print(traceback.format_exc(), flush=True)
        return jsonify({"response": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
