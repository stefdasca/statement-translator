A child wants to paint Easter eggs, having at their disposal paints of red, yellow, green, and blue colors. Each color will be represented by a single character as follows: `r` for red, `g` for yellow, `v` for green, and `a` for blue. To paint the eggs, they are placed in a row, one after another. Thus, a painting will be a sequence of $N$ characters from the set {'r', 'g', 'v', 'a'}, representing the colors of the $N$ eggs in the order they are placed. 

We call a sequence of $R$ characters a "dew" if exactly $R-1$ of those characters represent the color red, and one character represents one of the other 3 colors. For example, the dew sequences of length $3$ are `grr`, `rgr`, `rrg`, `vrr`, `rvr`, `rrv`, `arr`, `rar`, `rra`. The child considers a painting to be $R$-beautiful if any $R$ consecutive characters in the painting form a dew sequence. For example, for $N = 11$ eggs, the string `arrrvrrrarr` represents a $4$-beautiful painting.

# Task

Given $N$, the number of painted eggs, and the natural number $R$, write a program that determines and displays:

1. the number of dew sequences of length $R$ existing in the painting of the $N$ eggs;
2. the total number of $R$-beautiful paintings for the $N$ eggs.

# Input data

The input file `roua.in` contains on the first line a natural number $C$ representing the task from the problem that needs to be solved ($1$ or $2$). The second line of the file contains the natural numbers $N$ and $R$, separated by space, representing the number of eggs and the length of a dew sequence. If $C = 1$, the file will also contain a third line on which the painting of the $N$ eggs is given.

# Output data

The output file `roua.out` will contain a single line where a natural number will be printed, representing the answer to the task specified in the input file.

# Constraints and clarifications

* $3 \leq N \leq 10\ 000$
* $2 \leq R < N$
* For the correct solving of task $1$, $40$ points are awarded 
* For the correct solving of task $2$, $60$ points are awarded 
* For $60\%$ of the tests for task $2$, $3 \leq N \leq 70$
* For $40\%$ of the tests for task $2$, $N > 70$
* The result for task $2$ can have at most $2\ 400$ digits.

# Example 1

`roua.in`
```
1
7 3
vrrrgrr
```

`roua.out`
```
4
```

## Explanation

The task is $1$. There are $N = 7$ eggs. The dew sequences of length $3$ existing in the painting are `vrr`, `rrg`, `rgr`, `grr`.

# Example 2

`roua.in`
```
2
4 3
```

`roua.out`
```
4
15
```

## Explanation

The task is $2$. There are $4$ eggs.
The $3$-beautiful paintings of the $4$ eggs are `grrg`, `grrv`, `grra`, `vrrg`, `vrrv`, `vrra`, `arrg`, `arrv`, `arra`, `rgrr`, `rvrr`, `rarr`, `rrgr`, `rrvr`, `rrar`.