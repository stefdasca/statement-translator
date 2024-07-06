The Powerpraff girls and boys are seated in a string $s$ of length $K$, represented in the string by the characters `f` and `b`. With the appearance of new episodes, cloning has also been discovered, and this string has been multiplied $N$ times, with the new string of length $N \cdot K$ arranged in lines of $D$ characters each. Two boys are friends if they are adjacent horizontally or vertically in the new line arrangement. Two boys $B_x$ and $B_y$ are in the same group if they are friends or if there exists a sequence of boys $B_1, B_2, \dots, B_m$ (possibly $m$ can also be $0$) such that in the sequence $B_x, B_1, B_2, \dots, B_m, B_y$ any two adjacent boys are friends. A group can consist of at least one boy.

# Task

Given the values of $K$, $N$, and $D$, as well as the characters from the string $s$, find the number of groups that can be formed, knowing that each boy belongs to a single group.

# Input data

The input file `fsb.in` contains the numbers $K$, $N$, and $D$ on the first line, in this order, and on the second line the $K$ characters of the string $s$.

# Output data

The output file `fsb.out` will contain on the first line the number of groups that can be formed.

# Constraints and clarifications

* $1 \leq K \leq D \leq 2 \ 000$
* $1 \leq N \leq 1 \ 000 \ 000$
* $N$ is divisible by $D$.
* For tests worth $23$ points, we have $K = D$.
* For other tests, worth $31$ points, we have $N = D$ and $K < D$.
* For other tests, worth $46$ points, there are no additional constraints.

# Example 1

`fsb.in`
```
3 3 3
fbb
```

`fsb.out`
```
1
```

## Explanation

After multiplying $3$ times the string $s = fbb$ becomes `fbbfbbfbb`. It is arranged in lines of length $3$, obtaining the arrangement:

```
fbb
fbb
fbb
```

One group is formed, with all the boys in the same group.

# Example 2

`fsb.in`
```
2 3 3
fb
```

`fsb.out`
```
3
```

## Explanation

After multiplying $3$ times, the string $s = fb$ becomes `fbfbfb`. It is arranged in lines of length $3`, obtaining the arrangement:

```
fbf
bfb
```

Three groups are obtained, each consisting of a single boy.

# Example 3

`fsb.in`
```
3 8 4
fbb
```

`fsb.out`
```
3
```

## Explanation

After multiplying $8$ times the string $s = fbb$ becomes `fbbfbbfbbfbbfbbfbbfbbfbb`. It is arranged in lines of length $4`, obtaining:

```
fbbf
bbfb
bfbb
fbbf
bbfb
bfbb
```

Three groups are obtained.
