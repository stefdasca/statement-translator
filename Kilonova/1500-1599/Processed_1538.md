Here is the translated problem statement:

---

Two sequences $S1$ and $S2$ consisting only of lowercase letters are given. We define a subsequence of length $K$ of a sequence $a$ as a sequence $a^{\prime} =\;a_{i_1} +\;a_{i_2} + \dots\; + a_{i_K}$, so that $i_1 < i_2 < \dots\; < i_K$.

# Task
Determine the maximum length of a subsequence from $S1$, formed by concatenating some anagrams of the sequence $S2$. Among all the subsequences with maximum length, determine the one that is lexicographically smallest.
\
A sequence $a$ of length $n$ is considered lexicographically smaller than a sequence $b$ of length $n$ if there is an index $i$ such that $a_1=b_1$, $a_2=b_2$, $\dots$, $a_{i-1}=b_{i-1}$ and $a_i < b_i$. If the lengths of the two sequences differ, the sequence with the smaller length is considered lexicographically smaller.

A sequence $a$ is an anagram of a sequence $b$ if, when sorted in ascending order, the two sequences are identical.

# Input data

In the file `anagrame.in`, the first line contains a natural number $P$. The second line contains the sequence $S1$, and the third line contains the sequence $S2$.

# Output data

In the file `anagrame.out`, if $P=1$, then the first line will contain a natural number representing the maximum length of a sequence with the required property, and if $P=2$, then the first line will contain the subsequence with the maximum length with the required property and which is lexicographically smallest.

# Constraints and clarifications

* $1 \leq |S2| \leq |S1| \leq 10^5$, where $|a|$ is the length of the sequence $a$.
* It is guaranteed that at least one anagram of $S2$ appears in $S1$.

# Example 1

`anagrame.in`
```
1
abbaaabababbaabaabba
aba
```

`anagrame.out`
```
15
```

## Explanation

Because the letter `a` appears $11$ times, $S2$ can appear at most $5$ times.

We notice the subsequence formed by the underlined letters $\text{\underline{ab}b\underline{aaababa}b\underline{baabaa}bba}$ so $\text{abaaabababaabaa}$ is a subsequence of maximum length, equal to $15$, with the required property.

# Example 2

`anagrame.in`
```
2
abbaaabababbaabaabba
aba
```

`anagrame.out`
```
abaaabaabaabaab
```

## Explanation

We notice that the subsequence meets the required property.

---