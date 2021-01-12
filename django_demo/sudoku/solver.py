import re


def solved(values):
    """Checks if a sudoku puzzle is solved or unsolvable, returns -1 if unsolvable, 1 if solved and 0 if not solved"""
    for u in values:
        if len(values[u]) < 1:
            return -1
        elif len(values[u]) > 1:
            return 0
    return 1


def clear():
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')


class Solver():
    """The improved Solver class handles solving of the sudoku puzzle"""
    digits = '123456789'
    rows = 'ABCDEFGHI'

    # A, B are two charactor arrays
    def cross(self, A, B):
        "self.cross product of elements in A and elements in B."
        return [a + b for a in A for b in B]

    def __init__(self):
        self.cols = self.digits
        # 9x9 self.squares in a list
        self.squares = self.cross(self.rows, self.cols)

        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                    [self.cross(r, self.cols) for r in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.squares)

        # each square has 20 self.peers in its row, column and block in a set
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)


    #
    # resolver
    #
    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, {square: self.digits}, or
        return False if a contradiction is detected."""
        # initial values, every square can be any digit; then assign values (123456789) to each square
        values = dict((s, self.digits) for s in self.squares)

        # iterate through each square
        for s, d in self.grid_values(grid).items():
            # if square has a digit, update all its self.peers to remove this digit from the candidate list
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    # build a dict of square->value for display
    def grid_values(self, grid):
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."
        chars = [c for c in grid if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    # main function of the resolver
    def eliminate(self, values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values  ## Already eliminated

        # d is a candidate in square s, now eliminate it, and process further job on its self.peers
        values[s] = values[s].replace(d, '')

        ## (1) If a square s is reduced to one value d2, then eliminate d2 from the self.peers.
        if len(values[s]) == 0:
            return False  ## Contradiction: removed last value
        elif len(values[s]) == 1:
            d2 = values[s]  # square s is resolved. now remove its digit from all its self.peers
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False

        ## (2) If a unit u is reduced to only one place for a value d, then put it there.
        for u in self.units[s]:
            dplaces = [x for x in u if d in values[x]]
            if len(dplaces) == 0:
                return False  ## Contradiction: no place for this value
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def display(self, values):
        "Display these values as a 2-D grid."
        width = 1 + max(len(values[s]) for s in self.squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in self.rows:
            print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                          for c in self.cols))
            if r in 'CF': print(line)
        print

    def search(self, values, p_s="", p_d=""):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False  ## Failed earlier

        if all(len(values[s]) == 1 for s in self.squares):
            return values  ## Solved!

        ## Chose the unfilled square s with the fewest possibilities
        n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d), s, d)
                    for d in values[s])

    def solve(self, grid):
        return self.search(self.parse_grid(grid))

    def some(self, seq):
        "Return some element of seq that is true."
        for e in seq:
            if e: return e
        return False


def main():
    unresolvable = """
    600008940
    900006100
    070040000
    200610000
    000000200
    089002000
    000060005
    000000030
    800001600
    """
    original_grid = unresolvable
    grid = re.sub(r'[^.0-9]', "", original_grid)
    print(grid)

    solver = Solver()

    print("\nsudoku: ")
    #solver.display(solver.grid_values(grid))

    print("\nresult: ")
    # display(parse_grid(grid))

    #print(solver.solve(grid))
    solver.display(solver.solve(grid))

if __name__ == "__main__":
    main()