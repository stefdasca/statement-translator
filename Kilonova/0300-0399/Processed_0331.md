On a winter holiday day, Lulu was bored and decided it was time to solve a computer science problem from the holiday assignment. It goes as follows:

"Given $N$ natural numbers on which only two operations can be performed:
1) \`1 x y val\`: all numbers at positions $x$, $x+1$, $x+2$, ..., $y-1$, $y$ become equal to $val$;
2) \`2 x y\`: the XOR sum of the numbers at positions $x$, $x+1$, $x+2$, ..., $y-1$, $y$ is required.

A natural number $Q$ is also given, followed by $Q$ operations which can be of type 1 or 2. The task is to correctly respond to all type 2 operations."

# Task
Because Lulu is a lazy kid, he asks you to solve the problem for him, and if you manage to solve it correctly, Lulu will offer you a bag of jelly beans in return.

# Input data
The first line contains the number $N$ of elements. The second line will contain the $N$ natural numbers on which the two operations will be performed. The third line contains the number $Q$ of operations on the array, then, on the next $Q$ lines, the operations described according to the statement will be given.

# Output data
Print, on separate lines, the answers to all type 2 queries.

# Constraints and clarifications
- $1 \leq N, Q \leq 1\ 000\ 000$;
- The values in the queries will fit into 32-bit data types;
- The order of the queries will be respected!
- Due to the large size of the input data, it is recommended to use the following instructions at the beginning of the **main()** function (C++ language):
```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

## Subtask 1: 20 points
- $1 \leq N, Q \leq 100$.

## Subtask 2: 80 points
- No additional constraints.

# Examples

`stdin`
```
3
1 2 3
2
1 1 2 4
2 1 3
```

`stdout`
```
3
