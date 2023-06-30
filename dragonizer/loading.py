from munkres import Munkres
import json, yaml

### 
"""@package docstring
Documentation for this module.

More details.
"""
class Passenger:
    """
    Diese Klasse soll einen Passagieren abbilden. Ein Passagier hat Gewicht, einen Namen, Partner, präferierte Paddelseite und die zugewiesene Position sowie den präferierten Bereich (Maschinenraum, Heck, Bug)
    """
    def __init__(self, name, weight, preference, partner="", preferred_area=""):
        self.name = name
        self.weight = weight
        self.preference = preference  # backbord links, steuerbord rechts
        ## tbd :todo:
        self.optimized_position = (self.preference, 0)
        self.partner = partner
        self.preferred_area = preferred_area

### 
class DragonBoat:
    """
    Diese Klasse soll das Drachenboot mit Trommler, Steuermann und 9 Reihen je 2 Passagiere abbilden. Es soll das Gesamtgewicht, das Gewicht linke und rechte Seite abbilden.
    """
    def __init__(self,name):
        """
        constructor
        """
        self.boatname = name
        self.m = Munkres()
        self.team = []
        self.rows = []
        self.left = []
        self.right = []
        
    
    def parse_passenger_data(self, data):
        try:
            for passenger in json.loads(data):
                self.team.append(passenger)

        except ValueError:
            try:
                for passenger in yaml.loads(data):
                    self.team.append(passenger)
            except yaml.YAMLError:
                return None
    def get_team_seating(self):
        """
        Zuordnung linke und rechte Seite"""
        for passenger in self.team:
            if passenger.preference == "left":
                self.left.append(passenger)
            elif passenger.preference == "right":
                self.right.append(passenger)

    
        for left, right in zip(self.left, self.right):
            row = {
                "left_passenger": left,
                "right_passenger": right,
                "sum_weight": left.weight + right.weight,
            }
            loading["rows"].append(row)        
class SeatOptimizer:
    """
    Diese Klasse soll die Passagierdaten nehmen und die günstigste links-rechts-Zuordnung finden. 
    """
    def minimize_row_delta(self, boat:DragonBoat):
        left_passengers = DragonBoat.left
        right_passengers = []

        for passenger in self.team:
            if passenger.preference == "left":
                left_passengers.append(passenger)
            elif passenger.preference == "right":
                right_passengers.append(passenger)

        weight_matrix = []
        for left_passenger in left_passengers:
            row = []
            for right_passenger in right_passengers:
                weight_diff = abs(left_passenger.weight - right_passenger.weight)
                row.append(weight_diff)
            weight_matrix.append(row)

        indexes = self.m.compute(weight_matrix)

        left_assigned = [left_passengers[i] for i, _ in indexes]
        right_assigned = [right_passengers[j] for _, j in indexes]

        loading = {
            "left_side": left_assigned,
            "right_side": right_assigned,
            "rows": [],
        }

        for left, right in zip(left_assigned, right_assigned):
            row = {
                "left_passenger": left,
                "right_passenger": right,
                "sum_weight": left.weight + right.weight,
            }
            loading["rows"].append(row)

        return loading, loading["rows"]

    def print_optimal_seating_arrangement(self, seating_arrangement):
        print("Optimal Loading Result:")
        for row in seating_arrangement:
            left_passenger = row["left_passenger"]
            right_passenger = row["right_passenger"]
            sum_weight = row["sum_weight"]

            left_name = left_passenger.name if left_passenger else ""
            right_name = right_passenger.name if right_passenger else ""

            print(f"{left_name} | {right_name} | {sum_weight}")

    def optimize_seating(self, rows):
        """
        Erstmal nur sortiert von schwer nach leicht"""
        sorted_rows = sorted(rows, key=lambda x: x["sum_weight"], reverse=True)
        seating_arrangement = sorted_rows
        """
        num_rows = len(sorted_rows)
        seating_arrangement = [[] for _ in range(num_rows)]

        start_index = num_rows // 2

        for i in range(num_rows):
            row_index = (start_index + i) % num_rows
            seating_arrangement[row_index] = sorted_rows[i]
        """
        

        return seating_arrangement
