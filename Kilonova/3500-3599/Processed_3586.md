> Preda, what did you get?
> 100
> In bees, right?
> Yes
> Well, bees is penalizing.
> What about you, Dumitrache?
> 60

# Task

For the string $s$, we denote $len(s)$ = the length of the string $s$. We define $[l, r]$ from the string $s$ = the subarray from $l$ to $r$ of the string $s$ (for example, $[3, 4]$ from the string $abcdee$ = $cd$).  

We define $f(s, t)$, where $s$ and $t$ are two strings as:  

- If $t$ does not appear as a subsequence in $s$, $f(s, t) = -1$;  
- Otherwise, $f(s, t)$ = the maximum length of a subarray $[l, r]$ that can be removed from $s$ so that $t$ still appears as a subsequence in $s$.  

If we remove the subarray $[l, r]$ from $s$, $s$ will become:  
$s_1s_2s_3...s_{l-1}s_{r+1}s_{r+2}...s_{len(s)-1}s_{len(s)}$

We say that $t$ appears as a subsequence in $s$ if and only if there exist $len(t)$ indices $1 \leq i_1 < i_2 < i_3 < i_4 < ... < i_{len(t)} \leq len(s)$ such that $t_j=s_{i_j}$, where $1 \leq j \leq len(t)$.

For example, for $s = aabcd$ and $t = ac$, $f(s, t) = 2$, because we can remove the subarray $[2, 3]$ from $s$, which becomes $acd$, and $ac$ still appears as a subsequence.  

For $s = ggggg$ and $t = a$, $f(s, t) = -1$, because $t$ does not appear as a subsequence in $s$.  

For exactly $5$ pairs of strings $(s_i, t_i)$, display $f(s_i, t_i)$.  

# Input data

In the input file `carmuz.in`, on the $2 \cdot i$-th line, contains the string $s_i$, and on the $2 \cdot i + 1$-th line contains $t_i$, for $1 \leq i \leq 5$.  

# Output data

In the output file `carmuz.out`, on the next $5$ lines, contains the value $f(s_i, p_i)$, for $1 \leq i \leq 5$.  

# Constraints and clarifications

* We denote with $S_{len(s)}$ = the sum of the lengths of the strings $s$, and $S_{len(t)}$ = the sum of the lengths of the strings $t$;  
* $1 \leq S_{len(s)}, S_{len(t)} \leq 500\,000$;
* It is guaranteed that $s_i$ and $t_i$ contain lowercase letters, for $1 \leq i \leq 5$;

| Nr. | Points | Constraints |
|----|--------|-----------|
| 1  | 16      | $S_{len(s)}, S_{len(t)} \leq 10$ |
| 2  | 18     | $S_{len(s)}, S_{len(t)} \leq 500$ |
| 3  | 20     | $len(s_i) \leq len(t_i)+10$, for $1 \leq i \leq 5$ |
| 4 | 19    | $S_{len(s)}, S_{len(t)} \leq 5\,000$ |
| 5  | 27     | No other constraints |

# Example

`
carmuz.in
`

```
kbkbkg  
bkg  
bbbab  
bbbba  
bbbab  
bbbab  
gkghj  
ggh  
ghgkgjgkg  
gj  
```

`
carmuz.out
`

```
3  
-1  
0  
1  
4  
```

### Explanation

- For $s = kbkbkg$ and $t = bkg$, we can remove $[1, 3]$, so the answer is **3**.  
- For $s = bbbab$ and $t = bbbba$, $t$ does not appear as a subsequence, so the answer is **-1**.  
- For $s = bbbab$ and $t = bbbab$, $t$ appears as a subsequence, but we cannot remove any subarray, so the answer is **0**.