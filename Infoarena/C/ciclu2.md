## Task

Given an undirected graph with $V$ nodes and $E$ edges, and $Q$ questions of the form: "Is there a simple cycle of length $length$ that contains node $x$?", you are asked to answer the given questions.

## Input data

The input file `ciclu2.in` contains on the first line two integers, $V$ and $E$, as described in the statement. On the next $E$ lines, there are two integers $x$ and $y$ representing an edge between nodes $x$ and $y$. On the next line, there is an integer $Q$ indicating the number of questions. On the following $Q$ lines, there are two numbers $x$ and $length$ representing a question.

## Output data

In the output file `ciclu2.out`, you will print $Q$ lines with the answers to the questions. If the answer to a question is YES, you will print $1$, otherwise, you will print $0$.

## Constraints and clarifications

$1 \leq V \leq 200$

$1 \leq E \leq 350$

$1 \leq Q \leq 10$

$1 \leq length \leq 8$

## Example

`ciclu2.in`
```
5 6
1 2
2 3
3 1
3 4
4 5
5 3
3
1 3
3 6
4 5
```

`ciclu2.out`
```
1
1
0
```