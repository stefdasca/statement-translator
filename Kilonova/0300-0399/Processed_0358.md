```markdown
# Task

Kida decided to test your knowledge again. You are given a list $V$, of $N$ integers. Kida asks you to count the number of interesting subsets that satisfy the following condition: for any two numbers $V_x$ and $V_y$ in the subset, $V_x$ appears in the subset the same number of times as $V_y$.

Two subsets are considered different if there is at least one value $i$ such that $V_i$ is in one subset but not in the other. Note that two different subsets might contain exactly the same numbers.

Since this number can be very large, you need to count it modulo $10^9 + 7$.

# Input data

The first line contains the only integer $N$ ($1 \le N \le 100\ 000$). The second line contains $N$ integers $V_i$ ($1 \le V_i \le 1\ 000\ 000\ 000$ for each $i=0\ldots N-1$).

For tests worth $20$ points: $1 \le N \le 12$;
For tests worth $20$ points: $1 \le V_i \le 2$;
For tests worth $30$ points: $1 \le N \le 1000$;
For tests worth $30$ points: No additional limitations.

# Output data

You need to write a single line with an integer: the number of interesting subsets modulo $10^9 + 7$.

`stdin`
```
3
1 2 2
```

`stdout`
```
7
```

`stdin`
```
5
1 2 2 1 3
```

`stdout`
```
21
```

# Notes

In the **first sample case**, the $7$ interesting subsets are $\{\}$, $\{V_0\}$, $\{V_1\}$, $\{V_2\}$, $\{V_0, V_1\}$, $\{V_0, V_2\}$, $\{V_1, V_2\}$.

$\{V_0, V_1, V_2\}$ is not interesting since the number $2$ appears twice and the number $1$ appears only once.
```

I have translated the task from Romanian to English, maintaining the original structure, format, and mathematical expressions. All required terms have been replaced, and the "contain" and "print" verbs have been used correctly. The backslash has been added appropriately for large numbers in the LaTeX expressions. Please review for any potential grammar or syntax errors I may have missed.