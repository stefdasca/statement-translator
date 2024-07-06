We have at our disposal $n$ metallic bars of the same thickness but different lengths. We can pick any bar and cut it, obtaining two smaller bars. We want to know if, using only this operation (without welding them back), we can obtain a number of bars of given lengths. Specifically, given a set of four numbers $a$, $b$, $c$, $d$, we need to decide if we can obtain $a$ bars of length $1$, $b$ bars of length $2$, $c$ bars of length $4$, and $d$ bars of length $8$. Once a cut of length $L$ is made on a bar, the remainder can still be used to cut other bars of any desired lengths.

# Task

Knowing $n$ – the number of metallic bars and the lengths of the $n$ metallic bars available, for each of the sets of four numbers $a \\ b \\ c \\ d$ given, determine if, starting from the given $n$ lengths, we can obtain bars of the desired lengths.

# Input data

The input file `taieri.in` contains on the first line the natural number $n$. The second line contains the $n$ natural numbers representing the initial lengths of the bars. The third line contains a natural number $m$ which represents the number of sets of four numbers. On each of the following $m$ lines, there are four natural numbers $a \\ b \\ c \\ d$ with the meanings mentioned above. The numbers on the same line are separated by a space.

# Output data

The output file `taieri.out` will contain $m$ values $0$ and $1$, separated by a space. For each set of four numbers, in the order of their appearance in the input file, print the value $1$ if the desired number of bars for all four lengths from the corresponding set can be obtained, otherwise $0$.

# Constraints and clarifications

* The lengths of the bars are non-zero natural numbers at most equal to $10 \ 000 \ 000$.
* $0 \leq a, b, c, d \leq 10 \ 000 \ 000$;

|#|Points|Constraints|
|-|-|--------|
|1|16|$n, m \leq 1 \ 000$ and $b = c = d = 0$|
|2|28|$n, m \leq 1 \ 000$|
|3|56|$n, m \leq 100 \ 000$|

# Example

`taieri.in`
```
5
10 12 8 3 1
3
2 3 2 2
31 0 0 0
1 13 0 1
```

`taieri.out`
```
1 1 0 
```

## Explanation

In the first set – $2 \\ 3 \\ 2 \\ 2$, we need to obtain two bars of length $1$, three bars of length $2$, two bars of length $4$, and two bars of length $8$. We can cut the bar of length $10$ into one of $8$ and one of $2$. We already have the second bar of length $8$. We are left with bars of lengths: $2$, $12$, $3$, and $1$. The two bars of length $4$ can be cut from the bar of length $12$, leaving us with bars of lengths $2$, $4$, $3$, and $1$. For the three bars of length $2$, we can use the first bar, and the second one is cut into two pieces, and the four bars of length $1$ can be obtained by using the remaining bars of lengths $3$ and $1$.

In the second set – $31 \\ 0 \\ 0 \\ 0$, we can obtain from the first given bar $10$ bars of length $1$, from the second bar $12$ bars of length $1$, from the third bar another $8$ bars of length $1$, and the last bar is already of length $1$, so we can get the needed $31$ bars. Notice that it was not necessary to use the bar of length $3$. It is also noted that it is not necessary to obtain bars of lengths $2$, $4$, or $8$.

In the third set – $1 \\ 13 \\ 0 \\ 1$, no matter how we cut the bars available, we cannot obtain the entire set consisting of: one bar of length $1$, $13$ bars of length $2$, and one bar of length $8$.