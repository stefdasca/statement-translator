
# Task

Given an array $a$ of $N$ elements.  
<br>
Define:  
$f(x) = \begin{cases}  
1 &\text{if } x = 1 \\  
1 + f(\lfloor \sqrt{x} \rfloor) &\text{if } x > 1  
\end{cases}$  
<br>
Compute: $\sum_{i=1}^N \sum_{j=i}^N f(\sum_{k=i}^j a_k)$.

# Input data

The first line contains $N$, and the second line contains the array $a$.

# Output data

Print the required sum.

# Constraints and clarifications

* $1 \leq N, a_i \leq 2 \cdot 10^6$
* For $70$ points $1 \leq N, a_i \leq 2 \cdot 10^5$
* It is recommended to use the following code sequence for fast input:
```cpp
ios_base::sync_with_stdio(false);
cin.tie(0);
```

# Example 1

`stdin`
```
2
1 3
```

`stdout`
```
6
```

# Example 2

`stdin`
```
8
123 423 12 48 1 2 3 99999
```

`stdout`
```
160
```
