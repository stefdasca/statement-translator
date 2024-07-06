# Task

Filippo loves keyboards, and he just bought a new one for his collection.

Filippo's new keyboard is made of $10$ keys arranged in a row, each containing a digit from $0$ to $9$. Initially the digits are arranged in ascending order, i.e. the first key contains $0$, the second key contains $1$, and so on.

To test the new keyboard, Filippo decided to type a string $S$. Unfortunately, he is not very good at typing, in fact he only uses a single finger to press the keys. His finger can only move left or right, one key at a time, and he can only press a key if his finger is on it. In the beginning, his finger is on the first key, i.e. the key containing $0$.

Filippo can also swap the digits on two keys at any time (even before he starts typing), but he can only do this operation once. He does not move his typing finger while performing this operation, and he can do it even if his finger is on one of the two keys.

To get more practice, Filippo wants to type $T$ different strings $S_1, S_2, \dots, S_T$. How many times does he need to move his finger to type the string $S_i$?

Note that he types the strings independently of each other, i.e., when Filippo starts typing a string, the keyboard always contains the digits from $0$ to $9$ in ascending order, and Filippo can swap the digits on two keys at most once for every string.

# Input data

The first line contains the only integer $T$ ($1 \le T \le 20\ 000$), the number of strings.
The following $T$ lines contain the strings $S_1, S_2, \dots, S_T$ (Each string $S_i$ contains only digits from $0$ to $9$).

The length of each string is less than $100\ 000$.

The total length of the strings does not exceed $100\ 000$.

For tests worth $30$ points: Each string $S_i$ contains only $2$ different digits..

For tests worth $30$ points: The total length of the strings does not exceed $1000$.

For tests worth $40$ points: No additional limitations.

# Output data

You need to print $T$ lines with an integer: the minimum number of times Filippo needs to move his finger to type the string $S_i$.

`stdin`
```
1
73
```

`stdout`
```
3
```

`stdin`
```
3
01234
09018
9752123
```

`stdout`
```
3
12
15
```

# Notes

In the **first sample case** Filippo can swap the digits $2$ and $7$ before starting to type the string $73$.
Then he can type the string by moving his finger $3$ times:
* He moves his finger $2$ times to the right and presses the key (it now contains $7$)
* He moves his finger $1$ time to the right and presses the key containing $3$

In the **first case of the second sample** Filippo can move his finger $3$ times in total using the following strategy:
* He presses the key containing $0$
* He moves his finger $1$ time to the right and presses the key containing $1$
* He moves his finger $1$ time to the right and presses the key containing $2$
* He moves his finger $1$ time to the right and presses the key containing $3$
* He swaps the keys containing $3$ and $4$
* He now presses the key containing $4$ (he does not need to move his finger)