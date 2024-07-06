The children from the school in the city receive gifts before the holiday. There is a very large box containing $N$ candies that can be distributed to all the children present at the festival that was organized, such that, always, everyone receives the same number of candies, $B$.

# Task

1. Determine the maximum value of $B$, knowing that there are exactly $X$ children present at the festival, and after distribution, some candies may be left in the box.
2. Determine the maximum number of children that can be present at the festival, so that all the candies in the box are distributed, and the value of $B$ is at least $2$.
3. Determine the minimum number of candies that can be left in the box, after distribution, such that at least $X$ children are present at the festival and the value of $B$ is at least $Y$. Corresponding to the obtained number of candies left and the specified conditions, also determine the number of children present as well as the value of $B$. In case there are multiple options that meet these conditions, choose the one for which the number of children present is the maximum possible.

# Input data

The input file `bomboane.in` contains on the first line $4$ natural numbers $C \\ N \\ X \\ Y$ , in this order, separated by a space. The value $C$ represents the task to be solved, and the others have the significance given in the statement. Note that for some tasks not all $4$ values are necessary, but they will be present in the input file.

# Output data

The output file `bomboane.out` will contain the results on a single line, as follows: for the first two tasks, a natural number representing the requested value will be printed; for the third task, $3$ numbers separated by a space will be printed, in this order: the minimum requested number of candies that can be left in the box, the number of children present and the value of $B$, under the specified conditions in the task.

# Constraints and clarifications
* $1 \le C \le 3$
* $1 \le N, X, Y \le 2\ 000\ 000\ 000$
* It is guaranteed that there is a solution for all input data.
* It is guaranteed that for all input data corresponding to task $3$, the solution obtains by leaving at most $100$ candies in the box.

| # | Score | Constraints |
| - | - | ------------|
|1|19|$C = 1$|
|2|28|$C = 2$|
|3|53|$C = 3$|

# Example 1

`bomboane.in`
```
1 51 5 8
```

`bomboane.out`
```
10
```

## Explanation

We solve task $C = 1$, for $N = 51$ and $X = 5$ (the value $Y = 8$ is not necessary for this task). $B = 10$ candies can be distributed to each of the $X = 5$ children. One candy is left in the box.

# Example 2

`bomboane.in`
```
2 51 5 8
```

`bomboane.out`
```
17
```

## Explanation

We solve task $C = 2$, for $N = 51$ (the values $X = 5$ and $Y = 8$ are not necessary for this task). Maximum $17$ children can be present and each receives $B = 3$ candies.

# Example 3

`bomboane.in`
```
3 51 5 8
```

`bomboane.out`
```
1 5 10
```

## Explanation

We solve task $C = 3$, for $N = 51$, $X = 5$ and $Y = 8$. The minimum number of candies left in the box to satisfy the task is $1$. Under these conditions, the maximum number of children receiving candies is $5$ and each gets $B = 10$ candies.