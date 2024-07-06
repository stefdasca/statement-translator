Disappointed by the lack of football in recent times, Ștefan and Georgian secretly started a business selling coffee beans, trading $K$ different types of coffee. Thus, for $N$ days, they produce coffee, and they package the beans obtained on **consecutive** days into packs that contain **all** types of coffee.

Specifically, they know for each day which types of coffee they produce that day (possibly none, in which case the business takes a break), and then they divide the days into continuous sequences such that for each type of coffee, each sequence of days contains at least one day in which that type of coffee is produced.

# Task
Before starting to package the beans, Ștefan and Georgian ask themselves two questions:

1. What is the maximum number of packs that can be formed?
2. What is the number of ways to divide the days into sequences such that the maximum number of valid packs (that contain all types of coffee) is formed?

# Input data
The first line contains an integer $P$, representing the number of the task to solve.
The second line contains an integer $T$, representing the number of scenarios for which the problem needs to be solved.
Next are the $T$ instances of the problem, each consisting of $N + 1$ lines: the first line contains two integers $N$ and $K$, representing the number of days and the number of different types of coffee, respectively; the next $N$ lines contain $K$ binary digits, the $j$-th digit on line $i$ being $0$ if on day $i$ type $j$ of coffee is not produced, or $1$ if on day $i$ type $j$ of coffee is produced.

# Output data
For each of the $T$ instances, print the answer, starting on a new line, as follows:

1. If $P = 1$, then print on a single line the maximum number of valid packs that can be formed.
2. If $P = 2$, then print on a single line the number of ways to divide the days into continuous sequences such that the maximum number of packs is formed. The answer will be printed $\\text{mod } 1\\ 000\\ 000\\ 007$.

# Constraints and clarifications
* $1 \leq P \leq 2$
* $1 \leq T \leq 3$
* $1 \leq N \leq 200\ 000$
* $1 \leq K \leq 20$
* It is guaranteed that each type of coffee appears in at least one of the $N$ days.

## Scoring
* For 6 points: $P = 1, N \leq 15$
* For another 6 points: $P = 1, N \leq 100$
* For another 9 points: $P = 1, N \leq 2\ 000$
* For another 10 points: $P = 1, N \leq 200\ 000$
* For another 10 points: $P = 2, K = 1, N \leq 200\ 000$
* For another 4 points: $P = 2, N \leq 15$
* For another 4 points: $P = 2, N \leq 20$
* For another 9 points: $P = 2, N \leq 100$
* For another 8 points: $P = 2, N \leq 700$
* For another 8 points: $P = 2, N \leq 2\ 000$
* For another 8 points: $P = 2, N \leq 10\ 000$
* For another 9 points: $P = 2, N \leq 70\ 000$
* For another 9 points: $P = 2, N \leq 200\ 000$

# Example 1

`stdin`

```
1
3
3 3
010
101
111
6 2
10
01
00
10
11
01
5 4
0100
1010
0000
1110
0001
```

`stdout`

```
2
2
1
```

# Example 2

`stdin`

```
2
3
3 3
010
101
111
6 2
10
01
00
10
11
01
5 4
0100
1010
0000
1110
0001
```

`stdout`

```
1
3
1
```

## Explanation

The types of coffee produced each day are:
* On the first day, only type $2$ of coffee is produced
* On the second day, types $1$ and $3$ of coffee are produced
* On the last day, all $3$ types of coffee are produced

The maximum number of packs is $2$, and it is uniquely obtained by grouping the days as follows: $[1, 2], [3]$.

In the second example, the maximum number of packs is $2$, being obtained in the following $3$ ways:
* $[1, 2], [3, 4, 5, 6]$
* $[1, 2, 3], [4, 5, 6]$
* $[1, 2, 3, 4], [5, 6]$

In the third example, the maximum number of packs is $1$, being obtained by grouping all the days into a single sequence: $[1, 2, 3, 4, 5]$.