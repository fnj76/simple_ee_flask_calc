from flask import Flask, render_template, url_for, request
import numpy as np
import matplotlib.pyplot as plt

# Crear una instancia de la aplicación Flask
app = Flask(__name__,static_folder="static")

# Ruta principal de la aplicación
@app.route("/")
def main():
    # Renderiza la plantilla "inicio.html" para la página principal
    return render_template("inicio.html")

# Ruta para la página de la calculadora de Coulomb
@app.route("/coulomb")
def coulomb():
    # Renderiza la plantilla "coulomb.html" para la calculadora de Coulomb
    return render_template("coulomb.html")

# Ruta para la página de la calculadora de densidad de carga
@app.route("/densidad")
def densidad():
    # Renderiza la plantilla "densidad.html" para la calculadora de densidad de carga
    return render_template("densidad.html")

# Ruta para la página de la calculadora de energía potencial eléctrica
@app.route("/potencial")
def potencial():
    # Renderiza la plantilla "potencial.html" para la calculadora de energía potencial eléctrica
    return render_template("potencial.html")

# Ruta para la página de la calculadora de intensidad del campo eléctrico
@app.route("/intensidad")
def intensidad():
    # Renderiza la plantilla "intensidad.html" para la calculadora de intensidad del campo eléctrico
    return render_template("intensidad.html")

# Ruta para la página de las ecuaciones de Maxwell
@app.route("/Maxwell")
def Maxwell():
    # Renderiza la plantilla "Maxwell.html" para las ecuaciones de Maxwell
    return render_template("Maxwell.html")

# Ruta para calcular la fuerza electrostática usando la ley de Coulomb
@app.route("/calcular", methods=["post"])
def calcular():
    # Obtiene los valores de carga y distancia del formulario
    carga1 = float(request.form["carga1"])
    carga2 = float(request.form["carga2"])
    distancia = float(request.form["distancia"])
    # Constante de Coulomb (k) en unidades SI
    constantePropo = 9 * 10**9
    # Calcula la fuerza electrostática usando la fórmula de Coulomb
    resultado = constantePropo * carga1 * carga2 / (distancia ** 2)
    # Formatea el resultado para mostrar con comas como separadores de miles
    resultado_format = format(resultado, ",")
    # Renderiza la plantilla "coulomb.html" con el resultado calculado
    return render_template("coulomb.html", resultado=resultado_format)

# Ruta para calcular la densidad de carga
@app.route("/calcular1", methods=["post"])
def calcular1():
    # Obtiene los valores de carga y área del formulario
    carga = float(request.form["carga"])
    area = float(request.form["area"])
    # Calcula la densidad de carga usando la fórmula
    resultado = carga / area
    # Formatea el resultado para mostrar con comas como separadores de miles
    resultado_format = format(resultado, ",")
    # Renderiza la plantilla "densidad.html" con el resultado calculado
    return render_template("densidad.html", resultado=resultado_format)

# Ruta para calcular la energía potencial eléctrica
@app.route("/calcular2", methods=["post"])
def calcular2():
    # Obtiene los valores de carga y distancia del formulario
    carga1 = float(request.form["carga1"])
    carga2 = float(request.form["carga2"])
    distancia = float(request.form["distancia"])
    # Constante de Coulomb (k) en unidades SI
    constantePropo = 9 * 10**9
    # Calcula la energía potencial eléctrica usando la fórmula
    resultado = constantePropo * carga1 * carga2 / distancia
    # Formatea el resultado para mostrar con comas como separadores de miles
    resultado_format = format(resultado, ",")
    # Renderiza la plantilla "potencial.html" con el resultado calculado
    return render_template("potencial.html", resultado=resultado_format)

# Ruta para calcular la intensidad del campo eléctrico
@app.route("/calcular3", methods=["post"])
def calcular3():
    # Obtiene el valor de la carga y la distancia del formulario
    carga1 = float(request.form["carga"])
    distancia = float(request.form["distancia"])
    # Constante de Coulomb (k) en unidades SI
    constantePropo = 9 * 10**9
    # Calcula la intensidad del campo eléctrico usando la fórmula
    resultado = constantePropo * carga1 / distancia
    # Formatea el resultado para mostrar con comas como separadores de miles
    resultado_format = format(resultado, ",")
    # Renderiza la plantilla "intensidad.html" con el resultado calculado
    return render_template("intensidad.html", resultado=resultado_format)

