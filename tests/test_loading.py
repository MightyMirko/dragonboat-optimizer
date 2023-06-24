import unittest
from dragonizer.loading import optimal_loading, visualize_seating

class TestOptimalLoading(unittest.TestCase):

    def test_optimal_loading(self):
        passengers = [
            {'weight': 93, 'name': "Mirko", 'preference': 'left'},
            {'weight': 73, 'name': "Tina", 'preference': 'right'},
            {'weight': 80, 'name': "Martin", 'preference': 'left'},
            {'weight': 70, 'name': "Lisa", 'preference': 'right'},
            {'weight': 75, 'name': "Susanne", 'preference': 'left'},
            {'weight': 92, 'name': "Markus", 'preference': 'right'},
            {'weight': 75, 'name': "Mike", 'preference': 'left'},
            {'weight': 82, 'name': "Michel", 'preference': 'left'},
            {'weight': 50, 'name': "Katharina", 'preference': 'left'},
            {'weight': 80, 'name': "Henrik", 'preference': 'left'},
            {'weight': 50, 'name': "Demba", 'preference': 'left'},
            {'weight': 80, 'name': "Claudia", 'preference': 'left'},
        ]

        loading = optimal_loading(passengers)

        left_side = loading['left_side']
        right_side = loading['right_side']

        # Assert that the number of passengers on each side is equal
        self.assertEqual(len(left_side), len(right_side))

        # Assert that the weight distribution on each side is balanced
        left_weight = sum(passenger['weight'] for passenger in left_side)
        right_weight = sum(passenger['weight'] for passenger in right_side)
        self.assertAlmostEqual(left_weight, right_weight, delta=0.01)

        # Add more assertions as needed

    @staticmethod
    def test_visualize_seating():
        loading = {
            'left_side': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}],
            'right_side': [{'id': 8}, {'id': 9}, {'id': 10}, {'id': 11}, {'id': 12}, {'id': 13}, {'id': 14}]
        }

        visualize_seating(loading)

if __name__ == '__main__':
    unittest.main()
