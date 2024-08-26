## Task

Azusa, the witch from the mountains, recently got an apprentice, the dragon Laika, who hopes to learn the secrets of Azusa's incredible power. Unfortunately for Laika, the source of Azusa's power is nothing special: she has just practiced little by little for a long time. But as Laika keeps asking Azusa to give him something to do, Azusa invented the following programming problem. Azusa gives Laika an array of $N$ natural numbers, and then asks how many pairs of subsequences simultaneously satisfy the following three conditions:
1. The subsequences are disjoint.
2. Together, the subsequences form a subarray.
3. The bitwise XOR of the subsequences is equal.

## Input data

The input file `xorseq.in` contains on the first line $N$, and on the second line the given array.

## Output data

The output file `xorseq.out` must print the required number, modulo $10^9+7$.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$

$0 \leq$ an element of the array $< 2^{20}$

For 10 points, $1 \leq N \leq 15$

For another 30 points, $1 \leq N \leq 2\ 000$

For another 20 points, the array is randomly chosen from the set of possible arrays of its length.

## Example

`xorseq.in`
```
4
0 1 1 0
```

`xorseq.out`
```
20
```

`xorseq.in`
```
3
2 3 1
```

`xorseq.out`
```
3
```

`xorseq.in`
```
2
3 1
```

`xorseq.out`
```
1
```

`xorseq.in`
```
3
2 1 1
```

`xorseq.out`
```
2
```

## Explanation

In the first example, the pairs of subsequences that satisfy the required conditions are listed below. Each pair is written as a pair of sets of indices; thus the pair $(1, 3), (2, 4)$ represents a pair of subsequences where the first subsequence contains the first and third elements, and the second subsequence contains the second and fourth elements.

$(), (1)$

$(), (1, 2, 3)$

$(1), (2, 3)$

$(2), (1, 3)$

$(1, 2), (3)$

$(), (1, 2, 3, 4)$

$(1), (2, 3, 4)$

$(2), (1, 3, 4)$

$(1, 2), (3, 4)$

$(3), (1, 2, 4)$

$(1, 3), (2, 4)$

$(2, 3), (1, 4)$

$(1, 2, 3), (4)$

$(), (2, 3)$

$(2), (3)$

$(), (2, 3, 4)$

$(2), (3, 4)$

$(3), (2, 4)$

$(2, 3), (4)$

$(), (4)$