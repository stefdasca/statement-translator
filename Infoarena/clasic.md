## Task

Maria loves traveling a lot. Her father promised her that he would take her to Bucharest, to the National Informatics Contest "Adolescent Grigore Moisil", only if she knows how to solve the following problem: Given $T$ arrays of $N$ elements, determine for each one the xor sum of elements that appear an odd number of times. The xor operation represents the exclusive disjunction operation performed on the bits of the operands. In Pascal, the corresponding operator is `xor`, and in C/C++ this operator is `^`. For example, $20$ xor $14 = 26$.

## Input data

The input file `clasic.in` will contain on the first line the natural number $T$. The next $T$ lines will each contain a natural number $N$, followed immediately on the next line by $N$ numbers.

## Output data

The output file `clasic.out` will contain $T$ lines, each containing the answer for each test.

## Constraints and clarifications

For all evaluation tests, $T = 2$.

$N \leq 4\,000\,000$

The numbers in the array are less than or equal to $10^{11}$.

## Example

`clasic.in`
```
1
1
2
```

`clasic.out`
```
2
```