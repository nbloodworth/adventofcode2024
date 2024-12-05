'''
solutions.py

File containing methods that compute solutions to the advent of code 2024 puzzles
Written in vanilla python 3.12.4

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

def RedNosedReports_part1(input):
    '''
    Count the number of safe reports:
    A report is safe if
        (1) Any two adjacent levels differ by at least 1 and at most 3 
        AND
        (2) Levels are either all increasing or all decreasing
    
    For each line (level) in the report:
    1. Test for (1)
    2. Test for (2)
    If both are true, count the report as safe
    '''

    with open(input.resolve(),"r") as f:
        reports=[l.strip("\n") for l in f.readlines()]
    
    solution=0
    for report in reports:
        test1=False
        test2=False
        report=[int(x) for x in report.split(" ")]
        report_diff=[x0-x1 for x1,x0 in zip(report,report[1:]+[0])][0:-1]
        # Test 1:
        # All values in the differential must be between 1 and 3 inclusive
        report_diff_within_bounds=len([x for x in report_diff if abs(x)>=1 and abs(x)<=3])
        if report_diff_within_bounds==len(report_diff):
            test1=True
        # Test 2:
        # All values in the differential must be negative or positive
        report_diff_negcount=len([x for x in report_diff if x<0])
        if report_diff_negcount==0 or report_diff_negcount==len(report_diff):
            test2=True
        
        if test1 and test2:
            solution+=1 

    return solution


def RedNosedReports_part2(input):
    '''
    Perform the same test as before, but add an additional test
    (the "problem dampener") if a bad report is detected.
    '''
    
    def report_tester(report):
        '''
        Encapsulate the testing algorithm here so we don't waste space retyping it.
        '''
        test1=False
        test2=False
        report_diff=[x0-x1 for x1,x0 in zip(report,report[1:]+[0])][0:-1]
        # Test 1:
        # All values in the differential must be between 1 and 3 inclusive
        report_diff_within_bounds=len([x for x in report_diff if abs(x)>=1 and abs(x)<=3])
        if report_diff_within_bounds==len(report_diff):
            test1=True
        # Test 2:
        # All values in the differential must be negative or positive
        report_diff_negcount=len([x for x in report_diff if x<0])
        if report_diff_negcount==0 or report_diff_negcount==len(report_diff):
            test2=True
        
        if test1 and test2:
            return True
        else:
            return False

    with open(input.resolve(),"r") as f:
        reports=[l.strip("\n") for l in f.readlines()]
    
    solution=0
    for report in reports:
        report=[int(x) for x in report.split(" ")]
        if report_tester(report):
            solution+=1
        else:
            # If we fail the initial test, repeat it iteratively by sequentially
            # removing a value from the report. Once the report tests "safe", it can
            # be counted as safe and added to the solution total.
            for i in range(len(report)):
                report_tmp=report[0:i]+report[i+1:]
                if report_tester(report_tmp):
                    solution+=1
                    break
    return solution