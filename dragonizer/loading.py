from munkres import Munkres

def minimize_row_delta(passengers):
    # Separate left and right passengers
    left_passengers = []
    right_passengers = []

    for passenger in passengers:
        if passenger['preference'] == 'left':
            left_passengers.append(passenger)
        elif passenger['preference'] == 'right':
            right_passengers.append(passenger)

    # Create weight matrix for the Hungarian Algorithm
    weight_matrix = []
    for left_passenger in left_passengers:
        row = []
        for right_passenger in right_passengers:
            weight_diff = abs(left_passenger['weight'] - right_passenger['weight'])
            row.append(weight_diff)
        weight_matrix.append(row)

    # Apply the Hungarian Algorithm to find the optimal assignment
    m = Munkres()
    indexes = m.compute(weight_matrix)

    # Assign passengers based on the optimal assignment
    left_assigned = [left_passengers[i] for i, _ in indexes]
    right_assigned = [right_passengers[j] for _, j in indexes]

    loading = {
        'left_side': left_assigned,
        'right_side': right_assigned,
    }
    print_optimal_loading_result(loading)

    return loading

def print_optimal_loading_result(loading):
    print("Optimal Loading Result:")

    print("Left | Right | Sum")
    for row in range(max(len(loading['left_side']), len(loading['right_side']))):
        left_passenger = loading['left_side'][row] if row < len(loading['left_side']) else None
        right_passenger = loading['right_side'][row] if row < len(loading['right_side']) else None

        left_name = left_passenger['name'] if left_passenger else ""
        right_name = right_passenger['name'] if right_passenger else ""
        weight_sum = left_passenger['weight'] + right_passenger['weight'] if (left_passenger and right_passenger) else 0

        print(f"{left_name} | {right_name} | {weight_sum}")
