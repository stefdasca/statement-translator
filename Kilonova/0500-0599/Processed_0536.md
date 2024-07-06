Kida and The Harmless Bandito have $N$ digital displays that can show lowercase letters from the English alphabet. Each of these $N$ displays has $M$ cells. For each display $i$, we know the letters that can be displayed in each of its cells $j$.

For example, if $M = 3$ and a display can show letters $\{b, x\}$ in the first position, letters $\{y, z, c\}$ in the second position, and letters $\{d, a\}$ in the third position, we can form words like $byd$, $bya$, $bza$, etc.

The Harmless Bandito considers a word of length $M$ to be common if it can be formed on at least $K$ out of the $N$ displays. Hearing this, Kida asks you to help her calculate the number of distinct common words.

# Task
Help Kida calculate the number of distinct common words. Since this number can be very large, compute it modulo $10^9 + 9$.

# Input data
The first line of the input file contains three numbers: $N$, $M$, and $K$, as described above. The next $N$ lines contain $M$ strings of characters, consisting of distinct lowercase letters of the English alphabet, separated by spaces. The $j$-th string on the $i + 1$ line of the input file represents the characters that the $i$-th display can show in position $j$.

# Output data
The output file will contain the remainder when dividing by $10^9 + 9$ the number of distinct common words.

# Constraints and clarifications
- $1 \leq K \leq N \leq 22$
- $1 \leq M \leq 22$
- The $N$ displays can only show lowercase letters of the English alphabet.

|# | Points | Constraints|
| - | - | ---------- |
|1|11|$K = N$|
|2|13|$1 \leq N, M \leq 15$ and all $N$ displays can only show characters from the set $\{a, b\}$|
|3|14|$1 \leq M \leq 4$|
|4|25|$1 \leq N \leq 10$|
|5|22|$1 \leq M \leq 10$, $1 \leq N \leq 20$|
|6|15|no additional constraints|

# Example
`comun.in`

```
4 3 2
ab bc ad
ba bc dz
bx yzc da
ax cd zwyhd
```

`comun.out`

```
7
```

There are 4 displays that can show words of length $3$. The words that can be displayed on at least two displays are: $bca$, $abd$, $bbd$, $acd$, $bcd$, $xcd$, and $acz$.