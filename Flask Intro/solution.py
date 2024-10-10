from flask import Flask, request

app = Flask(__name__)

@app.route("/hello", methods = ['GET', 'POST'])
def index():
    name = request.args.get('name', "")
    if name:
        return 'Hello ' + name
    else:
        return "Hello World"

@app.route("/hello/<name>", methods=['GET'])
def whatevername(name):
    return 'Hello ' + str(name)

@app.route("/hello/<name>/<change>")
def change(name, change):
    return f'Hello {name}, your change is {change}'

@app.route('/reflect')
def reflect():
    return "Hello" + str(request.json)


@app.route("/reflect/plex")
def plex_reflect():
    new_dict = dict()
    for k, v in request.json.items():
        if type(k) == str:
            k = "plex_" + k
        if type(v) == str:
            v = "plex_" + v
        new_dict[k] = v

    return "Hello " + str(new_dict)

@app.route('/reflect/plex/form', methods=['POST'])
def reflect_form():
    return request.form

app.run(host='0.0.0.0', port=81)