grid = [(0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)]


def actions(state):
    """Returns the list of actions available from state."""
    # TODO You have to write this
    # Get current position of blank
    pos = state.index('_')
    if pos == 0:
        return 1, 3
    elif pos == 1:
        return 0, 2, 4
    elif pos == 2:
        return 1, 5
    elif pos == 3:
        return 0, 4, 6
    elif pos == 4:
        return 1, 3, 5, 7
    elif pos == 5:
        return 2, 4, 8
    elif pos == 6:
        return 3, 6
    elif pos == 7:
        return 4, 6, 8
    elif pos == 8:
        return 5, 7


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
    return dict(zip(list(state), pos))


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

print(prettify(s3))

"""
print(prettify(result(s3, 1)))
print(prettify(result(s3, 3)))
print(prettify(result(s3, 5)))
print(prettify(result(s3, 7)))
"""

print(actions(s3))
