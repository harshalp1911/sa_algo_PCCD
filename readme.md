Simulated Annealing for Part Consolidation in Additive Manufacturing

Project Overview

This project implements Simulated Annealing (SA) to optimize part consolidation in Additive Manufacturing (AM). The goal is to minimize the number of parts while satisfying constraints like relative motion, material compatibility, and size limitations. In future work, a Genetic Algorithm (GA) will be implemented for comparative analysis.

Project Structure

📁 SA_Part_Consolidation
│── main.py               # Runs the entire SA optimization
│── sa_algo.py        # Contains the SA logic
│── cost_function.py       # Defines the cost function
│── input_data.py          # Stores component details & constraints
│── results_analysis.py    # Compares SA with future GA implementation (Optional)
│── README.md              # Project description & usage

How It Works

Input Data:

Define the list of parts and their interaction strengths.

Store constraints (e.g., motion restrictions, material compatibility, size limits).

Simulated Annealing Process:

Initialize: Start with each part separate.

Cost Function: Evaluates the quality of a solution.

Neighbor Generation: Randomly merges parts to explore new solutions.

Acceptance Criteria: Accepts new solutions based on temperature.

Cooling Schedule: Gradually lowers temperature to refine the solution.

Early Stopping: Stops when no improvement occurs for a set number of iterations.

