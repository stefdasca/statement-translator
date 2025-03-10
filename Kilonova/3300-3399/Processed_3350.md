# Task

We have: $n$, $k$, and an array of $n$ natural numbers. This is a problem where we need to respond to a certain type of queries. We describe the meaning of one such query: given a position $p$ in the array ($p \geq k$). We imagine that the elements at positions from $p+1$ to $n$ are hidden (we don't know their values), but we can see the elements at positions from $1$ to $p$.

We know that we want to find **the maximum of every subarray of length $k$ that ends at positions greater than or equal to $p$**. Among the elements we can see, we want to identify a minimum number (as few as possible) such that we can be sure to determine the maxima of the indicated subarrays no matter what values the elements at positions from $p+1$ to $n$ have.

# Input data

The file `maxsecvk.in` contains on the first line the numbers $n$ and $k$ separated by space.  
The second line contains $n$ natural numbers, separated by spaces, representing the elements of the given array.  
The third line contains a number $t$.  
The fourth line contains $t$ natural numbers, separated by spaces, representing the positions $p$ for each query.

# Output data

The file `maxsecvk.out` will contain $t$ natural numbers representing the answer for each query, in the order they appeared in the input file.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* The elements of the given array are between $0$ and $1\ 000\ 000\ 000$ (inclusive).
* The hidden elements could have any value, but also within the range $0$, $1\ 000\ 000\ 000$ (inclusive).
* $1 \leq t \leq n$;
* The values from the queries can be any position in the array greater than or equal to $k$.
* The values $p$ can repeat in the input file.

# Example

`maxsecvk.in`
```
9 4
0 4 2 3 8 1 3 6 2
3
5 4 7
```

`maxsecvk.out`
```
1 2 2
```

## Explanation

For the query with $p = 5$, we consider that the array is `0 4 2 3 8 x x x x`.  
Only the element with value $8$ (at position $5$) can matter.

For the query with $p = 4$, we consider that the array is `0 4 2 3 x x x x x`.  
In the subarray ending at position $5$, the element with value $4$ could be the maximum. In the subarrays ending at position $6$ and larger, the maximum could be the element with value $3$.