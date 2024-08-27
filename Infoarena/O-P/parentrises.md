## Task

We define a string as a sequence of characters $($ and $)$. We define a well-parenthesized string as a string that can be transformed into a correct arithmetic expression by inserting the characters 1 and among the characters of the string. For example, the strings $()()$ and $((()))$ are well-parenthesized, as they can be transformed into $(1+1)$ and $((1+1)+1)$ respectively. On the other hand, $)($ and $(($ are not well-parenthesized. We agree that the empty string is well-parenthesized. Bogdan Păcuraru and Costel Rostogolitul work at $B.P.A.N.$ (Bureau of Unnecessary Algorithmic Problems), useless parenthesis division. They receive two types of tasks: Teo al Focului and Radu Muntele (their clients), both colorblind, have a string $S$. Teo can see only red and green, while Radu can see only blue and green. They want to color $S$ using the colors red, green, and blue such that both will see a well-parenthesized string if they ignore the parentheses in colors they cannot see. If such a coloring exists, we say that $S$ is $RGB$-readable. Find a coloring, or indicate that it does not exist. Mihai Precumlancea and Andrei Preotul (other clients) want to know how many $RGB$-readable strings of length $N$ exist, for a given $N$. They want the answer modulo $1.000.000.007$. Bogdan and Costel usually solve these tasks using $C$ / $C++$, but Bunelul cel Rău hacked their computers and they can only use $Rust$. Unfortunately, they know nothing about $Rust$; can you help them?

## Input data

The first line of the input file `parentrises.in` will contain a number $P$, denoting the type of task you will solve:

If $P = 1$, you will solve the task given by Teo and Radu.

If $P = 2$, you will solve the task given by Mihai and Andrei.

The second line will contain a number $T$, representing the number of tests in the file. The $T$ tests will follow, one per line:

If $P = 1$, a test will contain the string $S$.

If $P = 2$, a test will contain the number $N$.

## Output data

The output file `parentrises.out` will contain the answers for the $T$ tests, one per line. If $P = 1$ and no solution exists, print `impossible`. If $P = 1$ and a solution exists, print a possible coloring. The $i$-th character on the line will represent the color of the $i$-th character in $S$: $R$ represents red, $B$ represents blue, and $G$ represents green. 

If $P = 2$, print how many $RGB$-readable strings of length $N$ exist, modulo $1.000.000.007$.

## Constraints and clarifications

For 5 points,

$P = 1$, 

$1 \leq T \leq 5$,

$1 \leq$ length of $S \leq 13$

If $L$ is the sum of the lengths of the strings in the input, then for 11 more points,

$P = 1$, 

$1 \leq L \leq 100$

For 6 more points,

$P = 1$, 

$1 \leq L \leq 1.000$

For 28 more points,

$P = 1$, 

$1 \leq L \leq 1.000.000$

For 6 more points,

$P = 2$, 

$1 \leq N, T \leq 15$

For 16 more points,

$P = 2$, 

$1 \leq N, T \leq 30$

For 28 more points,

$P = 2$, 

$1 \leq N, T \leq 300$

## Examples

`parentrises.in` 

```
1
3
())(()
()((()
(()))
```

`parentrises.out` 

```
GRBRBG
BBRBG
impossible
```

`parentrises.in` 

```
2
2
6
100
```

`parentrises.out` 

```
12
959772055
```

In the first test of the first file, both Teo and Radu will see the string $()()$. In the second test of the first file, Teo will see the string $()$, and Radu will see the string $()()$. In the third test of the first file, there is no valid coloring.