## Task

Let $X$ be a natural number. We define $f(X) = \text{the number of distinct values } K \text{ with the property that } X \text{ can be written as a product of } K \text{ digits other than } 1 . \text{ Given two natural numbers, } A \text{ and } B , \text{ calculate the sum } f(A) + f(A + 1) + \dots + f(B) . 

## Input data

The input file `smooth.in` will contain on its first line two natural numbers, $A$ and $B$ . 

## Output data

The output file `smooth.out` will contain a single natural number, the required sum from the statement. 

## Constraints and clarifications

$1 \leq A \leq B \leq 10^{16}$

For tests worth 60 points, the relation 
$B - A \leq 200\ 000$ also holds.

We consider that $f(1)$ is equal to zero. 

## Example

`smooth.in` 
```
5 17
```

`smooth.out`
```
17
```