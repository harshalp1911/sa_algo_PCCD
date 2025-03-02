import numpy as np
from input_data import interaction_matrix, relative_motion

def cost_function(solution):
    """Calculates the cost of a given part consolidation solution."""
    part_count = len(set(solution))  # Number of unique groups
    penalty = 0

    # Penalty for merging parts with relative motion
    for i in range(len(solution)):
        for j in range(len(solution)):
            if relative_motion[i][j] == 1 and solution[i] == solution[j]:
                penalty += 100  # Large penalty to prevent merging

    # Add penalty for exceeding build volume (placeholder)
    # if exceeds_size_limit(solution):
    #     penalty += 50  

    return part_count + penalty  # Lower cost is better
