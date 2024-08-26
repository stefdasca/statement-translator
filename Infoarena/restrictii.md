## Constraints

A natural number $VAL$ is given, and an array $A$ consisting of $N$ natural numbers in the interval $[0, VAL - 1]$. The array $A$ is subject to a series of $M$ constraints of the form: the sum of the elements at positions between $X$ and $Y$ (inclusive of $X$ and $Y$) must be equal to $Z$, modulo $VAL$. Given $VAL$, $N$, and the $M$ constraints, calculate the number of arrays $A$ that satisfy all the $M$ constraints and display the result modulo $666013$.

## Input data

The input file `restrictii.in` will contain on the first line the numbers $N$, $M$, and $VAL$. The following $M$ lines will contain values $X$ $Y$ $Z$, as described in the task. 

## Output data

The output file `restrictii.out` will contain on the first line the desired number of arrays, modulo $666013$. 

## Constraints

$1 \leq N \leq 50000$ 

$1 \leq M \leq 100000$ 

$1 \leq VAL \leq 1000000000$ 

## Example

`restrictii.in` 
```
5 5 6 
1 5 2 
3 4 5 
4 5 0 
4 4 4 
3 5 1 
```

`restrictii.out` 
```
6 
0 
```

## Explanation

For the first example, the solutions are 
```
1 0 1 4 2 
3 4 1 4 2 
4 3 1 4 2 
2 5 1 4 2 
0 1 1 4 2 
5 2 1 4 2
```
For the second example, there are no solutions that satisfy all the $3$ constraints.