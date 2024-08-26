## Task

You are given $N$ dominoes. Determine a way to construct a sequence that contains all the dominoes, following the rule of the domino game. This rule means that the numbers on the corresponding faces of two consecutive dominoes must be equal. The dominoes can be chosen in any order and rotated.

## Input data

The first line of the input file `domino.in` will contain the number $N$ of dominoes. The next $N$ lines will contain two numbers separated by a single space, representing the two numbers written on the corresponding domino.

## Output data

The first line of the file `domino.out` has to contain $1$, if there is a solution, and $0$ if there is not. If there is a solution, exactly $N$ lines will follow, describing the constructed sequence. These $N$ lines must contain the order numbers of the dominoes in the sequence. Each order number will be followed by a space and a number, which can be $0$ or $1$ and will be equal to $1$ if the corresponding domino was rotated.

## Constraints and clarifications

$1 \leq N \leq 50000$ 

The numbers written on the dominoes can be between $0$ and $9$ inclusive 

## Example

`domino.in`
```
12
1 4
3 7
1 5
2 4
2 5
2 6
2 7
3 4
4 6
5 6
5 7
6 7
```

`domino.out`
```
1
3 0
11 0
12 1
9 1
8 1
2 0
7 1
6 0
10 1
5 1
4 0
1 1
```