from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

def calcular_troco(valor_compra, valor_pago):
    notas_disponiveis = [100, 10, 1]
    troco = valor_pago - valor_compra
    resultado = {'valor_compra': valor_compra, 'valor_pago': valor_pago, 'troco': troco, 'notas_troco': {}}

    for nota in notas_disponiveis:
        quantidade_notas = troco // nota
        if quantidade_notas > 0:
            resultado['notas_troco'][str    (nota)] = quantidade_notas
            troco -= quantidade_notas * nota

    return resultado

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        valor_compra = float(request.form['valor_compra'])
        valor_pago = float(request.form['valor_pago'])
        resultado = calcular_troco(valor_compra, valor_pago)
        return render_template('index.html', resultado=resultado)

    return render_template('index.html', resultado=None)

if __name__ == '__main__':
    app.run(debug=True)
