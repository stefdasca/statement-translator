Here's the translated competitive programming problem statement:

---

A stack is initially empty. The elements of the stack are numbered starting from $1$ from the bottom to the top. We have to process $T$ types of commands:

$\\rightarrow$ `0 x` - add the element $x$ to the top of the stack  
$\\rightarrow$ `1 x y add` - add the value $add$ to all elements in the interval $x\\ y$  
$\\rightarrow$ `2` - remove the top element of the stack

**Display the top element of the stack after each operation**.

It is guaranteed that:
1. the operation of type $2$ will not be performed unless there are at least $2$ elements in the stack
2. the first operation will be of type $0$

# Input data

The input file `izi.in` contains in the first line a natural number $T$, and on the following $T$ lines, the operations performed on the stack.

# Output data

The output file `izi.out` contains $T$ lines, representing the top elements of the stack after each operation.

# Constraints and clarifications

* $1 \leq T \leq 1 \ 000 \ 000$
* $\minus 1 \ 000 \leq add \leq 1 \ 000$
* For operations of type $1$, $\minus 1 \ 000 \leq x \leq 1 \ 000$, and for operations of type $2$, the number of elements in the stack is greater than $y$.
* For $36$ points: $1 \leq T \leq 1 \ 000$.
* For an additional $33$ points: All operations of type $2$ will be at the end of the input file.

# Example

`izi.in`
```
7
0 1
1 1 1 2
0 2
1 1 2 3
2
0 4
2
```

`izi.out`
```
1
3
2
5
6
4
6
```

---