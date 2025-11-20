from flask import Flask, render_template, request
import os
import importlib.util

# Importar módulo con nombre que empieza con número
ruta_corazon = os.path.join(os.path.dirname(__file__), "01_corazon.py")
spec = importlib.util.spec_from_file_location("corazon", ruta_corazon)
corazon_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corazon_module)
romantizar = corazon_module.romantizar

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form.get('nombre', 'Amor').strip() or "Amor"
        corazon = romantizar(nombre)
        return render_template('result.html', nombre=nombre, corazon=corazon)
    return render_template('index.html')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app.run(debug=True)