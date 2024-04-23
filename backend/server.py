from flask import Flask, request, jsonify
from dijkstra import Graph

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_distances():
    # Obtener los datos del grid desde la solicitud
    grid_data = request.get_json()

    # Crear instancia de Graph y calcular distancias con Dijkstra
    graph = Graph(...)
    distances = graph.dijkstra(...)

    # Devolver las distancias calculadas como respuesta JSON
    return jsonify(distances)

if __name__ == '__main__':
    app.run()