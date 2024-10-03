from flask import Flask, request

app = Flask(__name__)

@app.route("/hello", methods = ['GET', 'POST'])
def index():
    name = request.args.get('key') or request.args.get('name', "")
    return 'Hello ' + name

@app.route("/hello/<name>")
def whatevername(name):
    return 'Hello ' + str(name)

@app.route("/reflect")
def reflect():
    return "Hello " + str(request.json)

app.run(host='0.0.0.0', port=81)