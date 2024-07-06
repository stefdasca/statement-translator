The competitive programming problem statement in markdown, translated to English, while preserving the specified formats and instructions, is as follows:

---

On the occasion of the city of Suceava's day, the mayor decided to decorate the main street with flags. He bought $N$ red flags and $M$ blue flags. For each flag, we know its height. Furthermore, we know that he wants the flags of the same color to be on the same side of the street. Additionally, he wants to pair each red flag with a blue flag, aiming to make the number of pairs as large as possible. We define the discordance of a pairing as the maximum absolute difference in the heights of the paired flags. The mayor asks you to find the minimum discordance to make the city of Suceava as beautiful as possible.

# Task
Given two integers $N$ and $M$, then $N$ numbers (representing the heights of the red flags), then $M$ numbers (representing the heights of the blue flags). Display the minimum discordance.

# Input data
The input file `flags.in` contains the first line, two integers $N$ and $M$ separated by a space. The second line contains $N$ natural numbers separated by a space. The third line contains $M$ natural numbers separated by a space.

# Output data
In the output file `flags.out`, contain the result on the first line.

# Constraints and clarifications
* $1 \leq n, m \leq 10^5$
* $1 \leq$ height of a flag $\leq 10^9$
* For tests worth $20$ points, $N = M$.
* For tests worth $50$ points, $1 \leq N,M \leq 5\ 000$.
* For tests worth $40$ points, the maximum response is $150$.

# Example 1
`flags.in`
```
2 3
9 10
4 9 10
```
`flags.out`
```
0
```

## Explanation
We took the pairs $(9, 9)$ and $(10, 10)$.

# Example 2
`flags.in`
```
7 6
7 8 12 21 5 1 2
9 14 3 6 4 11
```
`flags.out`
```
3
```

---

I have ensured the translation maintains the structure and format, and fixed any potential grammar or syntax errors according to the rules of the English language.