Sant

To dig a $trench$ of length $S$, we hire a construction company that provides us with workers of various categories (a total of $C$ categories denoted $1$, $2$, $\dots$, $C$). A worker from a higher category works more and better but demands a higher salary. We want to finish the job in a single day, so we are interested in the salary and how many meters a worker from each category can dig in a day. In addition, we want to hire exactly $N$ workers (we have $N$ seats at the table!). It is also known that for each category, there is a sufficiently large number of workers, and a worker does not stop until they dig the length corresponding to their category.

## Task

Find the possibility of hiring $N$ workers from various categories who can dig exactly $S$ meters in one day and can be paid with the smallest possible amount of money.

## Input data

The first line of the input file `sant.in` will contain the natural numbers $S$, $N$, and $C$ (the length of the trench, the number of workers we want to hire, and the number of categories) separated by a space each. The next $C$ lines contain two natural numbers $L_i$ and $P_i$ $(i = 1, 2, \dots, C)$ representing the length of the trench dug and the daily payment required by a worker of category $i$.

## Output data

The first line of the output file `sant.out` will contain the minimum amount that can be paid to $N$ workers who dig exactly $S$ meters in one day, or the number $0$ if there is no solution. If there is a solution, the next line will contain a sequence of $N$ numbers sorted in ascending order, representing the categories of employed workers. If there are multiple solutions, the lexicographically smallest solution will be chosen (for those who have forgotten, an example: according to the lexicographic order, the sequence $1 1 1 2 3 3$ is smaller than the sequence $1 1 2 2 2 3$).

## Constraints

$1 \leq N \leq 100$

$1 \leq S \leq 1000$

$1 \leq C \leq 20$

$1 \leq L_i, P_i \leq 100$

## Example

`sant.in`
```
15 5 4
1 1
2 3
3 7
5 10
```

`sant.out`
```
27
1 2 2 4 4
```