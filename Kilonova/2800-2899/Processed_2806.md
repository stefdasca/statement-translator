> "The Ace of Spades represents judgment — a cut at the ideal point. With reason and logic, you must cut between good and evil." This is how you should choose what problems to spend your time on.

~[asp.png|align=right]

Given two natural numbers $A$ and $B$ where $A \leq B$. All natural numbers in the interval $[A, B]$ will be concatenated in some order such that they form a (very large) number $G$ as large as possible. For example, for the interval $[1, 3]$, the value of $G$ is $321$.

# Task

You need to answer $Q$ questions of the form: "What is the digit at position $K$ in the number $G$, considering that the first digit of the number $G$ is at position $0$?" It is guaranteed that this position exists.

# Input data

The first line of the input contains two numbers $A$ and $B$.

The second line contains a single integer representing the number of questions $Q$.

The third line contains $Q$ integers, representing the values $K$ from the $Q$ questions.

# Output data

The output should contain a continuous sequence of $Q$ digits, where the $i$-th character in the sequence represents the answer to the $i$-th question. No spaces should be printed between digits.

# Constraints and clarifications

* $1 \leq A \leq B \leq 10^{17}$
* $1 \leq Q \leq 50\ 000$
* _**Attention!**_ Let $x, y, z$ be three natural numbers. We denote with $xy, xz, yz$ etc. the concatenation of the numbers $x, y, x, z, y, z$. It can be demonstrated that if $xy \leq yx$ and $yz \leq zy$, then $xz \leq zx$.

| # | Points | Constraints          |
| - | ------ | -------------------- |
| 1 | 4      | $B - A \leq 7$       |
| 2 | 4      | $A$ and $B$ have the same number of digits and $Q \leq 10\ 000$ |
| 3 | 10     | $B - A \leq 100\ 000$|
| 4 | 33     | $1 \leq Q \leq 30$   |
| 5 | 23     | $1 \leq Q \leq 1\ 000$|
| 6 | 16     | $1 \leq Q \leq 10\ 000$|
| 7 | 10     | No additional constraints.    |

# Example 1

`stdin`
```
8 13
4
0 3 8 9
```

`stdout`
```
9310
```

## Explanation

$G = 9813121110$

# Example 2

`stdin`
```
1 144
15
0 1 2 3 4 5 6 7 8
9 10 11 12 13 14
```

`stdout`
```
999989796959493
```