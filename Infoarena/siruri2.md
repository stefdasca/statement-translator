## Task

Count how many increasing arrays of length $N$ can be formed with natural numbers from the interval $[1, M]$ such that each array contains at most $K$ distinct numbers.

## Input data

The input file `siruri2.in` contains on the first line three natural numbers $N$, $M$, $K$ with the significance from the statement.

## Output data

The output file `siruri2.out` will contain a single natural number representing the number of arrays that satisfy the conditions from the statement.

## Constraints and clarifications

$1 \leq N \leq 8000$  
$1 \leq M \leq 100000$  
$1 \leq K \leq 2000$  

The result will have at most $7000$ digits.

## Example

`siruri2.in`  
```
4 3 2
```

`siruri2.out`  
```
12
```

## Explanation

The $12$ arrays are: 
- $1 1 1 1$
- $1 1 1 2$
- $1 1 1 3$
- $1 1 2 2$
- $1 1 3 3$
- $1 2 2 2$
- $1 3 3 3$
- $2 2 2 2$
- $2 2 2 3$
- $2 2 3 3$
- $2 3 3 3$
- $3 3 3 3$