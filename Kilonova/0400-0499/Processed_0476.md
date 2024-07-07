
# Task

A squirrel discovered a deposit of peanuts. The deposit has a weirder shape, as it is made of $3$ rows of rooms, each of them having $3$ rooms. The deposit has in total $9$ rooms situated on the $3 \times 3$ grid. We know the number of peanuts present in each of the $9$ rooms from the matrix.

As the squirrel doesn’t like to see too many peanuts in a room or too few peanuts in another room, it will proceed as follows: from day $1$, the squirrel will take all the rooms in which a maximal number of peanuts exists and moves exactly one peanut to every adjacent room.

The squirrel is now asking you the following question:
> "How many peanuts will there be in each room after $n$ days?"

We need to answer to $t$ such questions the squirrel will give to us.

# Input

The first line of the input contains $t$, representing the number of tests we will need to solve ($1 \leq t \leq 100$).

Each testcase will contain $4$ lines.
The first line of the test will contain $n$ ($1 \leq n \leq 10^{18}$), the number of days corresponding to each step.
The following $3$ lines of the test will contain the grid, each of the lines having $3$ columns, representing the initial values of the matrix ($10 \leq a_{ij} \leq 10^{18}$).
For tests worth $14$ points, ($1 \leq n \leq 100$, $10 \leq a_{i,j} \leq 1 \ 000$).
For tests worth $7$ more points, ($1 \leq n \leq 10^5$).
For tests worth $5$ more points, ($10 \leq a_{i,j} \leq 15$).
For tests worth $14$ more points, ($10 \leq a_{i,j} \leq 10^4$).

# Output

Each test will contain the $3 \times 3$ grid corresponding to the answer for that particular test case.

# Example
`stdin`
```
4
2
15 14 18
16 15 13
11 18 14
3
11 14 13
13 12 15
14 16 12
4
16 12 14
13 14 12
11 14 12
1
11 12 13
14 13 11
12 13 11
```

`stdout`
```
16 17 14
14 13 16
13 16 15
13 13 13
12 13 15
15 13 13
12 14 14
14 14 11
13 12 14
12 12 13
11 14 11
13 13 11
```
```
