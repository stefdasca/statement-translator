## Task

We have a data structure that allows for forward and backward operations in time. The data structure accepts $insert(val)$ and $erase(time,val)$ operations. Additionally, we can move forward or backward in time to add or delete one of these two operations. Periodically, we also have $query(time, val)$ operations, for which we need to respond with the smallest number greater than or equal to $val$ at the $time$ on the timeline, considering the operations so far. 

## Input data

We are given a natural number $M$ representing the number of operations. The next $M$ lines contain the description of each operation. The operations are of 5 types. Each row starts with the operation type:

If it's an operation of type 1, the $insert(val)$ operation is added. This operation represents the insertion of value $val$ at the time $-\infty$.

If it's an operation of type 2, the $erase(time, val)$ operation is added. This operation represents the deletion of value $val$, if it exists, at time $time$. It is not guaranteed that $val$ exists or will ever exist.

If it's an operation of type 3, an $insert(val)$ operation will be deleted from the structure. It is guaranteed that there is an $insert(val)$ operation with this value already in the structure.

If it's an operation of type 4, an $erase(time, val)$ operation will be deleted from the structure. It is guaranteed that there is an $erase$ operation with these values. If there are multiple $erase$ operations with these values, only one will be deleted.

If it's an operation of type 5, you need to answer the question: what is the smallest value present in the structure at time $time$ that is greater than or equal to $val$?

## Output data

In the output file `timetravel.out`, print on line $i$ the answer to the $i$-th $query$ operation. If such a number does not exist, print "Time paradox" (without quotes).

## Constraints and clarifications

$1 \leq M \leq 500\ 000$

$1 \leq N \leq 100\ 000$

where $N$ is the number of distinct values used in $insert(val)$ calls.

There will not be two $insert$ operations with the same value at the same time.

$-1\ 000\ 000\ 000 \leq time, val \leq 1\ 000\ 000\ 000$ for any operation.

## Example

`timetravel.in`
```
19 
5 -100 100 
1 100 
2 20 100 
2 10 50 
2 10 50 
5 0 50 
5 0 101 
5 5 100 
5 15 100 
5 20 0 
1 50 
5 0 50 
5 5 51 
5 9 50 
5 10 50 
4 10 50 
5 10 50 
4 10 50 
5 10 50 
```

`timetravel.out`
```
Time paradox 
100 
Time paradox 
100 
100 
Time paradox 
50 
100 
50 
100 
100 
50 
``}