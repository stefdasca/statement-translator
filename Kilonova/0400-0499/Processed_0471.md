```markdown
# Task

Consider a string $S$ consisting of lower case English letters, indexed from $0$. Find, for each $i >= 2$, the largest $l$ for which there exists $0 < j < i - l + 1$ where the strings $[s_0s_1 ... s_{l-1}]$, $[s_js_{j+1} ... s_{j+l-1}]$ and $[s_{i-l+1}s_{i-l+2} ... s_{i}]$ are equal. If no such $l$ exists, display the value $0$.

# Input data

The first line will contain a natural number $N$ representing the size of the string. The second line contains the string $S$.

# Output data

The output file will print on different lines, $N-2$ natural numbers representing the values of $l$ for each position greater than or equal to 2.

# Constraints and clarifications

* $1 \leq N \leq 10^6$;
* Subtask $1$ ($14$p), $N \leq 50$;
* Subtask $2$ ($16$p), $N \leq 200$;
* Subtask $3$ ($35$p), $N \leq 1\ 000$;
* Subtask $4$ ($20$p), $N \leq 100\ 000$;
* Subtask $5$ ($15$p), $N \leq 1\ 000\ 000$.

# Example 1

`stdin`
```
10
babaaabaab
```

`stdout`
```
0
0
0
0
1
2
0
1
```

# Example 2

`stdin`
```
15
ldildildildqldi
```

`stdout`
```
0
0
0
0
1
2
3
4
5
0
1
2
3
```
```