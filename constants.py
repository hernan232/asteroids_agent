# Deep Q learning constants
BATCH_SIZE = 32
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.1
TARGET_UPDATE = 2500
REPLAY_MEMORY_SIZE = 1000000
LEARNING_RATE = 0.00025
MOMENTUM = 0.95

# Game parameters
INITIAL_LIVES = 4

# Input image constants
STATE_IMG_WIDTH = 84
N_IMAGES_PER_STATE = 8
STATE_IMG_HEIGHT = 84

# Training constants
N_EPISODES = 2000
N_TIMESTEP_PER_EP = 6000
STEPS_PER_EPOCH = 5000

# Test constants
TEST_EPSILON = 0.05
N_TEST_STEPS = 8000
N_STEPS_FIXED_STATES = 5000

# Interface
SHOW_SCREEN = True
PLOT_LOSS = False
PLOT_Q = True
SECONDS_SLEEP = 0.01

# Files
PERIODIC_SAVE = 5000


