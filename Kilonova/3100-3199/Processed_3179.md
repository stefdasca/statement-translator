Sure, let's translate the given competitive programming problem statement from Romanian to English, while maintaining the specified structure, formatting, and syntax.

---

Bahoi isn't doing his math holiday homework; instead, he's grinding on [vampire survivors](https://vampire-survivors.fandom.com/wiki/Vampire_Survivors_Wiki).

# Task

Initially, Bahoi's HP is $R$ units. There are $N$ monsters, and the $i$-th monster has a strength of $a_i$ units. He has a piece of [floor chicken](https://vampire-survivors.fandom.com/wiki/Floor_Chicken) at his disposal, which has the power to restore $P$ units of HP.

The game consists of $N$ rounds. In round $i$, the following can happen:
* $R$ becomes $R - a_i$. If after this operation $R$ drops below $1$ ($R \leq 0$), then Bahoi loses and the game ends.
* If he survives, then $R = R + P$.

The game ends after $N$ rounds. Find the minimum positive $P$ such that after completing the $N$ rounds, Bahoi remains alive. If Bahoi cannot win regardless of the value of $P$, output $-1$.

# Input data

The first line contains $t$, the number of test cases. The first line of each test case contains three numbers $N$ and $R$, and the next line contains exactly $N$ numbers separated by a space.

# Output data

Print $t$ lines, the answers to the $t$ test cases.

# Constraints and clarifications

* $1 \leq N, t \leq 2 \cdot 10^5$
* $1 \leq R, a_i \leq 10^9$
* It is guaranteed that the sum of the $N$ values over all test cases is $\leq 2 \cdot 10^5$.

# Example

`stdin`
```
7
4 14
5 7 8 7 
2 17
2 6 
5 11
2 8 7 8 2 
6 5
4 5 3 4 4 1 
8 3
2 1 9 2 1 2 9 4 
2 12
9 5 
4 18
4 3 4 7 
```

`stdout`
```
5
0
5
5
5
3
1
```

## Explanation

In the first test case, for $P = 4$, the values of $R$ during the game will be: $9, 6, 2, 6$. We note that in the last round $a_4 > 6$, so the answer is $5$.

In the second test case, for $P = 0$, Bahoi can win the game.

--- 

This concludes the translation while preserving the structure and format specified.