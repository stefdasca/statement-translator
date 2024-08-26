## Task

Gigel has discovered his passion for rankings. An example of a ranking is $abc$, where $a$ is in position $3$, $b$ in position $2$, and $c$ in position $1$. More generally, for a string of length $L$, the leftmost character is in position $L$ and the rightmost character is in position $1$. The distance between two rankings is defined as the sum of the absolute differences between the positions of each character in the two rankings. If a character does not appear in one of the rankings, then its position is considered to be $0$. For example, the distance between $ana$ and $danna$ is $9$ ($5$ from $d$, $1$ from the first $a$, $1$ from the first $n$, $2$ from the second $n$, and $0$ from the second $a$). Gigel has several sets of rankings. For each set of rankings, he found a ranking $X$ that has the minimum sum of distances from $X$ to each ranking in the set. He is curious if you can also find out what the value of this sum is.

## Input data

The input file `clasamente.in` contains on the first line $T$, the number of tests. Each test is as follows: the first line contains $N$, the number of rankings. On the next $N$ lines, each line contains a ranking given as a character string.

## Output data

The output file `clasamente.out` contains $T$ lines, each line containing the minimum distance for the rankings found by Gigel.

## Constraints

$T = 10$

$1 \leq N \leq 100$

$1 \leq \text{number of distinct characters in a test} \leq 60$, where the ranking $aa$ contains $2$ distinct characters encoded as $a1$ and $a2$ (see example)

## Example

`clasamente.in`

```
2
3
abc
cd
acbd
2
ana
danna
```

`clasamente.out`
```
11
9
```

## Explanation

For the first example, a possible ranking found by Gigel is $acd$. It has a distance of $4$ ($0$ for $a$ + $2$ for $b$ + $1$ for $c$ + $1$ for $d$) from the first ranking, a distance of $3$ ($3$ for $a$ + $0$ for $c$ + $0$ for $d$) from the second ranking, and a distance of $4$ ($1$ for $a$ + $2$ for $b$ + $1$ for $c$ + $0$ for $d$) from the third ranking. The sum of distances is $11$. If the ranking found by Gigel were $abc$, then the sum of the distances would also be $11$. The second example is described in the statement.