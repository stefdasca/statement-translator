## Task

Tassadar has discovered a Xel'Naga necklace consisting of $N$ diamonds, each diamond $i$ having an associated carat number $V_i$. The magical power offered by a necklace is $\max(V_i, 1 \leq i \leq N) - \min(V_i, 1 \leq i \leq N)$. He wants to divide the necklace into multiple necklaces of equal lengths, while respecting the following conditions:
- each new necklace must represent a subarray of the initial necklace
- each pearl of the initial necklace must be part of exactly one new necklace
- the total power offered by the new necklaces must be maximized

Since Tassadar is not a very skilled jeweler, he asks you to tell him the maximum power he can achieve through a division of the necklace.

## Input data

The input file `collar.in` contains on the first line the natural number $N$ as described in the statement. The next line contains $N$ integers $V_i$ representing the number of carats for each diamond.

## Output data

The output file `collar.out` will contain a single number, representing the maximum sum of powers that Tassadar can obtain by dividing the necklace.

## Constraints and clarifications

$1 \leq N \leq 65536$

$-1000000000 \leq V_i \leq 1000000000$

The initial necklace is circular

We recommend using signed 64-bit integers

## Example

`collar.in`
```
6
4 2 3 1 2 1
```

`collar.out`
```
5
```

## Explanation

We divide the sequence into the subarrays $\{4, 2, 3\}$ and $\{1, 2, 1\}$.

Another valid division is $\{4, 2\}$ $\{3, 1\}$ $\{2, 1\}$ (we can consider these divisions because the initial necklace is circular).