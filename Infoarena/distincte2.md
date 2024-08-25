## Task

Since he was caught playing on his phone during Potions class, Professor Snape gave Harry an additional assignment for the next day. Given an array $A$ with $N$ natural numbers representing the spell codes cast by the Hogwarts students in the past 24 hours, Harry must answer $M$ questions such as: "How many distinct spells with codes in the interval $[X,Y]$ were cast in the last day?" Being too busy with Ginny, he asks you to make a program to help him answer all of Professor Snape's questions.

## Input data

The input file `distincte2.in` will contain on the first line the natural numbers $N$ and $M$ representing the number of elements in the array and the number of questions respectively.

The 2nd line of the input file will contain the $N$ elements of the array.

The following $M$ lines will each contain 2 numbers $X$ and $Y$ $(X \leq Y)$ representing the start and end of an queried interval.

## Output data

The output file `distincte2.out` will have $M$ lines.

Line $i$ will contain a single natural number representing the answer to the $i$-th question.

## Constraints

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 100\ 000$

$1 \leq A[i] \leq 1\ 000\ 000$

$1 \leq X \leq Y \leq 1\ 000\ 000$ for each query

## Example

`distincte2.in`
```
8 4
2 7 5 3 1 2 3 4
1 2
2 5
3 3
1 10
```

`distincte2.out`
```
2
4
1
6
```