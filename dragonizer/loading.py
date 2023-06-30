from munkres import Munkres
import numpy as np

class SeatingOptimizer:
    def __init__(self):
        self.m = Munkres()

    def minimize_row_delta(self, passengers):
        # Separate left and right passengers
        left_passengers = []
        right_passengers = []

        for passenger in passengers:
            if passenger['preference'] == 'left':
                left_passengers.append(passenger)
            elif passenger['preference'] == 'right':
                right_passengers.append(passenger)

        # Create a weight matrix for the Hungarian Algorithm
        weight_matrix = []
        for left_passenger in left_passengers:
            row = []
            for right_passenger in right_passengers:
                weight_diff = abs(left_passenger['weight'] - right_passenger['weight'])
                row.append(weight_diff)
            weight_matrix.append(row)
        # Apply the Hungarian Algorithm to find the optimal assignment
        indexes = self.m.compute(weight_matrix)

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
       # for i in loading['rows']:
            #print(i)
        #for i in loading['rows']:
        #    print(type(i))
        #    for key,value in i.items():
#
        #        print(value['weight'])
        return loading, loading["rows"]

    def print_optimal_seating_arrangement(self, seating_arrangement):
        print("Optimal Loading Result:")
        for row in seating_arrangement:
            left_passenger = row['left_passenger']
            right_passenger = row['right_passenger']
            sum_weight = row['sum_weight']

            left_name = left_passenger['name'] if left_passenger else ""
            right_name = right_passenger['name'] if right_passenger else ""

            print(f"{left_name} | {right_name} | {sum_weight}")

    def optimize_seating(self, rows):
        sorted_rows = sorted(rows, key=lambda x: x['sum_weight'], reverse=False)
        for i in sorted_rows:
            print(i)
        optimized_rows = np.empty(len(rows), dtype=object)       
        optimized_rows[4]= sorted_rows.pop()
        optimized_rows[5]= sorted_rows.pop() 
        optimized_rows[6]= sorted_rows.pop()
        optimized_rows[7]= sorted_rows.pop()
        optimized_rows[8]= sorted_rows.pop() 
        optimized_rows[3]= sorted_rows.pop()
        optimized_rows[2]= sorted_rows.pop()
        optimized_rows[1]= sorted_rows.pop()
        optimized_rows[0]= sorted_rows.pop()

        #for i in optimized_rows:
        #    print(i)
        self.print_optimal_seating_arrangement(optimized_rows)
        return optimized_rows
