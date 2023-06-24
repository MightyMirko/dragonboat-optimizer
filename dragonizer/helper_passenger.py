import random

passengers = []

for i in range(1, 10):
    passengers.append({'weight': random.randint(55, 100), 'name': f"Passenger{i}", 'preference': 'left'})
    passengers.append({'weight': random.randint(55, 100), 'name': f"Passenger{i + 9}", 'preference': 'right'})


print(passengers)

