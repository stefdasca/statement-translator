## Task

Answer $T$ questions of the form: How many non-periodic strings of length $N$ with characters from $a$ to $z$ exist?

## Input data

The input file `cntper.in` will contain on the first line a natural number $T$. On the following $T$ lines, each line will contain a natural number $N$.

## Output data

The output file `cntper.out` will contain $T$ lines, each line containing the answer for the $i$-th test, modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq T \leq 200\ 000$

A string $S$ is considered periodic if there exists another string $P$ such that $S$ is obtained by concatenating the string $P$ multiple times. For example, the string `abcabc` is periodic because it can be obtained from the string `abc` with period $2`, while the string `abcabd` is not periodic. A string of length $1$ is not considered periodic.

## Example

`cntper.in`
```
1
2
```
`cntper.out`
```
650
```