## Task

Haralambie decided to try a new business in the construction field. He already acquired $N$ types of bricks of identical sizes but different colors, with $C_i$ bricks of each type. He will stack bricks on top of each other to build towers according to the following rules:
- Each tower must contain only bricks of different colors.
- All towers must have the same height.

Haralambie's goal is to use as many bricks as possible in his constructions. Not being passionate about computer science, he relies on you to answer $M$ questions of the type: "What is the maximum number of bricks I can use to build at most $L_i$ towers?". Besides the glory, Haralambie will also ensure that you get the remaining bricks.

## Input data

The input file `caramizi.in` will contain on the first line the numbers $N$ and $M$ with the meanings as described. On the next line, there will be $N$ natural numbers $C_1$, $C_2$ $\dots$ $C_N$, representing the number of bricks of each type. On the last line there will be $M$ numbers $L_1$, $L_2$, $\dots$, $L_M$, with the meaning as described.

## Output data

The output file `caramizi.out` will contain $M$ lines, each containing the answer to the corresponding question from the input file.

## Constraints and clarifications

- $1 \leq N \leq 200000$ 
- $1 \leq M \leq 200000$ 
- $1 \leq C_i \leq 1000000$ 
- $1 \leq L_i \leq 2000000000$

For 30% of the tests used for evaluation

- $1 \leq N \leq 100$
- $1 \leq M \leq 100$
- $1 \leq C_i \leq 100$
- $1 \leq L_i \leq 100$

For another 20% of the tests used for evaluation

- $1 \leq N \leq 500$
- $1 \leq M \leq 5000$
- $1 \leq C_i \leq 100$
- $1 \leq L_i \leq 5000$

For another 30% of the tests used for evaluation

- $1 \leq L_i \leq 1000000$

It is recommended to use 64-bit signed integers for displaying results.

## Example

`caramizi.in`

```
5 5
4 7 10 11 13
3 12 13 14 21
```

`caramizi.out`

```
15
40
40
42
45
```

## Explanation

In the first case, Haralambie builds 3 towers, each containing all 5 types of bricks, arranged in any way.

The next two cases have the same solution, where Haralambie builds 10 towers with 4 bricks each.

In the fourth case, Haralambie will use the maximum number of bricks by building 14 towers with 3 bricks each.

In the last case, Haralambie can use all the bricks he has available.