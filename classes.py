""" The Game class definition for a simulation of Conway's Game of Life.

The governing rules can be expressed as:
    1. A cell with fewer than two live neighbors will be set to off.
    2. A cell with two live neighbors will retain its state.
    3. A cell with three live neighbors will be set to on.
    4. A cell with more than three live neighbors will be set to off.
"""

from itertools import product

RANGE_MAX = 42

def neighbors((x, y)):
    """ This function returns the 2D neighborhood around x-y-coords.
    """

    return [c for c in product(range(x-1, x+2), range(y-1, y+2)) if c != (x, y)]


class Game:
    """ Game organizes data around live cells and all relevant neighbors,
        and contains logic to update state in the tick method.

        The game will store a set of live cells.

        The state will be updated by the tick method.
        The tick method will inspect each live cell.
            - First the neighbors will be identified.
            - Second the number of live neighbors (nln) will be counted.
                - If the number of live neighbors is 2 or 3, the cell lives.
            - Third, each neighbor is examined, and again nln is computed.
                - If the number of live neighbors is 3, the cell swithes on.
    """


    def __init__(self, cells):
        self.cells = cells


    def tick(self):
        """ This is the method that updates the game.
        """
        new_cells = set()

        for cell in self.cells:
            neighborhood = neighbors(cell)
            nln = len(self.cells.intersection(neighborhood))
            if nln in [2, 3]:
                new_cells.add(cell)
            for neighbor in neighborhood:
                if len(self.cells.intersection(neighbors(neighbor))) == 3:
                    new_cells.add(neighbor)

        self.cells = new_cells
