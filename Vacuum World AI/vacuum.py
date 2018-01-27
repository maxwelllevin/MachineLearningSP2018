# See bottom of file for instructions

import matplotlib
matplotlib.use("TkAgg")  # This seems necessary for the animation to work within PyCharm
import matplotlib.pyplot as plt
import numpy as np
import random

WORLD_WIDTH = 25  # Width, in squares, of the world

# These are used by apply to update the agent's location
OFFSETS = {'north': (-1, 0),
           'south': (1, 0),
           'east': (0, 1),
           'west': (0, -1)}

# These are used by animate and draw_world to draw the world in color
EMPTY = 0.0
DIRT = 0.33
OBSTACLE = 0.67
AGENT = 1.0
cmap = matplotlib.colors.ListedColormap(['white', 'orange', 'black', 'blue'])
norm = matplotlib.colors.BoundaryNorm([0.0, 0.25, 0.5, 0.75, 1.0], cmap.N)


def random_world():
    """Creates and returns a random world."""
    # Create empty world
    grid = np.zeros((WORLD_WIDTH, WORLD_WIDTH))
    # Add dirt and obstacles
    for r in range(WORLD_WIDTH):
        for c in range(WORLD_WIDTH):
            if random.random() < 0.5:
                grid[r, c] = DIRT
            elif random.random() < 0.1:
                grid[r, c] = OBSTACLE
    # Place agent
    while True:
        r = random.randrange(WORLD_WIDTH)
        c = random.randrange(WORLD_WIDTH)
        if grid[r, c] == EMPTY:
            return grid, r, c


def get_percept(grid, r, c):
    """Returns the percept for an agent at position r, c on grid: 'dirty' or 'clean'."""
    if grid[r, c] == DIRT:
        return 'dirty'
    else:
        return 'clean'


def draw_world(grid, r, c, image):
    """Updates image, showing grid with the agent at r, c."""
    under = grid[r, c]
    grid[r, c] = AGENT
    image.set_data(grid)
    grid[r, c] = under


def apply(grid, r, c, action):
    """Applies action ('suck', 'north', etc.) for an agent at position r, c on grid."""
    if action == 'suck':
        grid[r, c] = EMPTY
    else:
        new_r = r + OFFSETS[action][0]
        new_c = c + OFFSETS[action][1]
        if 0 <= new_r < WORLD_WIDTH and 0 <= new_c < WORLD_WIDTH and grid[new_r, new_c] != OBSTACLE:
            return new_r, new_c
    return r, c


def animate(agent, steps, initialize=None):
    """Animates an agent's performance in a random world for the specified number of steps. initialize is called
    once to provide additional parameters to the agent."""
    grid, r, c = random_world()
    image = plt.imshow(grid, cmap=cmap, norm=norm)
    if initialize:
        state = initialize()
    for t in range(steps):
        draw_world(grid, r, c, image)
        percept = get_percept(grid, r, c)
        if initialize:
            action, *state = agent(percept, *state)
        else:
            action = agent(percept)
        r, c = apply(grid, r, c, action)
        plt.pause(0.0001)
    plt.show()


def score(grid):
    """Returns the number of non-dirty squares in grid."""
    result = 0
    for r in range(WORLD_WIDTH):
        for c in range(WORLD_WIDTH):
            if grid[r, c] != DIRT:
                result += 1
    return result


def simulate(agent, steps, initialize=None):
    """Simulates an agent's performance in a random world for the specified number of steps. Returns the total score
    over this time. initialize is called once to provide additional parameters to the agent."""
    grid, r, c = random_world()
    if initialize:
        state = initialize()
    result = 0
    for t in range(steps):
        result += score(grid)
        percept = get_percept(grid, r, c)
        if initialize:
            action, *state = agent(percept, *state)
        else:
            action = agent(percept)
        r, c = apply(grid, r, c, action)
    return result


def experiment(agent, steps, runs, initialize=None):
    """Repeatedly simulates agent in runs random worlds for the specified number of steps each. Returns the average
    score across runs. initialize is called at the beginning of each run to provide additional parameters to the
    agent."""
    result = 0
    for r in range(runs):
        result += simulate(agent, steps, initialize)
    return result / runs


"""
INSTRUCTIONS:

You must define four functions here: reflex_agent, random_agent, state_agent, and init_state_agent

reflex_agent and random_agent each take a percept ('clean' or 'dirty') and return an action ('suck', 'north',
'south', 'east', or 'west').

state_agent takes a percept and any number of additional parameters recording the agent's state. It returns
an action plus updated versions of these parameters.

init_state_agent returns the original state parameters for state_agent.
"""


# Uncomment one of these to animate one of your agents
#animate(reflex_agent, 1000)
#animate(random_agent, 1000)
#animate(state_agent, 1000, init_state_agent)

# Uncomment these to run experiments comparing performance of different agents
# NOTE: This will take a while!
#print('Reflex agent: ', experiment(reflex_agent, 10000, 20))
#print('Random agent: ', experiment(random_agent, 10000, 20))
#print('State agent: ', experiment(state_agent, 10000, 20, init_state_agent))
