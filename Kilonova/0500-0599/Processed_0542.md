
A sequence $V$ containing $N$ integers numbered starting from $1$: $V_1, V_2, \ldots, V_N$ and two non-zero natural numbers $K$ and $L$, with the property that: $1 \leq K \leq L \leq N$ is given. `Mihai` only studies subarrays of length $L$, meaning subarrays formed by exactly $L$ elements located on adjacent positions in this sequence $V$.

He might ask himself the following question: â€œIf I rearrange the elements of the subarray of length $L$ starting at position $poz$ in the sequence $V$ in **ascending** order, which **value** would be at the $K$-th position in the resulting subarray?â€.

For the subarray in the sequence starting at position $poz$ and having $L$ elements, meaning $V_{poz}, V_{poz+1}, \ldots, V_{poz+L-1}$, the value of the element at the $K$-th position within the subarray is $V_{poz+K-1}$.

# Task
Help `Mihai` find the correct answer for $Q$ questions of the type described above!

# Input data
The input file `kth.in` contains three non-zero natural numbers $N$, $K$ and $L$, separated by a space, with the meanings described above. The next line contains, separated by a space, $N$ integers representing, in order, the elements of the array $V$. The following line contains the non-zero natural number $Q$, representing the number of questions formulated by `Mihai`. On each of the next $Q$ lines contains one non-zero natural number $poz$, representing the starting position of the subarray of $L$ elements for which the respective question is asked.

# Output data
The output file `kth.out` will contain $Q$ lines. On the $i$-th line will contain an integer representing the answer to the $i$-th question, in the order given in the input file, for each $i$: $1 \leq i \leq Q$.

# Constraints and clarifications

* $2 \leq N \leq 300\ 000$ and $1 \leq Q \leq 300\ 000$;
* $-50\ 000 \leq V_i \leq 50\ 000$, for each $i$: $1 \leq i \leq N$;
* $1 \leq poz \leq N - L + 1$, for each of the $Q$ questions;
* The values of $poz$ in the $Q$ questions are not necessarily distinct between any two of them.

|# | Score | Constraints|
| - | -- | ------------|
| 1 | 7  | $Q = 1$ and $V_1=V_2=\ldots=V_N$, meaning all elements in the array $V$ have the same value |
| 2 | 11 | $Q, N \leq 200$ |
| 3 | 12 | $Q, N \leq 1\ 000$ and $1 \leq V_i \leq 2\ 000$, for each $i$: $1 \leq i \leq N$ |
| 4 | 14 | $Q, N \leq 1\ 000$ |
| 5 | 27 | $1 \leq V_i \leq 23$, for each $i$: $1 \leq i \leq N$ |
| 6 | 29 | No additional constraints |

# Example 1

`kth.in`
```
5 2 3
4 -5 2 1 4
2
2
1
```

`kth.out`
```
1
2
```

## Explanation

There are $N = 5$ elements in the array $V = (4, -5, 2, 1, 4)$. For the first question (where $poz = 2$), if the subarray formed by $L=3$ elements: $(V_2, V_3, V_4)$ were sorted in ascending order, it would become: $(-5, 1, 2)$, which means that on the second ($K=2$) position within it would be the value $1$.

# Example 2

`kth.in`
```
5 2 3
1 5 2 4 3
2
2
1
```

`kth.out`
```
4
2
```

## Explanation

There are $N = 5$ elements in the array $V = (1, 5, 2, 4, 3)$, $K=2$ and $L=3$. 
$Q=2$ questions formulated.
```
