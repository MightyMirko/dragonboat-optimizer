import unittest
from munkres import Munkres
from dragonizer.loading import SeatingOptimizer, Passenger

class TestSeatingOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = SeatingOptimizer()
        self.passengers = [
            Passenger('Passenger1', 75, 'left'),
            Passenger('Passenger10', 78, 'right'),
            Passenger('Passenger2', 70, 'left'),
            Passenger('Passenger11', 80, 'right'),
            Passenger('Passenger3', 95, 'left'),
            Passenger('Passenger12', 63, 'right'),
            Passenger('Passenger4', 80, 'left'),
            Passenger('Passenger13', 85, 'right'),
            Passenger('Passenger5', 92, 'left'),
            Passenger('Passenger14', 93, 'right'),
            Passenger('Passenger6', 75, 'left'),
            Passenger('Passenger15', 83, 'right'),
            Passenger('Passenger7', 68, 'left'),
            Passenger('Passenger16', 94, 'right'),
            Passenger('Passenger8', 92, 'left'),
            Passenger('Passenger17', 83, 'right'),
            Passenger('Passenger9', 71, 'left'),
            Passenger('Passenger18', 95, 'right')
        ]

    def test_minimize_row_delta(self):
        loading, rows = self.optimizer.minimize_row_delta(self.passengers)

        # Überprüfen, ob die Anzahl der Passagiere auf jeder Seite gleich ist
        self.assertEqual(len(loading['left_side']), len(loading['right_side']))

        # Überprüfen, ob die Gewichtssumme in jeder Reihe korrekt ist
        for row in rows:
            left_weight = row['left_passenger'].weight
            right_weight = row['right_passenger'].weight
            sum_weight = row['sum_weight']
            self.assertEqual(sum_weight, left_weight + right_weight)

    def test_optimize_seating(self):
        _, rows = self.optimizer.minimize_row_delta(self.passengers)
        seating_arrangement = self.optimizer.optimize_seating(rows)

        # Überprüfen, ob die Reihenfolge der Sitzplätze korrekt ist
        for i in range(1, len(seating_arrangement)):
            prev_row = seating_arrangement[i-1]
            curr_row = seating_arrangement[i]
            prev_sum_weight = prev_row['sum_weight']
            curr_sum_weight = curr_row['sum_weight']
            self.assertGreaterEqual(prev_sum_weight, curr_sum_weight)

if __name__ == '__main__':
    unittest.main()
