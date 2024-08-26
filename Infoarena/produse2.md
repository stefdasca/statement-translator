# Produse2

Let $A$ be an array of $N$ natural elements and $B$ be an array of $N - 1$ elements with the property that $B_i = A_i * A_{i+1}$. Given the array $B$, calculate how many valid arrays $A$ exist and specify one of these arrays.

## Input data

The input file `produse2.in` will contain on the first line an integer $T$ representing the number of tests. Each test has the following format: the first line contains an integer $N$; the second line contains $N - 1$ integers representing the array $B$. 

## Output data

The output file `produse2.out` will contain the answers for the $T$ tests. The answer for each test will be on one or two lines: the first line will contain the number of arrays $A$ that result in the given array $B$; if there is at least one solution, the second line will contain $N$ natural numbers, representing one of the valid arrays $A$. 

## Constraints and clarifications

$2 \leq N \leq 3 \cdot 10^5$ \
$1 \leq B_i \leq 3 \cdot 10^6$ \
If there are multiple solutions, any of them is acceptable. There will be at most $1\ 500\ 000$ numbers in the input file. 

## Example

`produse2.in`
```
2
4
27 36 24 
4
2 3 4 
```

`produse2.out`
```
2
3 9 4 6
0
```