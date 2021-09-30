from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/name/<name>', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"

@app.route('/palindromo', methods=['GET'])
def ejercicio1():
    # Su código va aquí
    return

@app.route('/operaciones', methods=['GET'])
def ejercicio2():
    # Su código va aquí
    return

@app.route('/ordenar', methods=['GET'])
def ejercicio3():
    # Su código va aquí
    return


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
