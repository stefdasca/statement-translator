# „Dormeau adânc sicriele de plumb,
> Și flori de plumb și funerar veșmânt –�

Computer science awakens the spirit of a poet in every programmer. The mischievous Andi learned in the Romanian class about the poem „Plumb�, written by George Bacovia. The young computer scientist noticed that the term `plumb` (lead) is enclosed, meaning the vowel `u` is surrounded by the consonants `l` and `m`. Since then, whenever the boy sees a number, he only thinks about the poor enclosed digits.

In a number $X$, a digit is called enclosed if it has digits of different parity on both its left and right sides. For example, each of the numbers $456$, $878$, and $5321$ contains one enclosed digit, namely: $5$, $7$, and $2$, respectively. On the other hand, the numbers $12$, $334$, and $1024$ contain no such digits. Additionally, a sequence of at least two consecutive digits is called an enclosed group if they have the same parity and are flanked on both the left and right sides by a digit of different parity.

# Task

Given $C$, the task you must answer, and $N$ natural numbers, Andi asks you to answer one of the following two questions:

1. How many enclosed digits does each number have?
2. How many enclosed groups does each number have?

# Input data

- The first line will contain the number $C$ of the task.
- The second line will contain $N$, the number of numbers.
- The third line will contain the $N$ natural numbers, separated by a space.

# Output data

- $N$ numbers will be printed, separated by a space, such that the $i$-th response corresponds to the number in position $i$.

# Constraints and clarifications

- $1 \leq C \leq 2$;
- $1 \leq N \leq 100\ 000$;
- $1 \leq X \leq 10^{18}$;
- An enclosed group consists of at least 2 consecutive digits.
- For fast input and output, it is recommended to use these lines of code at the beginning of the `main` function:

```cpp
ios::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
```

| # | Score | Constraints |
|:---:|:----:|:----:|
| 1 | 5 | $C = 1, X < 1\ 000$ |
| 2 | 5 | $C = 1, X < 10\ 000$ |
| 3 | 5 | $C = 1, X < 100\ 000$ |
| 4 | 25 | $C = 1$ |
| 5 | 5 | $C = 2, X < 1\ 000$ |
| 6 | 5 | $C = 2, X < 10\ 000$ |
| 7 | 5 | $C = 2, X < 100\ 000$ |
| 8 | 45 | $C = 2$ |

# Example 1

`stdin`
```
1
5
1010 55679 1234 3 27
```

`stdout`
```
2 1 2 0 0
```

## Explanation

Below, we have highlighted the enclosed digits, marked between `|`:
`1|0|1|0`, `55|6|79`, `1|2|3|4`, `3`, `27`

# Example 2

`stdin`
```
2
6
257546 833425 123456 22 49768332 27
```

`stdout`
```
1 2 0 0 3 0
```

## Explanation

Below, we have highlighted the enclosed groups, marked between `|`:
`2|575|46`, `8|33|42|5`, `123456`, `22`, `4|97|68|33|2`, `27