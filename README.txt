Sudoku generator and solver
---------------------------

Main objective is to create an interactive sudoku game using python and create solver based on neural networks.

Next main objectives:
 
  - Create interactive game using pygame library
  - Create solver using neural networks
  
-----------------------------------------------------------
Files:

sudoku.py - contains the sudoku class object which can generate sudoku puzzle using recurrsion. 

create_puzzles.ipynb - This notebook create the train and test sudoku sets. Puzzles are randomly generated from the sudoku.py. Due to the nature of process of generating sudoku, solutions to the puzzles are ambiguous. In other words there can be more than one solution to a puzzle. 

CNN_sudoku_solver.ipynb - two different CNN models for solving sudoku are saved in this notebook. Both models, one called enhanced and the other reduced managed to solve test puzzles correctly in more then 95 % of all cases. 



