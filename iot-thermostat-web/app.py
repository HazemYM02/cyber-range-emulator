from flask import Flask, request, jsonify

app = Flask(__name__)
state = {"target": 22.0, "mode": "auto"}

@app.get('/')
def root():
    return jsonify({"ok": True, "state": state})

@app.post('/set')
def set_state():
    data = request.get_json(force=True, silent=True) or {}
    if 'target' in data:
        try:
            state['target'] = float(data['target'])
        except Exception:
            pass
    if 'mode' in data:
        state['mode'] = str(data['mode'])
    return jsonify(state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
