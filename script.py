from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify(message="hi")

if __name__ == '__main__':
    app.run(debug=True)
