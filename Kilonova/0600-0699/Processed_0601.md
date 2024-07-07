
# Statement
Chertes has an array $v$ with $n$ natural numbers. This array is very valuable to our character, so he wants to save information about the array in such a way that he can reconstruct it in case he loses it. An information represents a pair of natural numbers $(x,y) (1 \leq x \leq y \leq n)$, which has the following meaning: save the sum of the elements in the subarray $v[x..y]$. Formally, save the sum of the elements $v_x, v_{x+1}, ... v_{y}$.
For example, if we have the array $v=[1,2,7,3,8]$, a valid information could be $(1,3)$ (the sum of the elements $1$, $2$ and $7$ is saved, which is $10$). However, the information $(2,1)$ is not valid because $2=x>y=1$.

# Task
Since Chertes is a lazy but clever boy, he asks you the following question: in how many ways can we save a minimum number of informations so that we can reconstruct the array? **Even worse!** He restricts saving certain informations. More precisely, there are $m$ pairs $(x,y)$ that represent the informations you cannot save, in other words, you cannot save the sum of the elements in the subarray $v[x..y]$. **Even worse!!** The number of ways is very large, so the remainder of its division by $10^9 + 7$ is required.
Two ways are different if one of them contains at least one different information from the other.

# Input data
The input file `lostarray.in` contains:
- The first line contains a natural number $n$ representing the number of elements in the array.
- The second line contains a natural number $m$ representing the number of restrictions.
- The next $m$ lines contain pairs of the type $(x,y)$ representing the fact that you cannot save the information $(x,y)$.

# Output data
The output file `lostarray.out` contains the number $k$ representing the number of ways modulo $10^9 + 7$.

# Constraints and clarifications
* $1 \leq n \leq 500$
* $0 \leq m \leq \frac{n \times (n + 1)}{2}$
* For tests worth $60p$ we have $m = 0$

# Example
`lostarray.in`
```
2
0
```
`lostarray.out`
```
3
```
# Explanations
There are 3 ways to save a minimum number of informations so that we can reconstruct the array: $[(1,1), (2, 2)]$, $[(1,1), (1, 2)]$ and $[(1,2), (2, 2)]$.
```

I have preserved the math, variable names, custom image format, and other specified syntax rules. If you notice any errors or inconsistencies in English grammar or syntax, please point them out!