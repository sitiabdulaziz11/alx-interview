#!/usr/bin/python3
"""
Solving the n queens challenge
"""
import sys


def check_int(string):
    """ Check if the second argument is a valid integer """
    result = 1
    if string[0] == '0' and len(string) != 1:
        return 0
    for i in range(len(string)):
        if string[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = 0
            break
    return result


def nqueens(n):
    """ Implementation of the solution for the n queens challenge """
    all_results = []
    result = [[0] * 2 for i in range(n)]
    col = set()
    posDiag = set()
    negDiag = set()

    def backtrack(r):
        """ Recursive backtracking function """
        if r == n:
            copy_results = [row[:] for row in result]
            all_results.append(copy_results)
            return

        for c in range(n):
            if c in col or r + c in posDiag or r - c in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            result[r][0] = r
            result[r][1] = c
            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            result[r][0] = 0
            result[r][1] = 0
    backtrack(0)
    for row in all_results:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not check_int(sys.argv[1]):
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)
