import unittest
from dragonizer.loading import SeatingOptimizer

passengers_static = [
    {'weight': 75, 'name': 'Passenger1', 'preference': 'left'},
    {'weight': 78, 'name': 'Passenger10', 'preference': 'right'},
    {'weight': 70, 'name': 'Passenger2', 'preference': 'left'},
    {'weight': 80, 'name': 'Passenger11', 'preference': 'right'},
    {'weight': 95, 'name': 'Passenger3', 'preference': 'left'},
    {'weight': 63, 'name': 'Passenger12', 'preference': 'right'},
    {'weight': 80, 'name': 'Passenger4', 'preference': 'left'},
    {'weight': 85, 'name': 'Passenger13', 'preference': 'right'},
    {'weight': 92, 'name': 'Passenger5', 'preference': 'left'},
    {'weight': 93, 'name': 'Passenger14', 'preference': 'right'},
    {'weight': 75, 'name': 'Passenger6', 'preference': 'left'},
    {'weight': 83, 'name': 'Passenger15', 'preference': 'right'},
    {'weight': 68, 'name': 'Passenger7', 'preference': 'left'},
    {'weight': 94, 'name': 'Passenger16', 'preference': 'right'},
    {'weight': 92, 'name': 'Passenger8', 'preference': 'left'},
    {'weight': 83, 'name': 'Passenger17', 'preference': 'right'},
    {'weight': 71, 'name': 'Passenger9', 'preference': 'left'},
    {'weight': 95, 'name': 'Passenger18', 'preference': 'right'}
]

class TestOptimalLoading(unittest.TestCase):
    def setUp(self):
        self.optimizer = SeatingOptimizer()
        self.passengers = passengers_static

    def test_minimize_row_delta_loading(self):
        loading, _ = self.optimizer.minimize_row_delta(self.passengers)

        # Überprüfen, ob die Anzahl der Passagiere auf jeder Seite gleich ist
        self.assertEqual(len(loading['left_side']), len(loading['right_side']))

    def test_minimize_row_delta(self):
        _, rows = self.optimizer.minimize_row_delta(self.passengers)

        # Überprüfen, ob die Gewichtssumme in jeder Reihe korrekt ist
        for row in rows:
            left_weight = row['left_passenger']['weight']
            right_weight = row['right_passenger']['weight']
            sum_weight = row['sum_weight']
            self.assertEqual(sum_weight, left_weight + right_weight)

    def test_optimize_seating(self):
        _, rows = self.optimizer.minimize_row_delta(self.passengers)
        seating_arrangement = self.optimizer.optimize_seating(rows)
        self.optimizer.print_optimal_seating_arrangement(seating_arrangement)
        # Überprüfen, ob die Reihenfolge der Sitzplätze korrekt ist
        #for i in range(1, len(seating_arrangement)):
        #    prev_row = seating_arrangement[i-1]
        #    curr_row = seating_arrangement[i]
        #    prev_sum_weight = prev_row['sum_weight']
        #    curr_sum_weight = curr_row['sum_weight']
        #    self.assertGreaterEqual(prev_sum_weight, curr_sum_weight)

if __name__ == '__main__':
    unittest.main()
