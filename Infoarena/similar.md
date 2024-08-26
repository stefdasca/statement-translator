# Similar

As you know, Gigel likes to play with strings made up of $0$ and $1$ (zero and one). In this problem, Gigel also likes the characters $*$ and $?$. Gigel has a string $T$ composed of $0$ and $1$ and a string $P$ composed of $0$, $1$, $*$, and $?$. Gigel wants to check how similar $P$ and $T$ are. He checks the similarity by transforming the string $P$ into the string $T$ using the following operations:
- Transform the character $?$ into $0$ or $1$, paying $0$ RON in similarity costs.
- Transform the character $*$ into a string of $0$ and $1$, paying $0$ RON in similarity costs.
- Transform the character $0$ into $1$, paying $1$ RON in similarity costs.
- Transform the character $1$ into $0$, paying $1$ RON in similarity costs.

The degree of similarity between $P$ and $T$ is given by the lowest cost with which $P$ can be transformed into $T$. Gigel asks you to help him find the degree of similarity.

## Input data

The first line of the input file `similar.in` contains the number $Z$ of tests. The following $Z \cdot 2$ lines contain the tests, each test on two lines. The first line in a test contains the string $T$ and the second line contains the string $P$.

## Output data

For each test, print a line in the output file `similar.out` with a number representing the minimum similarity cost paid by Gigel. If the transformation cannot be done, print $-1$.

## Constraints and clarifications

- For each test, $P$ and $T$ have at least $1$ character and at most $1\ 000$ characters.
- $1 \leq Z \leq 512$

## Example

`similar.in`
```
3
0101
0*1
1111
??00
01
1
```

`similar.out`
```
2
1
-1
```

## Explanation

In the first test, $*$ is transformed into the string $01$ (cost $0$).

In the second test, each $?$ is transformed into $1$ (cost $0$) and the two $0$s are transformed into $1$ (cost $2$).

For the last test, $0$ cannot be transformed into $01$.