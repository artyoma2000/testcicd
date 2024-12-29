from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify(message="hi for you")

@app.route('/test', methods=['GET'])
def test():
    return jsonify(message="test answer")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
