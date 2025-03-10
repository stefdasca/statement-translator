
# Task
Participating for the first time in an informatics olympiad, Gigel wants to impress everyone. To do this, he draws a sequence $A$ on the board, containing $N$ values which can be $0$ or $1$, followed by him performing a magic trick with it after the contest (something related to masks on bits, he thought). Unfortunately, during the contest, one of his best friends, wanting to play a prank on him, modified the sequence $A$ using the following type of operation an arbitrary number of times:
1. He chose a subarray of size $K$ from the sequence $A$.
2. He flipped all the values in the chosen subarray.

The olympiad is coming to an end, and Gigel wants to complete his magic trick, so he asks you to find the minimum number of operations that must be applied to the new sequence to bring it back to the initial sequence, or to tell him if this is impossible.

# Input data

The first line of the input file `bitstransform.in` contains two integers, $N$ and $K$.  
The second line will contain $N$ values of $0$ or $1$, representing the sequence $A$.  
The third line will contain $N$ values of $0$ or $1$, representing the sequence $B$.

# Output data

The first line of the output file `bitstransform.out` should contain a single integer, the minimum number of operations to transform $B$ into $A$, or -1 if there is no solution.

# Constraints and clarifications

* $1 \leq K \leq N \leq 1 \ 000 \ 000$;
* For tests worth 20 points, it is guaranteed that $1 \leq N \leq 100$.
* For tests worth 20 points, it is guaranteed that $1 \leq N \leq 1 \ 000$.
* For tests worth 20 points, it is guaranteed that $1 \leq N * K \leq 1 \ 000 \ 000$.
* For tests worth 30 points, there are no other constraints.
* 10 points will be awarded automatically.

# Example 1

`bitstransform.in`
```
5 2
1 0 1 1 1
0 0 0 0 0
```

`bitstransform.out`
```
3
```

## Explanation

The subarrays that we will flip are [4, 5], [1, 2], [2, 3], totaling 3 operations.

# Example 2

`bitstransform.in`
```
5 2
1 0 1 1 0
0 0 0 0 0
```

`bitstransform.out`
```
-1
```

## Explanation

The initial sequence cannot be obtained using only the operations described in the statement.
