# DRL Framework for Nanocluster Global Minimum Search
Rajesh K. Raju have developed DRL framework for exploring potetial energy surface via Deep Reinforcement Learning and we have utilized this framework for AgPdCu ternary nanocluster and predicted global minimum configuration. 
## Deep reinforcement learning unveils ternary nanocluster configurations: A case study on Ag6Pd5Cu4
https://pubs.aip.org/aip/jap/article/137/22/224301/3349243/Deep-reinforcement-learning-unveils-ternary
### Installation and usage

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f env_clusgym.yml
     ```
2. **Activate the Environment:**
   - Activate the `clusgym` environment by using the following command:
     ```bash
     conda activate clusgym
     ```
3. **Configure the Nanocluster Composition:**
   - Edit `gym_trpo_single.py` to select the nanocluster composition.
     
     For simulating a ternary nanocluster of  6 silver (Ag), 5 palladium (Pd) and 4 copper (Cu) atoms:
     ```bash
     eleNames = ['Ag', 'Pd','Cu']
     eleNums = [6, 5, 4]
     ```

4. **Run the Simulation:**
   - Execute the script using Python.
     ```bash
     python gym_trpo_single.py   
     ```
## Acknowledgements:
We would like to thank [Rajesh K. Raju](https://github.com/rajeshkochi444/clusgm_drl) for his DRL framework.

