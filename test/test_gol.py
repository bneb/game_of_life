""" Test Conway's Game of Life Simulation

This file contains tests for functions and their edge-cases
in an implementation of the game of life.

This is meant to be tested with PyTest.

The test strategy is outside-in TDD.
"""

from game_of_life.classes import Game
from random import randint


def test_empty_game_init():
    """ Test the initialization of a game.
    """

    game = Game()
    assert not game.cells


def test_random_game_init():
    """ Test initialization with a random number of cells.
    """

    num = randint(0, 10)
    game = Game(set([(randint(-40, 40), randint(-40, 40)) for _ in range(num)]))
    assert len(game.cells) == num


def test_empty_game_update():
    """ Test update of empty game.
    """

    game = Game()
    game.tick()
    assert not game.cells


def test_loner_game_update():
    """ Test update of a game initialized with one live cell.
    """

    game = Game({(1, 2)})
    game.tick()
    assert not game.cells


def test_blinker_game_update():
    """ Test a random number of updates to a blinker game.
    """

    odd_cells = {(1, 2), (1, 3), (1, 4)}
    even_cells = {(0, 3), (1, 3), (2, 3)}
    game = Game(odd_cells)
    num = randint(1, 50)
    for _ in range(num):
        game.tick()
        assert game.cells == even_cells
        game.tick()
        assert game.cells == odd_cells


def test_scripted_update():
    """ This test should test all of the four rules governing the automata.
        The game will be initialized as follows:
            0 1 0 0
            0 1 1 0
            0 0 0 1
        The first update will produce:
            0 1 1 0
            0 1 1 0
            0 0 1 0
        The second update will produce:
            0 1 1 0
            0 0 0 1
            0 1 1 0
        The third update will produce:
            0 0 1 0
            0 0 0 1
            0 0 1 0
        The fourth update will produce:
            0 0 0 0
            0 0 1 1
            0 0 0 0
        The fifth update will produce:
            0 0 0 0
            0 0 0 0
            0 0 0 0
    """
    start = {(1, 0), (1, 1), (2, 1), (3, 2)}
    first_update = {(1, 0), (2, 0), (1, 1), (2, 1), (2, 2)}
    second_update = {(1, 0), (2, 0), (3, 1), (1, 2), (2, 2)}
    third_update = {(2, 0), (3, 1), (2, 2)}
    fourth_update = {(2, 1), (3, 1)}
    fifth_update = set()
    game = Game(start)
    game.tick() # first update
    assert game.cells == first_update
    game.tick() # second update
    assert game.cells == second_update
    game.tick() # third update
    assert game.cells == third_update
    game.tick() # fourth update
    assert game.cells == fourth_update
    game.tick() # fifth update
    assert game.cells == fifth_update
