## Task

Shinozaki Mikoto has $N$ objects to transport from location $A$ to location $B$. The weight of each object is known. Mikoto is curious about the minimum capacity $D$ she needs so that she can transport all $N$ objects in 2 trips. Mikoto can transport a set of objects if the sum of their weights is less than or equal to $D$.

## Input data

The input file `overdrive.in` will contain on the first line a natural number $N$. The next line will contain $N$ natural numbers: the $i$th element represents the weight of the $i$th object.

## Output data

The output file `overdrive.out` will contain a single natural number representing the required minimum capacity $D$.

## Constraints and clarifications

$1 \leq N \leq 32$

The weights of the $N$ objects are natural numbers in the range $[1, 2\ 000\ 000\ 000]$

## Example

`overdrive.in`

```
4
1 3 5 2
```

`overdrive.out`

```
6
```