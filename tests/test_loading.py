import unittest
from dragonizer.loading import *

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

    def test_minimize_row_delta_loading(self):
        loading, _ = minimize_row_delta(passengers_static)

        # Verify the number of passengers on each side
        self.assertEqual(len(loading['left_side']), len(loading['right_side']))


    def test_minimize_row_delta(self):

        _, rows = minimize_row_delta(passengers_static)

        # Verify the sum of weights in each row
        for row in rows:
            left_weight = row['left_passenger']['weight']
            right_weight = row['right_passenger']['weight']
            sum_weight = row['sum_weight']
            self.assertEqual(sum_weight, left_weight + right_weight)
        #*! Für später?
        ## Verify the order of rows based on sum of weights (heaviest to lightest)
        #for i in range(1, len(rows)):
        #    prev_row = rows[i-1]
        #    curr_row = rows[i]
        #    prev_sum_weight = prev_row['sum_weight']
        #    curr_sum_weight = curr_row['sum_weight']
        #    self.assertGreaterEqual(prev_sum_weight, curr_sum_weight)


    #def test_optimal_seating(self):
    #    loading = #minimize_row_delta(passengers=passengers_stat#ic)
    #    seating = optimize_seating(loading)

if __name__ == '__main__':
    unittest.main()
