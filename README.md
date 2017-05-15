# game_of_life

This is a follow-up to a code retreat that I participated in at work.
It is a working simulation of Conway's game of life.

The description of the game from Wikipedia (sourced on 2017-05-14):¬
> The Game of Life, also known simply as Life, is a cellular automaton devised by t
he British mathematician John Horton Conway in 1970.¬
> The "game" is a zero-player game, meaning that its evolution is determined by its
 initial state, requiring no further input.¬

---

## Rules and Assumptions

This implementation will be two-dimensional (unbounded).

The rules:

    1. A cell with fewer than two live neighbors will be set to off.
    2. A cell with two live neighbors will retain its state.
    3. A cell with three live neighbors will be set to on.
    4. A cell with more than three live neighbors will be set to off.

## Code

The code is organized into one file, with one class.
All tests are written within one file in the test directory.