# Ruta para procesar datos y graficar
@app.route("/aumentar", methods=["post"])
def aumentar():
    datos = []
    # Recoge los datos del formulario, creando una lista de tuplas con cargas y distancias
    for i in range(int(request.form["num_datos"])):
        carga1 = float(request.form[f"carga1_{i}"])
        carga2 = float(request.form[f"carga2_{i}"])
        distancia = float(request.form[f"distancia_{i}"])
        datos.append((carga1, carga2, distancia))
    # Renderiza la plantilla "graficar.html" con los datos recogidos
    return render_template("graficar.html", datos=datos)

# Ruta para graficar los datos recogidos
@app.route("/graficar", methods=["post"])
def graficar():
    datos = []
    # Recoge los datos del formulario, creando una lista de tuplas con cargas y distancias
    for i in range(int(request.form["num_datos"])):
        carga1 = float(request.form[f"carga1_{i}"])
        carga2 = float(request.form[f"carga2_{i}"])
        distancia = float(request.form[f"distancia_{i}"])
        datos.append((carga1, carga2, distancia))
    # Extrae las cargas y distancias para graficar
    x = [dato[0] for dato in datos]
    y = [dato[1] for dato in datos]
    # Crea un gráfico usando matplotlib
    plt.plot(x, y)
    plt.xlabel("Carga 1")
    plt.ylabel("Carga 2")
    plt.title("Gráfico de Cargas")
    # Guarda el gráfico como una imagen en el directorio estático
    plt.savefig("static/grafico.png")
    # Renderiza la plantilla "graficar.html" con la imagen del gráfico
    return render_template("graficar.html", imagen="grafico.png")

# Ruta para calcular las ecuaciones de Maxwell
@app.route('/ecuaciones_maxwell', methods=['POST'])
def ecuaciones_maxwell():
    if request.method == 'POST':
        # Ley de Gauss para el campo eléctrico
        carga__ = float(request.form.get('carga__', 0))
        area__ = float(request.form.get('area__', 1))  # Evita división por cero
        resultado_gauss_electrica = carga__ / (8.854e-12 * area__)

        # Ley de Gauss para el campo magnético
        campo_magnetico = float(request.form.get('campo_magnetico', 0))
        area_magnetica = float(request.form.get('area_magnetica', 1))  # Evita valores por cero
        resultado_gauss_magnetica = campo_magnetico * area_magnetica

        # Ley de Faraday de la inducción
        campo_electrico = float(request.form.get('campo_electrico', 0))
        longitud = float(request.form.get('longitud', 1))  # Evita valores por cero
        flujo_magnetico = float(request.form.get('flujo_magnetico', 0))
        resultado_faraday_induccion = -campo_electrico * longitud * flujo_magnetico

        # Ley de Ampere con corrección de Maxwell
        campo_magnetico_ampere = float(request.form.get('campo_magnetico_ampere', 0))
        longitud_ampere = float(request.form.get('longitud_ampere', 1))  # Evita valores por cero
        corriente_electrica = float(request.form.get('corriente_electrica', 0))
        flujo_electrico = float(request.form.get('flujo_electrico', 0))
        resultado_ampere_correccion_maxwell = campo_magnetico_ampere * longitud_ampere - 4e-7 * (corriente_electrica + flujo_electrico)

        # Formateo de los resultados
        resultado_gauss_electrica_format = format(resultado_gauss_electrica, ",")
        resultado_gauss_magnetica_format = format(resultado_gauss_magnetica, ",")
        resultado_faraday_induccion_format = format(resultado_faraday_induccion, ",")
        resultado_ampere_correccion_maxwell_format = format(resultado_ampere_correccion_maxwell, ",")

        # Renderiza la plantilla "Maxwell.html" con los resultados de las ecuaciones de Maxwell
        return render_template('Maxwell.html', 
                               resultado_gauss_electrica=resultado_gauss_electrica_format, 
                               resultado_gauss_magnetica=resultado_gauss_magnetica_format, 
                               resultado_faraday_induccion=resultado_faraday_induccion_format, 
                               resultado_ampere_correccion_maxwell=resultado_ampere_correccion_maxwell_format,
                               unidad_area='m²', 
                               unidad_flujo='Wb', 
                               unidad_longitud='m')
    # En caso de que no se reciba una solicitud POST, renderiza "Maxwell.html" sin resultados
    return render_template('Maxwell.html')

# Ejecuta la aplicación en modo de depuración si este archivo se ejecuta como script
if __name__ == '__main__':
    app.run()
