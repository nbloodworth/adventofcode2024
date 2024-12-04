'''
Command-line interface for running python-based solutions to 2024 advent of code puzzles.

(c) Nathaniel Bloodworth 2024
'''

# Python library imports
import argparse
from pathlib import Path
import inspect

# Import solutions:
import solutions

def solve_puzzle(
        input,
        puzzle
    ):
    '''
    Method for calling puzzle solutions on provided inputs.
    Given puzzle solutions are single numbers, prints solution to screen.

    Inputs:
    input [Path]:   Path object for input file
    puzzle [str]:   Method name from solutions.py

    Outputs:
    None 
    '''
    if not input.is_file():
        print(f"Input file {input.name} not found!")
        return
    # try:
    puzzle_solver=getattr(solutions,puzzle)
    print(puzzle_solver(input))
    # except AttributeError as e:
    #     print(f"Puzzle name {puzzle} not found!\nPuzzle names include: {", ".join(
    #         [x for x in dir(solutions) if inspect.isfunction(getattr(solutions,x))]
    #         )}")
    # except:
    #     print("Puzzle solver failed! Not sure why :(")

    return
    
parser=argparse.ArgumentParser(
    prog="Advent of Code 2024 Solutions",
    description="Test solutions to the Advent of Code 2024 in python"
)
parser.add_argument("-i","--input",
                    required=True,
                    type=Path,
                    help="File path for the puzzle input"
                )
parser.add_argument("-p","--puzzle",
                    required=True,
                    type=str,
                    help="Name of the puzzle to solve (method name in solutions.py)"
                )

args=parser.parse_args()

if __name__=="__main__":
    solve_puzzle(
        args.input,
        args.puzzle
    )