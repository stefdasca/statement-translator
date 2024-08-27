# Kino

On a wall of a pyramid, some archaeologists discovered $N$ sequences of strictly positive natural numbers, all of length $L$. Unfortunately, over time, some of the numbers were erased. Besides these sequences, they also know a special sequence $K_i$, also of length $L$, but without missing numbers, found on a parchment. It is known that the initial sequences follow a strange property: the numbers at position $i$ in each sequence are between $1$ and $K_i$ (inclusive). Since the sequences are of no use to them and because they are paid by the hour, archaeologists started playing with them by asking different questions. Thus, they defined the distance between two sequences as the number of corresponding positions with different values. For example, the distance between the sequences $[1 \ 2 \ 5 \ 3 \ 3]$ and $[3 \ 2 \ 1 \ 10 \ 3]$ is $3$. Based on this concept, they wonder with what numbers they should fill the missing places so that the property is still respected and the sum of the distances between any two initial sequences is maximum. Since the archaeologists are not skilled in computer science, they could not solve the problem and therefore asked you to help them.

## Input data

The first line of the file `kino.in` contains $2$ natural numbers $N$ and $L$, having the significance from the statement. The second line contains $L$ numbers representing the sequence from the parchment. The next $N$ lines contain $L$ numbers each, representing the sequences found by archaeologists. In place of missing numbers, the digit $0$ appears.

## Output data

In the output file `kino.out` you will display the maximum possible sum of the distances between any two sequences.

## Constraints and clarifications

$1 \leq N \leq 20\ 000$

$1 \leq L \leq 50$

$1 \leq K_i \leq 1\ 000\ 000\ 000$

For $30\%$ of the tests $1 \leq N, K_i \leq 500$

## Example

`kino.in`  
```
3 3
5 4 2
1 0 2
1 3 0
4 4 0
```

`kino.out`  
```
7
```

## Explanation

A solution that achieves the maximum sum could be composed of the sequences $[1 \ 1 \ 2]$, $[1 \ 3 \ 1]$, and $[4 \ 4 \ 1]$. The distance between the first two sequences is $2$, between the first and the third $3$, and between the second and the third $2$. Thus, the total (and maximum possible) sum is $7$.