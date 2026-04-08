## Clusgm-DRL: A Proximal Policy Optimization (PPO) framework for global minimum (GM) search on nanocluster potential energy surfaces (PES)
The framework models cluster optimization as a sequential decision-making process. An agent iteratively perturbs atomic coordinates (state St), receives the resulting energy (reward Rt), and updates its policy to favor moves that lower potential energy. Initially developed with Trust Region Policy Optimization (TRPO) in [clusgym_drl](https://github.com/rajeshkochi444/clusgm_drl) J. Phys. Chem. A 2024, 128, 42, 9122–9134. We thank the authors for making the code available on github. The framework has been upgraded to PPO to overcome TRPO’s computational bottlenecks and improve sample efficiency. The PPO update employs a clipped surrogate objective to constrain policy updates, enabling stable training on high-dimensional PES landscapes across diverse cluster types. 

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
   - Edit `gym_trpo_single.py` for TRPO to select the nanocluster composition.
   - Edit `gym_ppo_single.py` for PPO to select the nanocluster composition.
     
     For simulating a ternary nanocluster of  6 silver (Ag), 5 palladium (Pd) and 4 copper (Cu) atoms:
     ```bash
     eleNames = ['Ag', 'Pd','Cu']
     eleNums = [6, 5, 4]
     ```

4. **Run the Simulation:**
   - Execute the script using Python for TRPO.
     ```bash
     python gym_trpo_single.py   
     ```
   - Execute the script using Python for PPO.
     ```bash
     python gym_ppo_single.py   
     ```
## Acknowledgements:
The code is adapted from [clusgym_drl](https://github.com/rajeshkochi444/clusgm_drl). We thank the authors for making the code available on github. We would like to thank [Rajesh K. Raju](https://github.com/rajeshkochi444/clusgm_drl) for his DRL framework.

