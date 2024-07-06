During the summer vacation, after getting bored of the beach and water, Ionica spends most of his time in the Amusement Park. Among all the places for amusement, he chooses the shooting range. Thus, one evening Ionica scores $S$ points, after a certain number of shots (at least two shots).

Knowing that in all the shots he scored points and that after each shot he makes constant progress, meaning he scores one point more than in the previous shot, you are required to determine all the ways of obtaining the scores (with their sum equal to $S$).

# Input data

The input file `tir.in` contains a single integer $S$.

# Output data

The output file `tir.out` will contain a single integer $x$, the number of solutions to the problem.

On the next $x$ lines, the solutions of the problem will be found, in increasing order of the initial score, with each line displaying the initial score $p$ and the number of shots.

# Constraints and clarifications

* $1 \leq S \leq 10^{12}$;
* The tests and constraints have been redone, and the output format has also been modified from the original statement.
* All obtained scores are positive.

# Example 1

`tir.in`
```
15
```

`tir.out`
```
3
1 5
4 3
7 2
```

## Explanation

The solution $1 \\ 5$ corresponds to the scores $1 \\ 2 \\ 3 \\ 4 \\ 5$; the solution $7 \\ 2$ corresponds to the scores $7 \\ 8$; the solution $4 \\ 3$ corresponds to the scores $4 \\ 5 \\ 6$.