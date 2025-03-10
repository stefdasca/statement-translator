Certainly! Here is the translated version of the competitive programming problem statement:

---

> when the ship sinks, the rats also sink.

In the kingdom of $\text{Tramperika}$, the beloved king, $\text{Murp Dorald}$, is seriously considering how to best tax his subjects. The kingdom is composed of $N$ districts, each encoded with a character ($a,b, \dots, z$). All districts encoded with the same character form an alliance, and the larger the number of districts in an alliance, the more our sovereign emperor worries. However, the royal advisor, $\text{Eleonor}$, devises an efficient plan to calm the waters, and, as any wise person would do, defines the tax of an interval $[l,r]$ as being $ \displaystyle \sum_{i = a}^{z} ord(i)^{fr(i)} $, where $fr(i)$ represents how many districts form an alliance with the code $i$, and $ord(i)$ is equal to the position in the alphabet of the letter $i$.

For example, consider the string $\color{#87CEEB}a \color{#FFC300}b \color{#87CEEB}a \color{#00ff6f}c \color{#FFC300}b \color{#FFC300}b \color{#00ff6f}c$, from which we deduce that the tax will be equal to $1^{2} + 2^{3} + 3^{2} + 4^{0} + \dots + 26^{0} = 41$.

~[king.png|align=center|width=30em]
$$
\text{Regele taxandu-\și supușii}
$$
# Task

Hearing about the great idea of $\text{Eleonor}$, $\text{Dorald}$ is amazed and wonders what the sum of the taxes for all intervals would be. Despite your moral inclinations, your role is to calculate the sum requested by the king and display it on the screen $\text{modulo} \ 10^9 + 7$.

# Input data

The first line contains $T$, the number of subtests. The first line of each subtest contains $N$, the number of districts, and the following line contains a string $S$ of $N$ characters.

# Output data

For each of the $T$ lines, print the requested sum for the corresponding subtest.

# Constraints and clarifications

* $1 \leq T \leq 100$.
* Let $Sm$ be the sum of the number of districts from the $T$ subtests.
* $1 \leq Sm \leq 2 \cdot 10^5$.
| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 12 | $1 \leq N \leq 10, Sm \leq 1 \ \ 000$ |
| 2 | 20 | $1 \leq Sm \leq 10^4$ |
| 3 | 10 | $S_i = a$ |
| 4 | 15 | $T \leq 2, S_i = a \ \ \text{or} \ \ S_i = \text{b and the number of characters equal to b} \leq 10^4$|
| 5 | 43 | $\text{No constraints}$ |

# Example 1

`trumperika.in`
```
5
10
fwcmxivdzu
1
b
10
cqwyywzywh
2
og
5
naovo
```

`trumperika.out`
```
4500
27
281184
118
1407
```

---