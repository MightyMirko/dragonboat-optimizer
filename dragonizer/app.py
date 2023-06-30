from flask import Flask, render_template, request, redirect
from munkres import Munkres
from loading import SeatingOptimizer
import json, yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        passengers = request.form['passengers']
        passengers = json.loads(passengers)
        return redirect('/results?passengers=' + passengers)
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        passengers = request.args.get('passengers', '')
        print(passengers)
        optimizer = SeatingOptimizer()
        try:
            _, seating_arrangement = optimizer.minimize_row_delta(passengers)
            seating_arrangement = optimizer.optimize_seating(seating_arrangement)   
            return render_template('results.html', seating_arrangement=seating_arrangement)
        except:
            print(passengers)
            exit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
