# Simulated Annealing for Part Consolidation in Additive Manufacturing
## Project Overview
 > This project implements Simulated Annealing (SA) to optimize part consolidation in Additive Manufacturing (AM). The goal is to minimize the number of parts while satisfying constraints like relative motion, material compatibility, and size limitations. In future work, a Genetic Algorithm (GA) will be implemented for comparative analysis.

## Project Structure 📋
```
📁 SA_Part_Consolidation  
│── main.py               # Runs the entire SA optimization  
│── sa_algorithm.py        # Contains the SA logic  
│── cost_function.py       # Defines the cost function  
│── input_data.py          # Stores component details & constraints  
│── README.md              # Project description & usage  
```

## Output 📈

``1.  Displays the optimized part consolidation.``

``2. Shows the number of parts before and after optimization.``

``3. Indicates if early stopping occurred.``

## Installation & Usage📂
### Requirements

``Ensure you have Python installed along with the required libraries:``

```
pip install numpy
```

### Run the Optimization 

Execute the main script:
```bash
python main.py
 ```

### Expected Output Format:
```python
Initial Part Count: 10  
Optimized Part Count: 5  
Optimized Consolidation: [('Pedal', 'Lever'), ('Shaft', 'Right Case'), ('Pins', 'Bearing')]  
Stopping early at iteration 243, no improvement for 50 steps.
```


### Future Work

> * Implement Genetic Algorithm (GA) for comparison.

>* Integrate CAD data extraction for automatic FPI network generation.

> * Improve visualization with plots (cost vs. iteration, part groupings).

## Contributors

 Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


@ Harshal Patil






## License

[MIT](https://choosealicense.com/licenses/mit/)
