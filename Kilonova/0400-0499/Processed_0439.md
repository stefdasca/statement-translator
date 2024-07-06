The original text is a competitive programming problem statement written in Romanian, which I'll now translate into English. Let's start:

---

Two numbers, `N` and `T`, followed by a string `S` of length `N` are given. Then, `T` operations of 3 types are given:
1. A character is added to the end of the string `S`;
2. The string `S` is added to the set `M` only if it does not already exist in the set;
3. The number of strings in the set `M` that are suffixes of the string `S` is requested.

# Task
Print the answer to all operations of type `3`.

# Input data
The first line of the file `sufixe.in` contains two natural numbers `N` and `T`.
The second line of the input file contains the string `S`.
Each of the following `T` lines will contain the type of one of the 3 operations. On the same line as operation `1` there will be a character `a..z`;

# Output data
File `sufixe.out` will contain the answer to the operations of type `3`, one per line.

# Constraints and clarifications
* `1 \leq N \leq 1\ 000`
* `1 \leq T \leq 1\ 200\ 000`
* Initially, the set `M` is empty.

# Example
`sufixe.in`
```text
1 11
a
2
1 b
1 a
2
2
1 c
1 a
3
1 b
1 a
3
```
`sufixe.out`
```
1
2
```

Explanation
---
We start with the initial string `S = “a”`.
We add the string `S = “a”` to the set `M` => `M = {“a”}`;
We add the character `b` to the string `S` and get `S = “ab”`.
We add the character `a` to the string `S` and get `S = “aba”`.
We add the string `S = “aba”` to the set `M` => `M = {“a”, “aba”}`;
We add the string `S = “aba”` to the set `M` => `M = {“a”, “aba”}`;
We add the character `c` to the string `S` and get `S = “abac”`.
We add the character `a` to the string `S` and get `S = “abaca”`.
The result of operation `3` is `1`: `a`.
We add the character `b` to the string `S` and get `S = “abacab”`.
We add the character `a` to the string `S` and get `S = “abacaba”`.
The result of operation `3` is `2`: `a`, `aba`.

---

I have preserved the mathematical values, variable names, general syntax, structure, format, and custom image syntax as instructed. Please review and let me know if you need any further adjustments.