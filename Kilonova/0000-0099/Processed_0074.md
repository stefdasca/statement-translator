# Task

Miguel has learned how to write numbers in base 2 and how bitwise operations work, so he invented the following game:

You are given an array of $N$ numbers $v_1$, $v_2$, ..., $v_n$ and $Q$ queries. For each query, you are given two natural numbers $A$ and $B$ meaning that $v_A$ becomes equal to $B$. After each query, you need to display the magic number corresponding to the new array. Note that after displaying the magic number, the array **does not** revert to its initial state.

The magic number of an array $V$ of length $N$ is equal to the sum of all numbers in the subarrays $a_1$, $a_2$, ..., $a_n$. For $i=1$, $a_i$ is equal to $V$ and for each $i \\gt 1$, $a_i$ contains the results of the bitwise `AND` operation between any two consecutive numbers in $a_{i-1}$, maintaining the relative order of the pairs. Note that the subarray $a_i$ contains $N-i+1$ elements.

For example, if $V=\\{1,3,5,7\\}$, then $a_1=\\{1,3,5,7\\}, a_2=\\{1,1,5\\}, a_3=\\{1,1\\}, a_4=\\{1\\} $ and the magic number of $V$ is equal to $(1+3+5+7)+(1+1+5)+(1+1)+(1)=26$.

# Input data

The first line contains the natural numbers $N$ and $Q$. The second line contains $N$ integers $v_1$, $v_2$, ..., $v_n$. The following $Q$ lines contain a query in the form `A B`.

# Output data

Print the $Q$ magic numbers, each on a new line.

# Constraints and clarifications
* $1 \\leq N, Q \\leq 100\ 000$
* $0 \\leq a_i \\leq 100\ 000$ for any $1 \\leq i \\leq N$
* $0 \\leq B \\leq 100\ 000$
* $1 \\leq A \\leq N$

# Example
`stdin`
```
5 4
1 5 3 7 4
5 3
2 2
3 4
1 7
```

`stdout`
```
35
31
24
32
```

# Explanation

After the first query, the array becomes $1,5,3,7,3$ and the magic number is equal to $(1+5+3+7+3)+(1+1+3+3)+(1+1+3)+(1+1)+(1)=35$. To obtain $a_2$ we perform the following operations: $1\\&5$, $5\\&3$, $3\\&7$, $7\\&3$.