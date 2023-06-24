import unittest
from dragonizer.loading import optimal_loading

class TestOptimalLoading(unittest.TestCase):

    def test_optimal_loading(self):
        passengers = [
            {'weight': 70, 'position': 'front'},
            {'weight': 60, 'position': 'middle'},
            {'weight': 80, 'position': 'back'},
            {'weight': 65, 'position': 'middle'},
            # Add more test cases as needed
        ]

        loading = optimal_loading(passengers)

        # Perform assertions to check if the loading is optimal
        self.assertEqual(len(loading['left']), len(loading['right']))
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()
