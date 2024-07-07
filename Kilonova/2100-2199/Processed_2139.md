
# Task

You are given an array $A$ of $N$ values. From this array, we can choose any two adjacent elements with equal values and merge them into an element with a value incremented by $1$. 
What is the minimum length to which we can reduce the array so that it becomes a $COX$ array? 
A $COX$ array is an array in which the XOR of any two adjacent elements has an odd number of $1$ bits. 
For example, the elements $1$ and $3$ can be adjacent in a $COX$ array because $1 \oplus 3 = 2$, and $2$ has an odd number of $1$ bits (it has $1$ bit).

# Input data

The first line contains $N$. 
The second line contains the array $A$.

# Output data

Print the minimum length of a $COX$ array that we can achieve, or $-1$ if we cannot achieve any $COX$ array.

# Constraints and clarifications

* $1 \leq N \leq 10^3$
* $1 \leq A_i \leq 20$
* An array that contains a single element is considered $COX$.
* The problem admits only $100$ point solutions.

# Example 1

`stdin`
```
5
1 2 1 1 2
```

`stdout`
```
3
```

## Explanation

The minimum length is $3$ and we obtain it as follows:

$(1, 2, 1, 1, 2) \rightarrow (1, 2, 2, 2) \rightarrow (1, 3, 2)$.

# Example 2

`stdin`
```
4
2 1 1 5
```

`stdout`
```
-1
```

## Explanation

We cannot obtain a $COX$ array.
