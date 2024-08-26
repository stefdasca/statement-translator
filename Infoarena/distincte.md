## Task

Zaharel has an array of $N$ elements with natural number values between $1$ and $K$. He asks himself $M$ questions of the form: what is the sum of the distinct elements between positions $i$ and $j$ in the array?

## Input data

The input file `distincte.in` contains the numbers $N$, $K$, $M$ separated by spaces on the first line. The next $N$ lines will contain elements of the array. The next $M$ lines will describe the questions: two numbers $i$, $j$ $(1 \leq i \leq j \leq N)$ separated by spaces on each line.

## Output data

The output file `distincte.out` will contain $M$ numbers, the $i$th number representing the answer to the $i$th question. The result will be printed modulo $666013$.

## Constraints and clarifications

$1 \leq N, M \leq 100000$

$1 \leq K \leq N$

The elements in the array are numbered from $1$ to $N$

## Example

`distincte.in` 
```
6 3 2 
1 
2 
2 
1 
3 
1 
2 5 
1 4 
```

`distincte.out`
```
6 
3 
```

## Explanation

The elements in the array between positions $2$ and $5$ are $2$ $2$ $1$ $3$ and the sum of the distinct ones is $2 + 1 + 3 = 6$. 

The elements in the array between positions $1$ and $4$ are $1$ $2$ $2$ $1$ and the sum of the distinct ones is $1 + 2 = 3$.