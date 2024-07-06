Here is the translated statement:

Alexandra, the princess of the Kingdom of Dreams, received a cake and wants to share it with her friends. Thus, she will organize a party where she will invite them. Alexandra's cake consists of $N$ pieces, and the $i$-th piece has $a_i$ cherries. Alexandra will divide the cake into several continuous subarrays of pieces, so that each piece is included in exactly one subarray, and each subarray contains at least one piece of cake. The first subarray – the one that contains the first piece – she will eat the night before the party, and the rest of the pieces she will give to her invited friends. To avoid upsetting them, Alexandra wants each subarray given to a friend to contain as many cherries as any other subarray given to a friend (but not necessarily as many cherries as the one she will eat the night before the party). Alexandra needs to invite at least one friend to the party.

# Task

Given $N$ and the array $a$, find the number of ways Alexandra could divide the cake into continuous subarrays, so that the conditions of the statement are met. Two ways of dividing the cake are considered distinct if and only if there exists a subarray in one way that does not exist in the other (if we represent a way of dividing into subarrays by the increasing sequence of starting indices for each subarray in that division, two ways of dividing are distinct if their associated index sequences are different).

Formally, given an array of numbers, the goal is to find the number of ways to divide the array into at least two subarrays, such that the sum of the elements of all subarrays are equal, the first one potentially having a different sum of elements from the others.

# Input data

The first line of the input file `tort.in` contains the number $N$. The second line contains the values $a_1, \dots , a_N$, separated by spaces.

# Output data

The only line of the output file `tort.out` will contain the required number.

# Constraints and clarifications

* $1 \leq N \leq 200 \ 000$
* $1 \leq a_1, \dots , a_N \leq 400 \ 000$
* $a_1 + \dots + a_N \leq 400 \ 000$

| # | Points | Constraints           |
| - | ------ | --------------------- |
| 1 | 12     | $1 \leq N \leq 20$    |
| 2 | 12     | $1 \leq N \leq 100, a_1 = \dots = a_n = 1$  |
| 3 | 20     | $1 \leq N \leq 100$   |
| 4 | 28     | $1 \leq N \leq 1 \ 000, a_1 + \dots + a_N \leq 2 \ 000$ |
| 5 | 28     | No additional constraints. |

# Example

`tort.in`
```
5
1 1 2 1 1
```

`tort.out`
```
6
```

## Explanation

Valid divisions are:

1. $[1], [1, 2, 1, 1]$
2. $[1, 1], [2, 1, 1]$
3. $[1, 1], [2], [1, 1]$
4. $[1, 1, 2], [1, 1]$
5. $[1, 1, 2], [1], [1]$
6. $[1, 1, 2, 1], [1]$
