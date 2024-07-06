Ionel's grandfather is a beekeeper, so Ionel wanted to combine his passion for numbers with his grandfather's profession. He arranged $n$ numbers in the shape of a series of $nr$ honeycombs, numbered from $1$ to $nr$. Within a honeycomb, the numbers were arranged in the direction of the clock's hands. On the common side of two honeycombs, he only placed two numbers. Mihuț, Ionel's brother, as a joke, mixed the numbers within the honeycombs as follows: he took the largest prime number from the second honeycomb and swapped it with the largest prime number from the penultimate honeycomb (with the ordinal number $nr-1$), then he took the largest prime number from the third honeycomb and swapped it with the largest prime number from the antepenultimate honeycomb (with the ordinal number $nr-2$). He continued this process up to the middle of the series of honeycombs. Mihuț did not touch the numbers that were part of the common side of two adjacent honeycombs. If within a honeycomb Mihuț did not find a prime number that could be moved, then he did not make the swap within the corresponding pair of honeycombs.

Example:
Ionel started with $18$ numbers: $2, \ 11, \ 37, \ 14, \ 5, \ 12, \ 17, \ 101, \ 97, \ 26, \ 3, \ 19, \ 13, \ 5, \ 130, \ 7, \ 213, \ 907$ and arranged them according to the model in figure $1$. The model in figure $2$ resulted after Mihuț mixed the numbers. Mihuț is not allowed to mix the numbers: $11, \ 37, \ 101, \ 97, \ 19, \ 13$.
~[fagure.png|align=center]

# Task

Write a program that reads the information from the input file `fagure.in` and determines:

1. the number of honeycombs Ionel managed to construct;
2. the smallest ordinal number of the honeycomb on which Ionel placed the value $x$, before the mixing performed by Mihuț;
3. for a natural number $k$, read from the file, what is the new number placed by Mihuț on the honeycomb with the ordinal number $k$. If Mihuț did not touch the numbers on honeycomb $k$, the value $0$ will be written.

# Input data

The input file `fagure.in` contains three lines:

* the first line contains the pair of natural numbers $n$ and $k$ separated by a space with the meanings from the statement;
* the second line contains the $n$ nonzero natural numbers smaller than $32 \ 000$, separated by a space, with which Ionel constructed the honeycombs;
* the last line in the file contains the natural number $x$ with the meaning from the statement. The value $x$ can be found in the file and on the second line.

# Output data

The output file `fagure.out` will contain three lines:

1. the first line will contain the natural number $nr$ which represents the number of honeycombs constructed by Ionel;
2. the second line will contain the smallest ordinal number of the honeycomb on which the value $x$ was placed. If the value $x$ is found on the common side of two adjacent honeycombs, the ordinal numbers of the two honeycombs will be displayed in ascending order, separated by a space;
3. the third line will contain the number placed by Mihuț on honeycomb $k$ after mixing the numbers, or the value $0$ if he did not touch honeycomb $k$.

# Constraints and clarifications

* For all tests, the last honeycomb constructed by Ionel is formed of $6$ numbers.
* $10 \leq n \lt 10 \ 000$
* $2 \leq k \leq \text{middle honeycomb's ordinal number}$
* $1 \leq x \lt 30 \ 000$
* For solving task $1$ there is $30\%$ of the score, for solving task $2$, $40\%$ of the score, and for solving task $3$, $30\%$ of the score.

# Example

`fagure.in`
```
18 2
2 11 37 14 5 12 17 101 97 26 3 19 13 5 130 7 213 907
101
```

`fagure.out`
```
4
2 3
5
```

## Explanation

$4$ represents the number of honeycombs constructed by Ionel.
$101$ belongs to honeycombs $2$ and $3$.
$5$ represents the value placed by Mihuț on honeycomb $2$.