Pavare2

In the city of Z, there is a boulevard with a width of $1$ meter and a length of $N$ meters that needs to be paved. The city hall has white and black tiles of $1$ meter in length and $1$ meter in width for paving the boulevard. As you can imagine, the boulevard will be paved by placing $N$ tiles from the city hall's stock. To choose the best paving method, the mayor first wants to know how many paving ways exist such that there are no more than $A$ consecutive white tiles and $B$ consecutive black tiles on the boulevard. The mayor then wants to know the $K$-th paving possibility in lexicographic order, knowing that a white tile is lexicographically smaller than a black tile.

## Task

Given the number $N$ representing the length of the boulevard and the numbers $A$, $B$, and $K$, find the number of paving possibilities that meet the conditions stated. Also, determine and print the $K$-th paving possibility in lexicographic order, encoding a white tile with $0$ and a black tile with $1$.

## Input data

The first line of the file `pavare2.in` contains the numbers $N$, $A$, $B$, separated by spaces. The second line of the file contains the number $K$.

## Output data

The first line of the file `pavare2.out` contains a single number representing the number of paving possibilities, and the second line must print the requested paving encoded as stated, without displaying spaces between the characters $0$ and $1$.

## Constraints

$1 \leq N \leq 100$

$1 \leq A \leq N$

$1 \leq B \leq N$

It is guaranteed that there are at least $K$ ways to pave the boulevard and $K \geq 1$

For $50\%$ of the tests $K = 1$

## Example

`pavare2.in`

```
4 2 3 7
```

`pavare2.out`

```
12
1001
```

## Clarifications

The $12$ paving possibilities are, in lexicographic order:
$0010$ 
$0011$ 
$0100$ 
$0101$ 
$0110$ 
$0111$ 
$1001$ 
$1010$ 
$1011$ 
$1100$ 
$1101$ 
$1110$

It is observed that the $7$-th paving possibility is $1001$.