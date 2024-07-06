Bulanel just discovered an interesting problem involving data structures and thought to propose it for the contest you're participating in. You need to implement a data structure we'll call MStack, which supports all the operations of a regular stack (push, pop, top) plus the middle operation (which returns the element found in the middle of the stack). To make this problem more challenging, Bulanel adds the following constraints: Your MStack can only use $13$ regular stacks (numbered from $1$ to $13$) as internal storage, and the number of operations on these stacks must be less than or equal to $5 \times$ the number of operations on the MStack.

The operations that will be executed on the MStack are:
* `push`: adds the value $x$ to the top of the MStack, where $x$ is the number of push operations performed up to the current moment;
* `top`: returns the value from the top of the MStack;
* `middle`: returns the value in the middle of the MStack (if there are $N$ elements in the stack, the element in the middle is found in position $\frac{N}{2}+1$ counting from the base of the stack);
* `pop`: removes the element from the top of the MStack.

To prevent cheating, you must write the operations you perform on the $13$ stacks to the output file, and the allowed operations are:

* `move a b`: moves the element from the top of stack $a$ to the top of stack $b$;
* `pop a`: discards the element from the top of stack $a$;
* `push a`: adds the value $x$ to the top of stack $a$, where $x$ is the number of push operations performed up to the current moment;
* `top a`: answers the top or middle operation of the MStack, i.e., the element at the top of stack $a$ is the element from the top or middle of the MStack.

# Task
Given a set of operations that will be executed on the MStack, you need to execute a sequence of operations on the $13$ stacks such that:

1. For each push or pop operation in the input file, there is a corresponding push or pop operation in the output file, maintaining the order from the input file;
2. For each top and middle operation in the input file, there is a corresponding top operation in the output file, maintaining the order from the input file;
3. All push, top, and middle operations must be answered exactly in the order from the input file;
4. The move operation can be inserted between any two operations.

# Input data

The input file `mstack.in` contains on the first line the number of operations $N$, and on the following $N$ lines will be described the $N$ operations, one per line.

# Output data

The output file `mstack.out` contains the operations that will be executed on the $13$ stacks, one operation per line, in the order they will be executed.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$
* For $30\%$ of the tests $1 \leq N \leq 1\ 000$
* It is guaranteed that no pop operation will be performed when the MStack is empty
* Attention! To receive points for a test, the number of operations in the output file must be less than or equal to $5 \times$ the number of operations in the input file.

# Example

`mstack.in`
```
6
push
push
push
middle
pop
top
```

`mstack.out`
```
push 1
push 2
push 3
top 2
pop 3
top 2
```

## Explanation

Elements $1, 2,$ and $3$ are inserted into the MStack. The middle operation results in the value $2$, then $3$ is removed, and the subsequent top operation also results in the value $2$.

Internally, the element $1$ is inserted into stack $1$, element $2$ into stack $2$, and element $3$ into stack $3$. To obtain the middle element, we call the top operation on stack $2$. For the pop operation, we call the pop on stack $3$, and for the last top operation, we call the top on stack $2$.