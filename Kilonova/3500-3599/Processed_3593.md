The access codes for the elevator in an office building are natural numbers with a maximum of $9$ digits. Each code is formed by pressing some of the keys from $0$ to $9$. Over time, certain keys, pressed more often than others, wear out and thus, the corresponding digits become invisible.

The service engineer wants to replace the most worn-out $2$ keys. If more than $2$ keys are worn out to the maximum, the engineer chooses the ones with the highest digit value. Additionally, it is desired to identify the least frequently used key among the pressed keys (a key is considered used if it has been pressed at least once).

# Task

Write a program that displays:
- The key with the smallest value among those used the fewest times, if the task is $1$;
- The $2$ keys that will be replaced, if the task is $2$.

# Input data

The input file `lift.in` contains on the first line the task number, $c$. The second line contains a natural number $n$. The third line contains exactly $n$ natural numbers representing the access codes.

# Output data

The output file `lift.out` will contain:
- For task 1, the key used the least;
- For task 2, the values of the $2$ keys with maximum wear. The numbers shown will be written in ascending order and will be separated by a single space (it is guaranteed that at least $2$ distinct keys have been used).

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* The formed codes can have a minimum of one and a maximum of $9$ digits
* The formed codes can repeat
* $45$ points are awarded for task $1$, $45$ points for task $2$, and $10$ points by default.

# Example 1

`lift.in`
```
1 
4 
196048 947561 16497 245096
```

`lift.out`
```
2
```

## Explanation

The task is $1$.  
Keys $2$ and $8$ have been used only once.  
We choose the smallest among them.

# Example 2

`lift.in`
```
1 
3 
100 100 100 
```

`lift.out`
```
1
```

## Explanation

The task is $1$.
Key $1$ is the least used.

# Example 3

`lift.in`
```
2 
4 
192048 947521 12497 245096 
```

`lift.out`
```
4 9
```

## Explanation

The task is $2$.
Keys $2$, $4$, and $9$ have been used $4$ times each.  
We choose the two largest among them.

# Example 4

`lift.in`
```
2 
4 
196068 947561 16497 245096
```

`lift.out`
```
6 9
```

## Explanation

The task is $2$.
Key $6$ was pressed $5$ times. Key $9$ was used $4$ times.  
They are the most worn keys, we display them in ascending order.

# Example 5

`lift.in`
```
2 
3 
1500 1500 1500
```

`lift.out`
```
0 5
```

## Explanation

The task is $2$.  
Key $0$ was pressed $6$ times. Keys $1$ and $5$ were used $3$ times each.  
We choose the largest from keys $1$ and $5$.  
**Display is in ascending order.**