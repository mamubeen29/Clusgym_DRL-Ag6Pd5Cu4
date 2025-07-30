
### DRL Framework for Nanocluster Global Minimum Search 
### Deep reinforcement learning unveils ternary nanocluster configurations: A case study on Ag6Pd5Cu4
https://pubs.aip.org/aip/jap/article/137/22/224301/3349243/Deep-reinforcement-learning-unveils-ternary
### How to Run the Code

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f env_clusgym.yml
     ```

2. **Configure the Nanocluster Composition:**
     ```
     For simulating a ternary nanocluster of  6 silver (Ag), 5 palladium (Pd) and 4 copper (Cu) atoms:
     eleNames = ['Ag', 'Pd','Cu']
     eleNums = [6, 5, 4]
     ```

3. **Run the Simulation:**
   - Execute the script using Python.
     ```bash
     python gym_trpo_single.py   
     ```


