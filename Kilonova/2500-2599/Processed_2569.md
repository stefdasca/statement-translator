> Happy Birthday, Mugur! May you live for 1,000,000 years!

Mugur received a gift from his son Mugurel on his birthday, a **stack**. After partying with friends at the Cultural Hall in the Rubber Duck Empire, he goes home excited and starts performing operations on it.

The operations are of two types:

* $\\text{push } x$ — The number $x$ is added to the stack ($x$ becomes the top element of the stack).
* $\\text{pop}$ — The top element of the stack is removed. If the stack is empty, the operation has no effect.

Unfortunately, the stack was not of the highest quality, so after performing $N$ operations on it, an error called *maCmAcMac* occurs, and it can no longer execute other operations.

# Task

Being an old duck, Mugur cannot instantly remember all the operations he performed, but each day he remembers one operation and its position in the initial sequence of operations. To avoid boredom, he asks himself daily: given only the operations up to the current day, if we execute them in the order of their indices, what would be the top element of the **stack**?

# Input data

The input file will contain on the first line an integer $N$, representing the number of operations.

Each line $i$ from the next $N$ lines contains one operation: a natural number $p_i$ representing the index of the operation, a string $s_i$ representing the type of operation, and a natural number $x_i$ if the operation is of type $\\text{push}$, representing the number that is pushed onto the stack.

# Output data

The output file will contain $N$ lines, each line containing a single natural number: the top element of the stack considering the current operations or `-1` if the stack is empty.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$
* $1 \\leq x_i \\leq 10^9$
* $s_i \\in \\{ \\text{push}, \\text{pop} \\}$
* $1 \\leq p_i \\leq N$
* All operation indices are distinct.
* All numbers are integers.
* Mugurel apologizes for the inconvenience, next time he will buy a higher quality gift.
* For tests worth $5$ points, the operation indices are in increasing order.
* For other tests worth $5$ points, all operations are of type $\\text{push}$.
* For other tests worth $8$ points, $N \\leq 5 \\ 000$.
* For other tests worth $13$ points, all $\\text{push}$ operations occur before $\\text{pop}$ operations.
* For other tests worth $69$ points, there are no additional constraints.

# Example 1

`mugur.in`
```
4
1 push 2
4 pop
2 push 3
3 push 4
```

`mugur.out`
```
2
-1
2
3
```

## Explanation

In this example, we have the following operations after each day:

* After the first day, we have the operations: $\\text{push} \\ 2$. The top of the stack is $2$.
* After the second day, we have the operations: $\\text{push} \\ 2$, $\\text{pop}$. The stack is empty.
* After the third day, we have the operations: $\\text{push} \\ 2$, $\\text{push} \\ 3$, $\\text{pop}$. The top of the stack is $2$.
* After the fourth day, we have the operations: $\\text{push} \\ 2$, $\\text{push} \\ 3$, $\\text{push} \\ 4$, $\\text{pop}$. The top of the stack is $3$.

# Example 2

`mugur.in`
```
7
1 pop
4 push 7
2 push 9
5 pop
3 push 5
6 pop
7 pop
```

`mugur.out`
```
-1
7
7
9
5
9
-1
```

## Explanation

In this example, we have the following operations after each day:

* After the first day, we have the operations: $\\text{pop}$. The stack is empty.
* After the second day, we have the operations: $\\text{pop}$, $\\text{push} \\ 7$. The top of the stack is $7$.
* After the third day, we have the operations: $\\text{pop}$, $\\text{push} \\ 9$, $\\text{push} \\ 7$. The top of the stack is $7$.
* After the fourth day, we have the operations: $\\text{pop}$, $\\text{push} \\ 9$, $\\text{push} \\ 7$, $\\text{pop}$. The top of the stack is $9$.
* After the fifth day, we have the operations: $\\text{pop}$, $\\text{push} \\ 9$, $\\text{push} \\ 5$, $\\text{push} \\ 7$, $\\text{pop}$. The top of the stack is $5$.
* After the sixth day, we have the operations: $\\text{pop}$, $\\text{push} \\ 9$, $\\text{push} \\ 5$, $\\text{push} \\ 7$, $\\text{pop}$, $\\text{pop}$. The top of the stack is $9$.
* After the seventh day, we have the operations: $\\text{pop}$, $\\text{push} \\ 9$, $\\text{push} \\ 5$, $\\text{push} \\ 7$, $\\text{pop}$, $\\text{pop}$, $\\text{pop}$. The stack is empty.