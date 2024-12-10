
At a Formula 1 race, each participating team builds its own car to compete. The numbering of the cars in the race is done by the organizers using square flags that alternately contain, in each row (both horizontally and vertically), identical-sized white and black squares. In the following figure, the flags of the first 4 cars in the race are presented in order. We observe that each flag has two more rows (both horizontally and vertically) than the previous flag, and in all four corners of any flag there is a black square.

~[formula1.jpg]

# Task

Write a program that reads two natural numbers $K$ and $N$ and determines:

1. How many white and black squares are there in total on the flag of the car with number $K$;
2. Denoting by $A$ the total number of white squares on the flags of the first $N$ cars in the race, how many white and black squares are there in total on the largest flag that contains at most $A$ white squares.

# Input data

The input file `formula1.in` contains on the first line a natural number $C$. For all input tests, the number $C$ can only have the value $1$ or the value $2$ and represents the number of the task that needs to be solved. The second line of the file `formula1.in` contains, in order, the natural numbers $K$ and $N$.

# Output data

If $C = 1$, the first task will be solved. In this case, the output file `formula1.out` will contain on the first line a natural number representing the total number of squares on the flag of the car with number $K$.
If $C = 2$, the second task will be solved. In this case, the output file `formula1.out` will contain on the first line a natural number representing the total number of squares on the largest flag that contains at most $A$ white squares.

# Constraints and clarifications

* $1 \leq K \leq 100\ 000$;
* $1 \leq N \leq 500\ 000$;
* For the correct solution of the first task, you get 20 points, and for the correct solution of the second task, you get 80 points.

# Example 1

`formula1.in`
```
1
3 4
```

`formula1.out`
```
25
```

## Explanation

The first task is solved, and only the value $K$ is used. The flag of the third car has a total of $25$ white and black squares.

# Example 2

`formula1.in`
```
2
3 4
```

`formula1.out`
```
81
```

## Explanation

The second task is solved, and only the value $N$ is used. On the flags of the first $4$ cars, there are a total of $0 + 4 + 12 + 24 = 40$ white squares. The largest flag that contains at most $40$ white squares belongs to the car with number $5$ which has a total of $81$ squares.
