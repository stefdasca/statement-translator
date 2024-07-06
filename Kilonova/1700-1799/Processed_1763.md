Alibaba must discover the cipher that opens the chest containing the great treasure. The cipher is very hard to find. He has discovered multiple stones, each stone having a different color, with a natural number of at most $4$ digits written on each stone. Alibaba observes that the numbers on each stone are distinct from each other. The rule by which the cipher is formed is very simple, and Alibaba managed to figure it out quite easily: the cipher is formed by concatenating, in a certain order, all the stones. What Alibaba also knows is that in position $p$ of the cipher, the digit $k$ is certainly found.

# Task

Write a program that determines the number of cipher variants Alibaba will have to try. The number, being very large, will be computed modulo $46\ 337$.

# Input data

The input file `cifru.in` contains on the first line three natural numbers $n$, $p$, and $k$ separated by a space, representing the total number of numbers on the parchment, position $p$, and respectively the digit $k$ which is found at position $p$ in the cipher. The next $n$ lines contain one of the $n$ numbers on the parchment on each line.

# Output data

The first line of the output file `cifru.out` must contain a natural number representing the number of variants modulo $46\ 337$ of ciphers that Alibaba will have to try.

# Constraints and clarifications:

* $0 < n < 25$
* The numbers on each stone are strictly positive and less than $10\ 000$ and are distinct from each other.
* $0 \leq k \leq 9$
* Two ciphers differ from each other in the order of arranging the stones, even if the number obtained by reading the numbers on the stones is the same. For example, if there are three stones with the numbers $12$, $3$, and respectively $123$, they can be concatenated as $12 - 3 - 123, 123 - 12 - 3$, the two ciphers being considered different, the digits having different colors.

# Example

`cifru.in`
```
7 6 2
12
56
3
214
523
6
2
```

`cifru.out`
```
1548
```
