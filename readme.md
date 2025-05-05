<!-- readme.md -->
## Part Consolidation Candidate Detection using Simulated Annealing

This project identifies optimal groups of components that can be consolidated into single parts while considering physical and functional constraints.

### Objective
- **Physical compatibility** (volume, material, dimensions)  
- **Inter-component relationships** (from influence matrix)  
- **Penalty** for over-grouping or incompatible merges  

Uses a Simulated Annealing (SA) meta-heuristic to explore the grouping space.

### Project Structure
├── run.py
├── component.py
├── cost_function.py
├── simulated_annealing.py
├── util.py
├── check-col.py
├── components.xlsx
├── initial_weights.xlsx
└── readme.md


### Usage
1. Install dependencies:
   ```bash
   pip install numpy pandas openpyxl
