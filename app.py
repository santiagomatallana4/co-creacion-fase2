from flask import Flask, render_template, send_from_directory, request, jsonify#Importamos tres componentes esenciales de Flask:
import csv # Importa el módulo csv para trabajar con archivos CSV
import json #Inporta el módulo json para trabajar con archivos JSON
import os
app=Flask(__name__, template_folder="pages") #Crea una instancia Flask y la asigna a la variable app. __name__ indica el módulo actual.

@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory('styles', filename)

@app.route('/js/<path:filename>')
def javascript(filename): 
    return send_from_directory('js', filename)

@app.route('/assets/img/<path:filename>')
def images(filename):
    return send_from_directory('assets/img', filename)

@app.route('/especies')
def obtener_especies():
    archivo_json= os.path.join('assets', 'json', 'especies_invasoras_boyaca.json')

    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            especies_data = json.load(f)
        return jsonify(especies_data)
    except FileNotFoundError:
        return jsonify({"error": "Archivo no encontrado"}), 404

@app.route("/") #Asocia la función index con la URL raíz (/) de la aplicación
def index(): #Define la función index que maneja la solicitud de la página principal.
    return render_template("index.html") #Renderiza la plantilla HTML "index.html".

@app.route("/flora")
def flora():
    return render_template('flora.html')

@app.route("/fauna")
def fauna():
    return render_template('fauna.html')

@app.route("/ecosistemas")
def ecosistemas():
    return render_template('ecosistemas.html')

@app.route("/especies-invasoras")
def especies_invasoras():
    return render_template('especies-invasoras.html')

if __name__ == '__main__':
    app.debug=True
    app.run()          