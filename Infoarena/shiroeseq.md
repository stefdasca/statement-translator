## Task

Shiroe's new activity involves trying to detect certain memorable phrases in some encrypted data streams. Specifically, he is given a string $S$ and a set of $K$ patterns $P_i$ (with $|P_i| \leq |S|$), all containing only lowercase letters. For each pattern $P$, a substring $S'$ of $S$ "strongly contains" $P$ if and only if every subarray $S''$ of length $|P|$ in $S'$ is an anagram of $P$. To find out how often each pattern appears in $S$, Shiroe needs to determine, for each $P_i$, the length of $S'_i$, the longest subarray of $S$ that "strongly contains" $P_i$. Note that a substring of a string $S = \langle s_1, \dots, s_n \rangle$ is another string $P = \langle p_1, \dots, p_k \rangle$ such that there exists a position $t$ (with $0 \leq t \leq n-k$) such that $s_{t+x} = p_x$ for all $x \in \{1, 2, 3, \dots, k\}$. Note that an anagram of a string $S$ is any other string $P$ that can be formed from $S$ by permuting the characters of $S$.

## Input data

The input file `shiroeseq.in` contains the number $T$, the number of tests. The first line of a test contains $S$. The second line of a test contains $K$. The next $K$ lines of each test contain the patterns $P_i$, in order.

## Output data

The output file `shiroeseq.out` contains the answers for each test in order. The answer for a test consists of $K$ lines, each representing the length of the required substring for the respective pattern.

## Constraints and clarifications

$1 \leq T \leq 10$  
$1 \leq |S| \leq 50\ 000$  
$1 \leq |P_1| + \dots + |P_K| \leq 50\ 000$

## Example

`shiroeseq.in` 
```
2 
ababab 
2 
ab 
abab 
abcaxa 
3 
a 
yyy 
ax
```

`shiroeseq.out` 
```
6 
6 
1 
2 
3
```

~[diagram.png|width=300|height=200]