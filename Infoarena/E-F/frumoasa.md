## Task

Tractorel gave up (for the moment) heavy lions and drinking milk. Due to its value, it was captured by the Greeks. You are given 3 numbers $N$, $P$, $1000000007$ ( $10^9 + 7$ ) and an alphabet $\text{SIGMA} = \{'a', 'b', \dots, 'z'\}$ consisting of 26 letters. Consider a word formed from the letters $c_1, c_2, \dots, c_N$. We define the distance between 2 letters $c_i$, $c_j$ as $|i - j|$. Restricted by the Greeks, Tractorel can only form words of length $N$ using letters from the alphabet $\text{SIGMA}$ such that any 2 identical letters must be at least $P + 1$ distance apart. Tractorel is in big trouble, knowing that Romania - Greece will end 3-0, he asks for your help to count the sequences he can form in the presence of the Greeks. Attention! For obscure reasons, the result is desired to be displayed modulo $1000000007$.

## Input data

The input file `frumoasa.in` contains on the first line 2 numbers: $N$ and $P$.

## Output data

The output file `frumoasa.out` should contain a single number representing the answer.

## Constraints

$1 \leq N \leq 10^{15}$

$1 \leq P \leq N$

## Example

`frumoasa.in`
```
2 1
```

`frumoasa.out`
```
650
```

## Explanation

$ab$, $ac$, $\dots$, $az$, $ba$, $bc$, $\dots$, $yz$, $za$, $zb$, $\dots$, $zy$