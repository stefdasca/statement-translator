CDM is a very diligent boy and this year he managed to achieve good enough grades to receive a merit scholarship. With this scholarship, he wants to buy the Teeks code, a very useful tool. In his attempt to purchase this code, he has to get past the administrator Esoterik. Esoterik tells CDM that to invite him to the group for purchasing the Teeks code, he needs to solve the following problem:

Given $n$ and $n$ non-zero natural numbers.

# Task

1. Determine the maximum digit that appears in at least one of the $n$ numbers and the number of its occurrences.
2. Concatenate all these numbers, and sort the digits of the resulting number in ascending order. Display the $k$-th digit from the sequence obtained after sorting.

# Input data

The first line of the input file `sensegame.in` contains $C$ representing the number of the task that needs to be solved.

The second line of the input file contains $n$, and in the case of task $2$, the number $k$ with its significance as described in the statement.

The third line of the input file contains the $n$ non-zero natural numbers.

# Output data

The first line of the output file `sensegame.out` contains the answer corresponding to task $C$.

# Constraints and clarifications

* $1 \le n \le 10^6$;
* The total number of digits of all numbers $\le 10^7$;
* $1 \le a_i \le 10^{14}$;
* $1 \le k \le 10^7$.

| # | Score | Constraints                                                      |
|---|-------|-----------------------------------------------------------------|
| 1 | 20    | $C = 1$                                                         |
| 2 | 20    | $C = 2$ and $1 \le$ total number of digits of all numbers $\le 10^3$ |
| 3 | 20    | $C = 2$ and $1 \le$ total number of digits of all numbers $\le 10^5$ |
| 4 | 40    | No additional constraints                                       |

# Example 1

`sensegame.in`

```
1
7
358 73 789 241 100 357 266
```

`sensegame.out`

```
9 1
```

## Explanation

The largest digit is $9$ and it appears once.

# Example 2

`sensegame.in`

```
2
7 9
358 73 789 241 100 357 266
```

`sensegame.out`

```
3
```

## Explanation

If we concatenate the numbers and then sort the digits, we obtain the sequence: $00112233345566777889$. From this sequence, the $9$-th digit is $3$.