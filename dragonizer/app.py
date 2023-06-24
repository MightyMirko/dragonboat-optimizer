from flask import Flask, render_template, request, jsonify
from dragonizer.loading import SeatingOptimizer

app = Flask(__name__)
optimizer = SeatingOptimizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    passengers = request.get_json()

    loading, rows = optimizer.minimize_row_delta(passengers)
    seating_arrangement = optimizer.optimize_seating(rows)

    # Erstelle eine Liste mit den Sitzplatzinformationen
    seating_info = []
    for row in seating_arrangement:
        left_passenger = row['left_passenger']
        right_passenger = row['right_passenger']
        sum_weight = row['sum_weight']

        left_name = left_passenger['name'] if left_passenger else ""
        right_name = right_passenger['name'] if right_passenger else ""

        seating_info.append({'left_name': left_name, 'right_name': right_name, 'sum_weight': sum_weight})

    return jsonify({'loading': loading, 'seating_arrangement': seating_info})

if __name__ == '__main__':
    app.run(debug=True)
