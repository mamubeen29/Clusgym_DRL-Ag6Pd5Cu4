import matplotlib
matplotlib.use("Agg")
import gym
from clusgym import MCSEnv
import gym.wrappers
import numpy as np
import tensorforce
from tensorforce.agents import Agent
from tensorforce.execution import Runner
import os
import copy
from callback import Callback

# ---------------------------------------------------------------------------
# Compatibility fix: tensorforce 0.5.5 + TensorFlow 2.12
#
# TF 2.12 resets Module class-level variables to None. Restore only the ones
# that need a non-None value; leave the rest as None (their correct default).
# ---------------------------------------------------------------------------
from tensorforce.core.module import Module

Module.global_scope        = ''   # str  – root TF name scope
Module.scope_stack         = []   # list – push/pop during graph build
Module.while_counter       = 0    # int  – compared with > 0
Module.cond_counter        = 0    # int  – compared with > 0
Module.global_tensors_spec = {}   # dict – keyed tensor specs
Module.global_tensors      = {}   # dict – keyed tensor objects
Module.queryable_tensors   = {}   # dict – item assignment used
# global_summary_step, set_parent, inherit_* stay None — correct defaults

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
timesteps = 200

eleNames  = ['Ag','Cu']
eleNums   = [1,12]
clus_seed = None
save_dir  = 'result_' + ''.join(f"{name}{num}" for name, num in zip(eleNames, eleNums)) + '/'


def setup_env(recording=False):
    MCS_gym = MCSEnv(
        eleNames=eleNames,
        eleNums=eleNums,
        clus_seed=clus_seed,
        observation_fingerprints=True,
        save_dir=save_dir,
        timesteps=timesteps,
        save_every=1,
        n_unique_pool=25,
    )
    env = tensorforce.environments.OpenAIGym(
        MCS_gym,
        max_episode_timesteps=400,
        visualize=False,
    )
    return env


# ---------------------------------------------------------------------------
# Build the PPO agent
# ---------------------------------------------------------------------------
agent = Agent.create(
    agent='ppo',
    environment=setup_env(),
    batch_size=128,
    max_episode_timesteps=200,
    learning_rate=5e-4,
    subsampling_fraction=0.5,
    optimization_steps=4,
    likelihood_ratio_clipping=0.2,
    entropy_regularization=0.01,
    discount=0.99,
)

agent_spec = agent.spec
print(agent_spec)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
callback = Callback(save_dir).episode_finish

runner = Runner(
    agent=agent,
    environment=setup_env(recording=False),
    max_episode_timesteps=timesteps,
)

runner.run(num_episodes=5000, callback=callback, callback_episode_frequency=1)
runner.close()
