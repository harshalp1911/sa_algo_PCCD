'''import numpy as np
import random
import math
from cost_function import cost_function
from input_data import parts

# Simulated Annealing Parameters
initial_temp = 100  
cooling_rate = 0.95  
min_temp = 1  
max_iterations = 500  

# Generate a neighboring solution (randomly merge two parts)
def generate_neighbor(solution):
    """Create a new solution by merging two parts."""
    new_solution = solution.copy()
    idx1, idx2 = random.sample(range(len(solution)), 2)
    if new_solution[idx1] != new_solution[idx2]:  # Ensure different groups
        new_solution[idx2] = new_solution[idx1]  # Merge
    return new_solution  

# Simulated Annealing Algorithm
def simulated_annealing(initial_solution):
    """Performs simulated annealing to find optimal part consolidation."""
    current_solution = initial_solution.copy()
    best_solution = initial_solution.copy()
    current_temp = initial_temp

    while current_temp > min_temp:
        for _ in range(max_iterations):
            new_solution = generate_neighbor(current_solution)
            delta_e = cost_function(new_solution) - cost_function(current_solution)
            
            if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / current_temp):
                current_solution = new_solution.copy()
                if cost_function(current_solution) < cost_function(best_solution):
                    best_solution = current_solution.copy()
        
        current_temp *= cooling_rate  # Reduce temperature
    
    return best_solution  
'''

import numpy as np
import random
import math
from cost_function import cost_function
from input_data import parts

# Simulated Annealing Parameters
initial_temp = 100  
cooling_rate = 0.95  
min_temp = 1  
max_no_improve = 50  # If no improvement for 50 iterations, stop

def generate_neighbor(solution):
    """Create a new solution by merging two parts."""
    new_solution = solution.copy()
    idx1, idx2 = random.sample(range(len(solution)), 2)
    if new_solution[idx1] != new_solution[idx2]:  # Ensure different groups
        new_solution[idx2] = new_solution[idx1]  # Merge
    return new_solution  

def simulated_annealing(initial_solution):
    """Performs simulated annealing with adaptive stopping."""
    current_solution = initial_solution.copy()
    best_solution = initial_solution.copy()
    current_temp = initial_temp
    best_cost = cost_function(best_solution)
    no_improve_count = 0  # Tracks stagnation
    
    iteration = 0  # Track actual iterations

    while current_temp > min_temp:
        for _ in range(100):  # Inner loop to explore solutions
            iteration += 1  
            new_solution = generate_neighbor(current_solution)
            new_cost = cost_function(new_solution)
            delta_e = new_cost - cost_function(current_solution)
            
            if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / current_temp):
                current_solution = new_solution.copy()
                
                if new_cost < best_cost:
                    best_solution = current_solution.copy()
                    best_cost = new_cost
                    no_improve_count = 0  # Reset no improvement counter
                else:
                    no_improve_count += 1  # Increment stagnation count
            
            # **Early stopping condition**
            if no_improve_count >= max_no_improve:
                print(f"Stopping early at iteration {iteration}, no improvement for {max_no_improve} steps.")
                return best_solution  

        current_temp *= cooling_rate  # Reduce temperature

    print(f"Finished at iteration {iteration}, final cost: {best_cost}")
    return best_solution  
