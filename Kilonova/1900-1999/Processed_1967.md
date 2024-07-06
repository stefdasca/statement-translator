```markdown
# Problem Statement
Alex learned at school about several sequences like the Fibonacci sequence. Moreover, he learned that he can create his own sequence. After doing that, being naturally curious, Alex studied multiple properties of it, including the remainders of its numbers when divided by other numbers, but he's unable to answer all his questions, so he asks you to help him.

# Task
Given a sequence formed by the recurrence relation $a_i=a_{i-1} \cdot x + y$. Given $Q$ queries of the form $l, r, k, m$ about how many numbers in the subarray $a_l \dots a_r$ give the remainder $k$ when divided by $m$, answer each query efficiently to help Alex.

# Input data
The input file `sirmod.in` will contain on the first line three integers: $a1, x, y$. The second line will contain the natural number $q$, with the meaning stated in the problem statement. On the next $q$ lines, there will be $4$ natural numbers, $l, r, k, m$.

# Output data
In the output file `sirmod.out` there will be $q$ lines, on line $i$ containing a single natural number, representing the answer to question $i$.

# Constraints and clarifications
* $1 \leq a_1,x,y \leq 10^9$
* $1 \leq q \leq 2 \cdot 10^5$
* $1 \leq m_i \leq 5000$
* $0 \leq k_i < m_i$
* $1 \leq l_i \leq r_i \leq 10^{18}$

For tests worth $30$ points: $1 \leq q \leq 100, 1 \leq l_i \leq r_i \leq 10^6$

For tests worth $60$ points: $1 \leq q \leq 5000$

# Example
`sirmod.in`
```
1 2 1
2
1 5 0 31
2 7 3 31
```

`sirmod.out`
```
1
2
```

# Explanation
The first $7$ numbers in the sequence are $1,3,7,15,31,63,127$
```