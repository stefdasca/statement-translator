## Task

Alinuța received as a gift $n$ precious stones from several broken necklaces. Each stone is associated with a natural number, and stones with consecutive numbers are part of the same original necklace. There are no two precious stones with the same associated number. Alinuța also has $k$ magic stones, each with a certain power, expressed as a natural number. The power of a magic stone lies in the fact that it can transform into exactly $p$ precious stones with any consecutive values. By using a magic stone, Alinuța can merge two necklaces into one, provided that the power of the stone allows this. Each magic stone can only be used once. To merge two necklaces, a single magic stone can be used only if its power exactly covers the difference between two successive necklaces. Knowing the values associated with the $n$ precious stones and the power of each magic stone, help Alinuța determine:
- the number of necklaces she has initially
- the minimum number of necklaces she can get by obligatorily using all the precious stones and the magic stones
- the length of the longest necklace obtained by using at most one magic stone

## Input data

The input file `pietre3.in` contains:
- the first line contains a natural number $n$, representing the number of precious stones;
- the second line contains $n$ natural numbers separated by spaces, representing the values associated with the precious stones;
- the third line contains the value $k$, the number of magic stones;
- the last line contains $k$ natural numbers separated by spaces, representing the powers of the magic stones. 

## Output data

The output file `pietre3.out` will contain:
- the first line contains a natural value $d$, representing the number of necklaces she has initially;
- the second line contains the minimum number of necklaces that can be obtained by obligatorily using all the precious stones and the magic stones;
- the third line contains a natural value, representing the length of the longest necklace obtained by using at most one magic stone. 

## Constraints and clarifications

$ 1 \leq n \leq 100\ 000 $

$ 1 \leq k \leq 100\ 000 $

The values associated with the precious stones are natural numbers less than or equal to $1\ 000\ 000$

The values associated with the magic stones are natural numbers less than or equal to $1\ 000\ 000$

A single precious stone forms a necklace 

## Example

`pietre3.in`
```
9
1 2 3 6 11 8 7 14 9
3
2 1 2
```

`pietre3.out`
```
4
1
9
```

## Explanation

9
1 2 3 6 11 8 7 14 9
3
2 1 2 4 1 9

There are 4 necklaces $(1\ 2\ 3),\ (6\ 7\ 8\ 9),\ (11),\ (14)$

The magic stone that has the power $2$ can transform into stones $(4\ 5)$, leading to the formation of the necklace $(1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9)$

The magic stone that has the power $1$ transforms into $10$, merging the necklaces $(6\ 7\ 8\ 9)$ and $(11)$, and the magic stone that has the power $2$ transforms into $12\ 13$, merging $(11)$ with $(14)$

The longest subsequence can be obtained by merging the necklaces $(1\ 2\ 3)$ and $(6\ 7\ 8\ 9)$