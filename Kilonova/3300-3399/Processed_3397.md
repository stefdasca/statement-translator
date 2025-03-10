**Note: During the competition, we increased the time limit to 1.5 seconds but will lower it back to 0.6 seconds to encourage more efficient solutions.**

Bobi has discovered an amusing data structure, namely the heap. More precisely, the heap is a tree data structure where each node has a certain value and at most two direct children, namely the left child and the right child. The heap can be of two types:
- **max-heap**, where the value of each node is **greater** than the values of its direct children. As a result, the root of the **max-heap** contains the **maximum** value in the heap.
- **min-heap**, where the value of each node is **less** than the values of its direct children. As a result, the root of the **min-heap** contains the **minimum** value in the heap.

For example, here is a max-heap containing the numbers $[1, 2, 3, 3, 4, 6]$:
~[maxheap.png]

Bobi plays with the first type of heap mentioned above, initially adding $N$ numbers to it. He wants to apply $Q$ operations of the following types:
- $1 \\ val$ - Bobi inserts the value $val$ into the heap;
- $2 \\ val$ - Bobi deletes one of the occurrences of the value $val$ from the heap. If it doesn't exist, the heap will remain unchanged;
- $3 \\ k \\ r$ - Bobi extracts the largest $k$ values from the heap, then decreases all of them by $r$ and inserts them back into the heap. If $k \\geq \\text{the size of the heap}$, then all values will be extracted from the heap.

# Task

Help Bobi to obtain the heap after the end of the operations and display the numbers from the final heap in descending order.

# Input data

The first line contains the numbers $N$ and $Q$.
The second line contains the $N$ numbers, in descending order, representing the initial heap.
The next $Q$ lines contain the operations as described in the statement.

# Output data

The final heap will be displayed on a single line, with numbers separated by a single space, in descending order.

# Constraints and clarifications

* $0 \\leq N, Q \\leq 100 \\ 000$;
* $-1 \\ 000 \\ 000 \\ 000 \\leq heap_i \\leq 1 \\ 000 \\ 000 \\ 000$;
* $1 \\leq k_i \\leq N+Q$;
* $0 \\leq r_i \\leq 10 \\ 000$;
* The elements of the initial heap are given in descending order;
* For $15$ points: $N, Q \\leq 1 \\ 000$;
* For another $10$ points: $k_i = 1$;
* For another $44$ points: $N, Q \\leq 60 \\ 000$;
* The use of fastio is recommended.

# Example 1

`stdin`
```
8 1
8 8 8 8 5 4 4 1
3 5 2
```

`stdout`
```
6 6 6 6 4 4 3 1
```

## Explanation

The largest $5$ elements are $8$, $8$, $8$, $8$, and $5$. By decreasing them by $2$ and inserting them back into the heap, we get $[6, 6, 6, 6, 4, 4, 3, 1]$.

# Example 2

`stdin`
```
0 7
1 4
1 5
1 7
3 2 4
2 3
1 6
1 7
```

`stdout`
```
7 6 4 1
```

## Explanation

Initially, the heap is empty.
After the first operation, $4$ is inserted. The heap is: $[4]$.
After the second operation, $5$ is inserted. The heap is: $[5, 4]$.
After the third operation, $7$ is inserted. The heap is: $[7, 5, 4]$.
After the fourth operation, the largest $2$ numbers, namely $7$ and $5$, are extracted. By decreasing them by $4$ and inserting them back into the heap, we get $[4, 3, 1]$.
After the fifth operation, $3$ is deleted. The heap is: $[4, 1]$.
After the sixth operation, $6$ is inserted. The heap is: $[6, 4, 1]$.
After the seventh operation, $7$ is inserted. The heap is: $[7, 6, 4, 1]$.