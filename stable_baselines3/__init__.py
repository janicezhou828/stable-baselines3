import os

from stable_baselines3.a2c import A2C
from stable_baselines3.ppo import PPO
from stable_baselines3.sac import SAC

# Read version from file
version_file = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_file, "r") as file_handler:
    __version__ = file_handler.read().strip()
