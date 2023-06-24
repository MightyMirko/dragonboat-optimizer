import unittest
from dragonizer.loading import optimal_loading

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

    def test_optimal_loading(self):
        loading = optimal_loading(passengers=passengers_static)

        # Separate left and right passengers
        left_passengers = loading['left_side']
        right_passengers = loading['right_side']

        # Calculate weight sums
        left_side_weight_sum = sum(p['weight'] for p in left_passengers)
        right_side_weight_sum = sum(p['weight'] for p in right_passengers)

        # Verify the optimal loading result
        self.assertAlmostEqual(left_side_weight_sum, right_side_weight_sum,delta=50)

        # Print weight sums
        print("Summe der Gewichte links:", left_side_weight_sum)
        print("Summe der Gewichte rechts:", right_side_weight_sum)

        # Print the seating arrangement for visualization
        seating = {
            'left_side': [p['name'] for p in left_passengers],
            'right_side': [p['name'] for p in right_passengers]
        }
        print("Sitzanordnung:")
        #print(seating)



if __name__ == '__main__':
    unittest.main()
