
### DRL Framework for Nanocluster Global Minimum Search 
Deep Reinforcement Learning (DRL) framework for exploring the potential energy surfaces of nanoclusters, efficiently identifying ground state and low-energy configurations, demonstrating exceptional adaptability and potential for advancing materials science.

### How to Run the Code

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f env_clusgym.yml
     ```

2. **Configure the Nanocluster Composition:**
     ```
   - For simulating a ternary nanocluster of  6 silver (Ag), 5 palladium (Pd) and 4 copper (Cu) atoms:
     eleNames = ['Ag', 'Pd','Cu']
     eleNums = [6, 5, 4]
     ```

3. **Run the Simulation:**
   - Execute the script using Python.
     ```bash
     python gym_trpo_single.py   
     ```


