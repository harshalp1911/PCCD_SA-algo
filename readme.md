## Part Consolidation Candidate Detection using Simulated Annealing 
This project identifies optimal groups of components that can be consolidated in a mechanical or manufacturing assembly using a metaheuristic approach. The goal is to minimize complexity and cost by merging feasible parts while considering physical and functional constraints.

## Objective
To find groups of components that are feasible to merge based on:

- Physical compatibility (volume, material, dimensions)

- Inter-component relationships (from influence matrix)

- Penalty for over-grouping or incompatible merges

The system uses the Simulated Annealing (SA) algorithm to explore the solution space and identify the best combination of parts to consolidate


## 📁 Project Structure

File/Folder	Description
components.xlsx	        :    Contains component attributes (e.g., name, volume, material)
initial_weights.xlsx	:    Influence/relationship matrix between components
component.py	        :    Class representing a component and its properties
util.py	                :    Utility functions for loading data from Excel files
app.py	                :    Core simulation logic for iterative updates
run.py	                :    Entrypoint to run the simulation
simulated_annealing.py	:    Simulated Annealing logic to search for optimal merges
cost_function.py	    :    Defines the cost function that evaluates merge feasibility
merger.py (optional)	:    Handles merge/split operations for groups of components
README.md	            :    This file


# 🧮 Algorithm Overview

1. Initialize components and weights from Excel files

2. Define a cost function to evaluate a candidate grouping

3. Use Simulated Annealing to iteratively:

    - Propose a new grouping (merge or split)

    - Evaluate new cost

    - Accept or reject based on cost and temperature

4. Output the best grouping configuration

## 🧾 Input Format

### initial_weights.xlsx
    A square matrix where entry (i,j) indicates the influence of component i on j.


## 📤 Output
Final grouping of components (e.g., [[C1, C2], [C3], [C4, C5]])

Final cost (indicating merge feasibility)
Optionally: matrix visualization or CSV export

## 📌 Customization
Modify cost_function.py to tweak scoring rules

Adjust SA parameters in simulated_annealing.py:

Initial temperature

Cooling rate

Number of iterations

