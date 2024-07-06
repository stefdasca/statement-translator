> A man enters a bar. The bartender asks him:
> -What can I serve you?
> - I would like a non-alcoholic beer, he replies.
> To which the bartender responds:
> -Sure, would you also like a coloring book?

For a certain number $n$ and a certain number $m$, a sequence of parentheses is said to be *good* if it has length $n$ and has exactly $m$ correctly parenthesized subarrays.

# Task

Given $n$ and $m$, display a good sequence of parentheses. If it does not exist, display `-1`. Because this is too easy for you, you will have to do this $T$ times.

# Input data

The first line contains a number $T$, representing the number of tests. On line $i + 1$, there will be two numbers $n_i$ and $m_i$, representing the input data for case $i$.

# Output data

On line $i$, print `-1` or a good sequence of parentheses for case $i$.

# Constraints and clarifications

* $1 \leq T \leq 10^4$
* $1 \leq \displaystyle\sum_{i=1}^T n_i \leq 10^5$
* $0 \leq m_i \leq n_i^2$
* **The displayed sequence does not need to be correctly parenthesized**.
* A sequence is called correctly parenthesized if and only if characters `+` and `1` can be inserted so that the resulting sequence represents a correct [mathematical expression](https://en.wikipedia.org/wiki/Mathematical_expression). For example `(())` and `()(())` are correctly parenthesized sequences because `(1+(1+1))` and `(1+1)+(1+(1+1))` are correct mathematical expressions, but `(()` and `())(()` are not correctly parenthesized sequences.

# Example

`stdin`
```
3
6 4
2 4
4 2
```

`stdout`
```
()(())
-1
(())
```

## Explanation

For the first case, the correctly parenthesized subarrays are `()(())`, `()` (the first two characters), `(())` and `()` (the fourth and fifth characters).

For the second case, it can be demonstrated that there is no solution.

For the third case, the correctly parenthesized subarrays are `()` and `(())`.