from flask import Flask, render_template, request
from munkres import Munkres
from loading import SeatingOptimizer
import json, yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        passengers = request.form.get('passengers')
        passengers = json.loads(passengers)
        optimizer = SeatingOptimizer()
        loading, seating_arrangement = optimizer.minimize_row_delta(passengers)
        seating_arrangement = optimizer.optimize_seating(seating_arrangement)
        
        #for i in seating_arrangement:
        #    print(i)
        #    type(i)
        print(seating_arrangement.__getattribute__)
        return render_template('results.html', seating_arrangement=seating_arrangement)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
