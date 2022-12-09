from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
	return json.dumps(dict(text="hello"))

if __name__ == '__main__':
	app.run(debug=True)