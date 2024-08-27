Koba

Miruna has encountered the great wizard Koba. He has just discovered a magic sequence of numbers, which will allow him to travel through time. The first three terms of the sequence are $T_1$, $T_2$, and $T_3$. The following terms are calculated using the formula $T_i = T_{i-1} + T_{i-2} * T_{i-3}$. To travel through time, the wizard calculates the last digit for the first $N$ terms of the sequence, and then sums them up. Since he is very old, it is very difficult for him to find the much-desired answer, so he asks Miruna to help him.

## Input data

The input file `koba.in` contains 4 integers $N$, $T_1$, $T_2$, and $T_3$, having the meaning from the statement.

## Output data

The output file `koba.out` will contain a single number representing the sum of the last digits of the first $N$ terms of the sequence.

## Constraints

$1 \leq T_1$, 
$T_2$, 
$T_3 \leq 10000$ 

$1 \leq N \leq 10^8$ 

## Example

`koba.in`
```
1000 9 7 23 
```
`koba.out`
```
4660
```