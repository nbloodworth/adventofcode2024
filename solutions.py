'''
solutions.py

File containing methods that compute solutions to the advent of code 2024 puzzles

(c) Nathaniel Bloodworth 2024
'''

def HistorianHysteria_part1(input):
    '''
    Given a list with two columns, our task is to:
        1. Order both columns smallest to largest
        2. Find the difference between each ordered pair
        3. Calculate the sum of the distances
    '''
    with open(input.resolve(),"r") as f:
        lines=[l.strip("\n") for l in f.readlines()]
    
    solution=sum(
        [abs(i[1]-i[0]) for i in zip(
            sorted([int(x.split()[0]) for x in lines]),
            sorted([int(x.split()[1]) for x in lines])
            )
        ]
    )

    return solution

def HistorianHysteria_part2(input):
    '''
    How to calculate a similarity score:
        1. For each element in the left list, determine the number of times it appears on the right
        2. Multiply the element by the value in (1)
        3. Add all elements 
    '''
    with open(input.resolve(),"r") as f:
        lines=[l.strip("\n") for l in f.readlines()]
        
    solution =sum(
        [y*len(
            [x for x in [int(x.split()[0]) for x in lines] if x==y]
            ) for y in [int(x.split()[1]) for x in lines]
        ]
    )
    return solution