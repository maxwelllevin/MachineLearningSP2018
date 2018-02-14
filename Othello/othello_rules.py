from copy import deepcopy


def diagram_to_state(diagram):
	"""Converts a list of strings into a list of lists of characters (strings of length 1.)"""
	return [list(a) for a in diagram]


INITIAL_STATE = diagram_to_state(['........',
                                  '........',
                                  '........',
                                  '...#O...',
                                  '...O#...',
                                  '........',
                                  '........',
                                  '........'])



def count_pieces(state):
	"""Returns a dictionary of the counts of '#', 'O', and '.' in state."""
	d = { '#': 0, 'O': 0, '.': 0 }
	for a in state:
		for b in a:
			d[b] = d[b] + 1
	return d


def prettify(state):
	"""
	Returns a single human-readable string representing state, including row and column indices and counts of each color.
"""
	count = count_pieces(state)
	pound_count = count.get('#')
	oh_count = count.get('O')
	dot_count = count.get('.')
	pretty = ' 01234567\n' + \
		'0' + state[0] + '0\n' + \
		'1' + state[1] + '1\n' + \
		'2' + state[2] + '2\n' + \
		'3' + state[3] + '3\n' + \
		'4' + state[4] + '4\n' + \
		'5' + state[5] + '5\n' + \
		'6' + state[6] + '6\n' + \
		'7' + state[7] + '7\n' + \
		' 01234567\n' + \
		"{'#': " + pound_count + ", 'O': " + oh_count + ", '.': " + dot_count + "}\n"
	return pretty


def opposite(color):
	"""opposite('#') returns 'O'. opposite('O') returns '#'."""
	# TODO You have to write this
	if color == '#':
		return 'O'
	else:
		return '#'

def flips(state, r, c, color, dr, dc):
    """
    Returns a list of pieces that would be flipped if color played at r, c, but only searching along the line
    specified by dr and dc. For example, if dr is 1 and dc is -1, consider the line (r+1, c-1), (r+2, c-2), etc.

    :param state: The game state.
    :param r: The row of the piece to be  played.
    :param c: The column of the piece to be  played.
    :param color: The color that would play at r, c.
    :param dr: The amount to adjust r on each step along the line.
    :param dc: The amount to adjust c on each step along the line.
    :return A list of (r, c) pairs of pieces that would be flipped.
    """
    # TODO You have to write this


OFFSETS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def flips_something(state, r, c, color):
    """Returns True if color playing at r, c in state would flip something."""
    # TODO You have to write this


def legal_moves(state, color):
    """
    Returns a list of legal moves ((r, c) pairs) that color can make from state. Note that a player must flip
    something if possible; otherwise they must play the special move 'pass'.
    """
    # TODO You have to write this


def successor(state, move, color):
    """
    Returns the state that would result from color playing move (which is either a pair (r, c) or 'pass'.
    Assumes move is legal.
    """
    # TODO You have to write this


def score(state):
    """
    Returns the scores in state. More positive values (up to 64 for occupying the entire board) are better for '#'.
    More negative values (down to -64) are better for 'O'.
    """
    # TODO You have to write this


def game_over(state):
    """
    Returns true if neither player can flip anything.
    """
    # TODO You have to write this