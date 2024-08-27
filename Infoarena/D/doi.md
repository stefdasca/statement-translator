# Doi

Afrodisia is playing together with Ambrozia and Anisia and they have discovered a new game called Doi. Given a natural number $N$, they need to reach the number 0 (zero) by performing as few operations as possible. There are three allowed operations. The current number can be incremented or decremented (by a single unit). Additionally, if the current number is even, it is also possible to divide it by two. The girls quickly got bored with the game and need your help.

## Input data

The input file `doi.in` contains on the first line a natural number $T$, representing the number of tests in the file. On each of the next $T$ lines, there is a natural number for which the answer to the game proposed by the girls needs to be determined.

## Output data

The output file `doi.out` will contain $T$ lines, with the answer for the $i$-th number from the input file on the $i$-th line.

## Constraints

$N$ will have at most 500 digits

$1 \leq T \leq 50$

In 40% of the tests, all numbers will have at most 15 digits

## Example

`doi.in`
```
2
4
3
```

`doi.out`
```
3
3
```

## Explanation

For the first test, a possible solution is $4 \div 2 = 2$, $2 \div 2 = 1$, $1-1 = 0$.

For the second test, a possible solution is $3-1 = 2$, $2-1 = 1$, $1-1 = 0$.