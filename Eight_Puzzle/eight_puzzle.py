import search
import random
from statistics import mean

class EightPuzzle(search.Problem):
    """Traditional sliding-tile puzzle. A state is represented as a tuple of characters, '_' and '1' through '8'.
    The first three characters are the top row, the next three the middle row, and the last three the bottom row.
    An action is represented as the index of the position where the blank is being moved."""

    def __init__(self, n):
        """The initial state is formed by making n random moves from the goal state. Note that the shortest distance to
        the goal may be less than n because some random moves 'cancel out' others."""
        self.initial = tuple('_12345678')
        for i in range(n):
            action = random.choice(self.actions(self.initial))
            self.initial = self.result(self.initial, action)

    def actions(self, state):
        """Returns the list of actions available from state."""
        grid = [(0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)]
        index_dict = dict(zip(grid, [0, 1, 2, 3, 4, 5, 6, 7, 8]))
        pos_dict = position_dict(state)
        x, y = pos_dict.get('_')
        acts = []
        if x + 1 <= 2:
            acts.append(index_dict.get((x + 1, y)))
        if x - 1 >= 0:
            acts.append(index_dict.get((x - 1, y)))
        if y + 1 <= 2:
            acts.append(index_dict.get((x, y + 1)))
        if y - 1 >= 0:
            acts.append(index_dict.get((x, y - 1)))
        return tuple(acts)

    def goal_test(self, state):
        """Returns true if state corresponds to _12345678."""
        return state == tuple('_12345678')

    def result(self, state, action):
        """Returns the state resulting from taking action in state."""
        new = list(state)
        # TODO You have to write the middle of this, modifying new
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


def misplaced(node):
    """8-puzzle heuristic returning the number of mismatched tiles."""
    # TODO You have to write this
    mismatched = 0
    state = node.state
    count = 0
    for i in state:
        if count == 0 and i != '_':
            mismatched += 1
        if count > 0 and i != str(count):
            mismatched += 1
        count += 1
    return mismatched


def manhattan(node):
    """8-puzzle heuristic returning the sum of Manhattan distance between tiles and their correct locations."""
    # TODO You have to write this
    dist = 0
    state = position_dict(node.state)
    goal = position_dict('_12345678')
    for s in goal:
        dist += abs(state.get(s)[0] - goal.get(s)[0])
        dist += abs(state.get(s)[1] - goal.get(s)[1])
    return dist


if __name__ == '__main__':
    # TODO This should be unchanged in the final program you hand in, but it might be useful to make a copy,
    # comment out one copy, and modify the other to get things to run more quickly while you're debugging
    depths = (1, 2, 4, 8, 16)
    trials = 100
    path_lengths = {}
    state_counts = {}
    for depth in depths:
        print('Gathering data for depth ' + str(depth) + '...')
        path_lengths[depth] = {'BFS': [], 'IDS': [], 'A*-mis': [], 'A*-Man': []}
        state_counts[depth] = {'BFS': [], 'IDS': [], 'A*-mis': [], 'A*-Man': []}
        for trial in range(trials):
            puzzle = EightPuzzle(depth)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['BFS'].append(len(search.breadth_first_search(p).path()))
            state_counts[depth]['BFS'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['IDS'].append(len(search.iterative_deepening_search(p).path()))
            state_counts[depth]['IDS'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['A*-mis'].append(len(search.astar_search(p, misplaced).path()))
            state_counts[depth]['A*-mis'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['A*-Man'].append(len(search.astar_search(p, manhattan).path()))
            state_counts[depth]['A*-Man'].append(p.states)
    print('Path lengths:')
    print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}'.format('Depth', 'BFS', 'IDS', 'A*-mis', 'A*-Man'))
    for depth in depths:
        print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}' \
              .format(depth,
                      mean(path_lengths[depth]['BFS']),
                      mean(path_lengths[depth]['IDS']),
                      mean(path_lengths[depth]['A*-mis']),
                      mean(path_lengths[depth]['A*-Man'])))
    print('Number of states generated (not counting initial state):')
    print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}'.format('Depth', 'BFS', 'IDS', 'A*-mis', 'A*-Man'))
    for depth in depths:
        print('{:>5}  {:>8.1f}  {:>8.1f}  {:>8.1f}  {:>8.1f}' \
              .format(depth,
                      mean(state_counts[depth]['BFS']),
                      mean(state_counts[depth]['IDS']),
                      mean(state_counts[depth]['A*-mis']),
                      mean(state_counts[depth]['A*-Man'])))
