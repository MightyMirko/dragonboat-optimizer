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
        'rows': []
    }

    for left, right in zip(left_assigned, right_assigned):
        row = {
            'left_passenger': left,
            'right_passenger': right,
            'sum_weight': left['weight'] + right['weight']
        }
        loading['rows'].append(row)

    print_optimal_loading_result(loading)

    return loading, loading["rows"]

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

def optimize_seating(loading):
    # Calculate the total weight of each row
    row_weights = []
    for row in loading:
        row_weight = sum(passenger['weight'] for passenger in row)
        row_weights.append(row_weight)

    # Sort the rows by their total weight in descending order
    sorted_rows = [row for _, row in sorted(zip(row_weights, loading), reverse=True)]

    # Assign seats to rows starting from the middle
    num_rows = len(sorted_rows)
    start_index = num_rows // 2
    seating_arrangement = [[] for _ in range(num_rows)]

    # Assign seats to rows, reducing weight disparity from center to edges
    for i in range(num_rows):
        row_index = (start_index + i) % num_rows
        row = sorted_rows[i]
        seating_arrangement[row_index] = row

    print_optimal_loading_result(seating_arrangement)
    return seating_arrangement
