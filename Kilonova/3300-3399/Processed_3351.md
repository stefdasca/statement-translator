
# Task

You are given a sequence of $n$ natural numbers. You need to write a program that answers queries of the following type: for a given subarray, of length a power of $2$, identified by the indices $st$ (starting position) and $dr$ (ending position), we want to obtain the "minimum path". This is defined as a sequence of intervals obtained as follows:
- The first interval in the sequence is $st$, $dr$.
- If the minimum is only in the first half, the starting and ending indices of this half represent the next interval in the path.
- If the minimum is only in the second half, the starting and ending indices of this half represent the next interval in the path.
- If the minimum is in both halves, we include the half with more occurrences of the minimum in the path, and in case of a tie, the left half.
- We continue the path until reaching an interval of length $1$ that contains the minimum.

# Input data

The file `minpath.in` contains on the first line the number $n$, and on the second line the $n$ elements of the given sequence (in order by indices, from $1$ to $n$).  
The third line contains the number of queries, $t$. Each of the next $t$ lines contains the endpoints of an interval for which we need to find the minimum path.

# Output data

The file `minpath.out` contains $t$ lines, with each line being an even number of values representing the minimum path for the corresponding query from the input file, as follows: the first two numbers are the left and right endpoints of the first interval (the one given), the next two numbers are the left and right endpoints of the second interval, and so on, with the last two numbers being equal and representing the endpoints of the last interval, which is of length $1$.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* The elements of the given sequence are natural numbers with a maximum of nine digits.
* $1 \leq t \leq 100 \ 000$;
* The values $st$ and $dr$ from the queries satisfy the conditions: both are between $1$ and $n$, $dr-st+1$ is a power of $2$, and $st \leq dr$.

# Example 1

`minpath.in`
```
10
2 1 4 5 2 3 1 6 1 5
2
1 2
2 9
```

`minpath.out`
```
1 2 2 2
2 9 6 9 6 7 7 7
```

## Explanation

Explanation for the query `2 9`:  
The given subarray is:  
2 **1 4 5 2 3 1 6 1** 5 The starting and ending indices are displayed, $2$ and $9$.  
The minimum is present in both halves but appears more often in the second half  
2 1 4 5 2 **3 1 6 1** 5 The starting and ending indices are displayed, $6$ and $9$.  
In this case, the minimum is equally found in both halves, so we continue on the left  
2 1 4 5 2 **3 1** 6 1 5 The endpoints are displayed, $6$ and $7$.  
The minimum is on the right  
2 1 4 5 2 3 **1** 6 1 5 We reach an interval of length $1$, display its endpoints and stop.
