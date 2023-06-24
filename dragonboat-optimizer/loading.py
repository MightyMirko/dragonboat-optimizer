def optimal_loading(passengers):
    """
    Function to determine the optimal loading of passengers in an aircraft or dragon boat.

    Args:
        passengers (list): List of dictionaries representing passengers with their weight and position.

    Returns:
        dict: Dictionary containing the optimal loading configuration with passengers divided into left and right sides.

    """

    # Sort passengers based on weight in descending order
    passengers = sorted(passengers, key=lambda x: x['weight'], reverse=True)
    
    # Group passengers based on their position (front, middle, back)
    groups = {'front': [], 'middle': [], 'back': []}

    for passenger in passengers:
        group = passenger['position']
        groups[group].append(passenger)

    left_side = []
    right_side = []

    # Load passengers alternately on left and right sides
    for group in groups.values():
        group = sorted(group, key=lambda x: x['weight'])
        num_passengers = len(group)
        for i, passenger in enumerate(group):
            if i < num_passengers // 2:
                left_side.append(passenger)
            else:
                right_side.append(passenger)

    loading = {'left': left_side, 'right': right_side}
    return loading
