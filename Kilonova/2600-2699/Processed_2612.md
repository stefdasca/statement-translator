Just a few minutes are left until the billionaire returns from his weekly golf game, and Gigi and Gina (a sort of Bonnie and Clyde duo from Romania) have discovered his safe. Luckily, the maid has given them 3 possible codes. As the billionaire is very cautious and doesn't want anyone to find out his cipher, he might have added a random digit to each discovered code.

However, Gigi and Gina have another valuable piece of information that will help them eliminate some of the possible codes received from the maid: the cipher is a number divisible by $3$.

To save time, they want to try only those codes that could be correct (since the cipher might be long, typing each code takes time).

# Task

A natural number $N$ is read, representing the number of digits in each of the following 3 codes. For each of these, $N$ digits (0-9) are read. Write a program that decides for a set of 3 codes:
1. which ones could be correct without eliminating a digit (they correspond to a number divisible by $3$)
2. which ones could be correct after eliminating a digit (they correspond after processing to a **NON-ZERO** number divisible by $3$)

# Input data

The input file `jaf.in` contains:
* On the first line, a natural number $C$, representing the task to be solved.
* On the next line, a natural number $N` and then on the following 3 lines, digits (0-9), separated by a space.

# Output data

In the output file `jaf.out`, on line $i$, print the message `DA` if the $i$-th received cipher could be correct (either before or after eliminating a digit, according to the task) or `NU` if it is incorrect.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq C \leq 2$
* The sequence of digits may start with digits of $0$.

| # | Score | Constraints |
|---|-------|-------------|
| 1 | 25    | $C = 1$ and $N < 10$ |
| 2 | 25    | $C = 1$ and $N < 100$ |
| 3 | 50    | $C = 2$ and $N < 10$ |

# Example 1

`jaf.in`
```
1
3
0 3 6
1 6 3
0 1 0
```

`jaf.out`
```
DA
NU
NU
```

## Explanation

$36$ is a multiple of $3$  
$163$ is not a multiple of $3$  
$10$ is not a multiple of $3$  

# Example 2

`jaf.in`
```
2
3
0 3 6
1 6 3
0 1 0
```

`jaf.out`
```
DA
DA
NU
```

## Explanation

For the first number, we can eliminate one digit and get $3$ or $6$, which are multiples of $3$.  
For the second number, we can eliminate the digit $1$ and get $63$, which is a multiple of $3$.  
For the last number, after eliminating one digit, $1$ and $10$ are not multiples of $3$.