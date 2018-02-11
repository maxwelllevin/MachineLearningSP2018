grid = [(0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)]


def actions(state):
    """Returns the list of actions available from state."""
    # Store our available actions in this list
    acts = []

    # Map grid points (x,y) to proper indices
    index_dict = dict(zip(grid, [0, 1, 2, 3, 4, 5, 6, 7, 8]))

    # Map state to grid points (x,y)
    pos_dict = position_dict(state)

    # Print the grid location of '_'
    # print(list(pos_dict.get('_')))

    # Get the grid coordinates of '_'
    x, y = pos_dict.get('_')

    # Add available actions to our list
    if x + 1 <= 2:
        acts.append(index_dict.get((x + 1, y)))
    if x - 1 >= 0:
        acts.append(index_dict.get((x - 1, y)))
    if y + 1 <= 2:
        acts.append(index_dict.get((x, y + 1)))
    if y - 1 >= 0:
        acts.append(index_dict.get((x, y - 1)))
    return tuple(acts)


def result(state, action):
    """Returns the state resulting from taking action in state."""
    new = list(state)
    # TODO You have to write the middle of this, modifying new # Works
    if action != new.index('_'):
        new[state.index('_')] = state[action]
        new[action] = '_'
    return tuple(new)


def prettify(state):
    """Returns a more human-readable grid representing state."""
    result = ''
    for i, tile in enumerate(state):
        result += tile
        if i % 3 == 2:
            result += '\n'
    return result


def position_dict(state):
    """Returns a dictionary that maps values to positions. Useful for manhattan."""
    pos = [(0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)]
    return dict(zip(state, pos))


def misplaced(state):
    """8-puzzle heuristic returning the number of mismatched tiles."""
    # TODO You have to write this
    mismatched = 0
    state = state
    count = 0
    for i in state:
        if count == 0 and i != '_':
            mismatched += 1
        if count > 0 and i != str(count):
            mismatched += 1
        count += 1
    return mismatched


def manhattan(state):
    """8-puzzle heuristic returning the sum of Manhattan distance between tiles and their correct locations."""
    # TODO You have to write this
    dist = 0
    state = position_dict(state)
    goal = position_dict('_12345678')
    for s in goal:
        dist += abs(state.get(s)[0] - goal.get(s)[0])
        dist += abs(state.get(s)[1] - goal.get(s)[1])
    return dist


s1 = '_12345678'  # Solved
s2 = '_87654321'  # Reverse Solved
s3 = '1234_5678'  # Space in middle
s4 = '123456_78'  # Space bottom left
s5 = '1234567_8'  # Space bottom middle

active = s3

print(prettify(active))

"""
print(prettify(result(s3, 1)))
print(prettify(result(s3, 3)))
print(prettify(result(s3, 5)))
print(prettify(result(s3, 7)))
"""

print(misplaced(active))
