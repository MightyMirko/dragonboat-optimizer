from dragonizer.loading import visualize_seating

def test_visualize_seating():
    loading = {
        'left_side': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}],
        'right_side': [{'id': 8}, {'id': 9}, {'id': 10}, {'id': 11}, {'id': 12}, {'id': 13}, {'id': 14}]
    }

    visualize_seating(loading)

test_visualize_seating()
