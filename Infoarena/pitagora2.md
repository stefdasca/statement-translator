# Pitagora2

Pitagora is asking for your help. He wants to know if there exists a right triangle with integer side lengths, where the length of one of the legs is a given natural number, $N$. Display the length of the leg that, together with the one of length $N$, forms a right triangle with the minimum area. If no solution exists, display $-1$.

## Input data

The input file `pitagora2.in` will contain on the first line the natural number $N$.

## Output data

The output file `pitagora2.out` will contain on the first line the length of the leg that, together with the one of length $N$, forms a right triangle with the minimum area.

## Constraints

$1 \leq N \leq 250\,000\,000$  
The triangle must not be degenerate.  
The triangle inequality must be respected.

## Example

`pitagora2.in`  
```
12
```

`pitagora2.out`  
```
5
```

## Explanation

$12^2 + 5^2 = 13^2$. The area of the triangle is $\frac{12 \times 5}{2} = 30$.