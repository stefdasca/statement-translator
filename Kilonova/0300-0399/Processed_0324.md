# Task

Kida has found herself in the casino again! In front of her, there are $N$ roulettes, each having $M$ pins. Each of the $M$ pins of a roulette wheel is coded by a lowercase letter of the English alphabet.

Kida considers two roulettes to be similar if the configuration of the pins of the first roulette can be obtained on the second roulette by shifting left or right all the pins of the second roulette an arbitrary number of times. Note that each shift is a cyclic shift.

For example $abca$ can be obtained from $caab$, but $abac$ or $aacb$ cannot be obtained from $abca$.

Kida asks you to count the number of unordered pairs of similar roulettes.

# Input

The first line contains two integers $N$ and $M$ ($1 \le N * M \le 10^6$). Each of the following $N$ lines contains a string of $M$ characters representing a roulette.

For tests worth $20$ points: $N \le 100$, $M \le 100$.

For tests worth $20$ more points: $N \le 500$, $M \le 500$

For tests worth $60$ more points: No additional limitations.

# Output

You need to write a single integer, representing the number of unordered pairs of similar roulettes.

# Example 1

`stdin`

```
4 4
abcd
xbcd
cdab
dabc
```

`stdout`

```
3
```

# Example 2

`stdin`

```
3 6
adaada
aaadda
aadaad
```

`stdout`

```
1
```

# Notes

In the **first sample case**, the $3$ pairs are $(0, 2)$, $(0, 3)$ and $(2, 3)$.

In the **second sample case**, the only pair is $(0, 2)$.