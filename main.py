from sa_algo import simulated_annealing
from input_data import parts

# Initial state: each part is separate
initial_solution = list(range(len(parts)))

# Run SA
optimized_solution = simulated_annealing(initial_solution)

# Print results
#print("Optimized Consolidation:", optimized_solution)
from input_data import parts

# Create a dictionary mapping groups to part names
grouped_parts = {}
for idx, group in enumerate(optimized_solution):
    if group not in grouped_parts:
        grouped_parts[group] = []
    grouped_parts[group].append(parts[idx])

# Print groups in a readable format
for group, part_list in grouped_parts.items():
    print(f"Group {group}: {part_list}")

