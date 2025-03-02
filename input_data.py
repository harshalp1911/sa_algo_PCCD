# List of components
parts = ["Pedal", "Pins", "Lever", "Right case", "Shaft", "Bearing", "Retaining ring"]

# Interaction strength between parts (1 = very strong, 0 = no connection)
interaction_matrix = [
    [0, 0.8, 0.6, 0, 0.5, 0, 0],
    [0.8, 0, 0.9, 0, 0, 0.7, 0],
    [0.6, 0.9, 0, 0.4, 0, 0, 0],
    [0, 0, 0.4, 0, 0.3, 0, 0.9],
    [0.5, 0, 0, 0.3, 0, 0.7, 0],
    [0, 0.7, 0, 0, 0.7, 0, 0.6],
    [0, 0, 0, 0.9, 0, 0.6, 0]
]

# Relative motion constraints (1 = motion exists, so no merging)
relative_motion = [
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

# Define size constraints for the AM printer (L, W, H)
max_build_volume = (350, 250, 250)
