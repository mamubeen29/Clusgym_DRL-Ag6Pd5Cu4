# DRL Framework for Nanocluster Global Minimum Search
This repository contains the implementation of the Deep reinforcement learning (DRL) agent, employed for the identification of Ag6Pd5Cu4 nanocluster using Deep Reinforcement Learning (DRL). The aims is to efficiently explore GM nanocluster configuration. This is an adapted version of the DRL framework from [clusgym_drl](https://github.com/rajeshkochi444/clusgm_drl) J. Phys. Chem. A 2024, 128, 42, 9122–9134. We thank the authors for making the code available on github. However, our framework has been adapted to tackle the additional challenges. We modified the code to work with ternary nanocluster. 

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
The code is adapted from [clusgym_drl](https://github.com/rajeshkochi444/clusgm_drl). We thank the authors for making the code available on github. We would like to thank [Rajesh K. Raju](https://github.com/rajeshkochi444/clusgm_drl) for his DRL framework.

