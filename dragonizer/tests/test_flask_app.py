import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_seating_optimization(self):
        passengers = [
    {"weight": 75, "name": "Passenger1", "preference": "left"},
    {"weight": 78, "name": "Passenger10", "preference": "right"},
    {"weight": 70, "name": "Passenger2", "preference": "left"},
    {"weight": 80, "name": "Passenger11", "preference": "right"},
    {"weight": 95, "name": "Passenger3", "preference": "left"},
    {"weight": 63, "name": "Passenger12", "preference": "right"},
    {"weight": 80, "name": "Passenger4", "preference": "left"},
    {"weight": 85, "name": "Passenger13", "preference": "right"},
    {"weight": 92, "name": "Passenger5", "preference": "left"},
    {"weight": 93, "name": "Passenger14", "preference": "right"},
    {"weight": 75, "name": "Passenger6", "preference": "left"},
    {"weight": 83, "name": "Passenger15", "preference": "right"},
    {"weight": 68, "name": "Passenger7", "preference": "left"},
    {"weight": 94, "name": "Passenger16", "preference": "right"},
    {"weight": 92, "name": "Passenger8", "preference": "left"},
    {"weight": 83, "name": "Passenger17", "preference": "right"},
    {"weight": 71, "name": "Passenger9", "preference": "left"},
    {"weight": 95, "name": "Passenger18", "preference": "right"}
]
