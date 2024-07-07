
# Task

Ancient viking people carved stories on stone using their own symbols. Björn found $N$ versions of the same story and he already converted them to texts containing only the lowercase letters **a-z**. The texts are indexed from 0 to $N-1$, let's denote them with $S_0, S_1, \ldots S_{N-1}$. All the texts have the same length $K$, but they might differ on some positions.

Now Björn wants to know which is the original version of the story, because he thinks that the others are just mutated copies of it. He suspects that the original text is the one that has the minimal average distance from all the others. We define the distance between two texts as the number of positions where they differ.

More formally, the distance between two texts $S_i$ and $S_j$ denoted by $dist(S_i, S_j)$ is the number of different $k$ indices, for which $0 \leq k \leq K-1$ and $S_i[k] \neq S_j[k]$. We are looking for the text $S_{orig}$ for which the value $avgdist(S_{i})$ = $$\frac{1}{N-1} \sum_{j=0}^{N-1}{dist(S_{i}, S_j)}$$ is minimal. (Note that $dist(S_i, S_i) = 0$). If there are multiple texts with the same average distance from the others, you should choose the one which has the smallest index of those.

Can you help Björn to determine which one is the original text?

# Input

The first line contains two integers $N$ and $K$ ($1 \le N, K \le 10^5$), ($1 \le N * K \le 10^6$). The following $N$ lines each contain a string $S_i$ of length $K$ containing only lowercase English letters *abc...z*.

For tests worth $4$ points, $N = 2$.

For tests worth $11$ more points, $N = 3$.

For tests worth $21$ more points, $1 \le N, K \le 100$.

For tests worth $25$ more points, $S_i$ consists of only letters $a$ and $b$.

# Output

You need to write a single line with an integer between $0$ and $N-1$, the index of the original text. If there are multiple possible solutions, print the one with the smallest index.

# Example 1

`stdin`
```
3 3
aab
aba
aaa
```

`stdout`
```
2
```

# Example 2

`stdin`
```
5 7
abcdefg
abcdefh
abcdefh
abcdefi
abcdefj
```

`stdout`
```
1
```

# Explanation

In the **first sample case**,

* $avgdist(aab)$ = $$\frac{1}{2}(dist(aab, aba)$$ + dist(aab, aaa)) = $$\frac{1}{2}(2 + 1)$$ = $1.5$
* $avgdist(aba)$ = $$\frac{1}{2}(dist(aba, aab)$$ + dist(aba, aaa)) = $$\frac{1}{2}(2 + 1)$$ = $1.5$
* $avgdist(aaa)$ = $$\frac{1}{2}(dist(aaa, aab)$$ + dist(aaa, aba)) = $$\frac{1}{2}(1 + 1)$$ = $1$

So, the last text has the minimal average distance from the others, hence the answer is its index, which is 2.

In the **second sample case**, *abcdefh* has an average distance of $0.75$ while the other texts have an average distance of $1$, so the solution is the index of the first occurrence of *abcdefh*, which is 1.
