## Factorials

We define $P!$ ($P$ factorial) as the product of the first $P$ positive integers. Given $N$ natural numbers $x_1, x_2, \dots, x_N$. We denote by $M = (x_1!) \ast (x_2!) \ast \dots \ast (x_N!)$. Determine the smallest non-zero natural number that must be multiplied by the number $M$ so that the result can be written in the form $A^K$, where $K$ is given and $A$ is a natural number. 

## Input data

The input file `factoriale.in` contains in the first line the numbers $N$ and $K$, separated by a space. The second line contains the numbers $x_1, x_2, \dots, x_N$. 

## Output data

The output file `factoriale.out` will contain the minimum number that fulfills the required property.

## Constraints

$1 \leq N \leq 100$

$2 \leq K \leq 100$

$1 \leq x_i \leq 100$ 

## Examples

`factoriale.in`
```
2 2
2 4
```

`factoriale.out`
```
3
```

## Explanation

$M = 2! \ast 4! = 2 \ast 24 = 48$. $48 \ast 3 = 144 = 12^2$. $3$ is the smallest natural number with the property that the result of the multiplication between it and $48$ is a perfect square.