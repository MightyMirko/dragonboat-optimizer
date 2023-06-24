def visualize_seating(loading):
    left_side = loading['left_side']
    right_side = loading['right_side']

    seating = ['X'] * 9
    for i, passenger in enumerate(left_side):
        if 'id' in passenger:
            seating[i] = str(passenger['id'])

    seating_str = " | ".join(seating)

    print("Seating Arrangement:")
    print("-------------------")
    print("Left Side:  |", seating_str, "|")
    print("-------------+----------------+-------------")

    seating = ['X'] * 9
    for i, passenger in enumerate(right_side):
        if 'id' in passenger:
            seating[8 - i] = str(passenger['id'])

    seating_str = " | ".join(seating)

    print("Right Side: |", seating_str, "|")


# Beispielaufruf der Funktion mit Testdaten
loading = {
    'left_side': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}],
    'right_side': [{'id': 8}, {'id': 9}, {'id': 10}, {'id': 11}, {'id': 12}, {'id': 13}, {'id': 14}]
}

visualize_seating(loading)


def optimal_loading(passengers):
    """
    Function to determine the optimal loading of passengers in an aircraft or dragon boat.

    Args:
        passengers (list): List of dictionaries representing passengers with their weight and seating preferences.

    Returns:
        dict: Dictionary containing the optimal loading configuration with passengers assigned to seats.

    """

    # Sort passengers based on weight in descending order
    passengers = sorted(passengers, key=lambda x: x['weight'], reverse=True)

    left_side = []
    right_side = []

    # Group passengers based on seating preferences
    for passenger in passengers:
        if passenger['preference'] == 'left':
            left_side.append(passenger)
        elif passenger['preference'] == 'right':
            right_side.append(passenger)

    # Determine the number of seats available on each side
    num_seats = min(len(left_side), len(right_side))

    # Assign passengers to seats based on weight and seating preferences
    left_assigned = []
    right_assigned = []

    for _ in range(num_seats):
        heaviest_left = max(left_side, key=lambda x: x['weight'])
        heaviest_right = max(right_side, key=lambda x: x['weight'])

        # Swap passengers if the weight difference is significant
        if abs(heaviest_left['weight'] - heaviest_right['weight']) >= 10:
            heaviest_left, heaviest_right = heaviest_right, heaviest_left

        left_assigned.append(heaviest_left)
        right_assigned.append(heaviest_right)

        left_side = [p for p in left_side if p != heaviest_left]
        right_side = [p for p in right_side if p != heaviest_right]

    loading = {
        'left_side': left_assigned,
        'right_side': right_assigned,
    }
    visualize_seating(loading)
    return loading
