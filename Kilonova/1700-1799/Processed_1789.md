Let's consider a stack, initially empty. We can perform the following operations:
- $push(X)$ - introduce the letter $X$ into the stack (obviously, at the top of the stack);
- $pop$ - extract the letter located at the top of the stack (the pop operation is executed when the stack is not empty);
- $top$ - display the letter located at the top of the stack (the top operation is executed when the stack is not empty).

A sequence of operations is considered correct if:
- initially, the stack is empty;
- a series of $push$, $pop$, $top$ operations are executed, without performing pop or top when the stack is empty;
- at the end, the stack is empty.

Using correct sequences of operations, we can display different character strings. For example, the string `ABCACBA` can be generated as follows: $push(A)$, $top$, $pop$, $push(B)$, $top$, $pop$, $push(C)$, $top$, $pop$, etc.

Another correct but shorter sequence of operations would be: $push(A)$, $top$, $push(B)$, $top$, $push(C)$, $top$, $push(A)$, $top$, $pop$, $top$, $pop$, $top$, $pop$, $top$, $pop$.

# Task

Given a string formed from uppercase letters, determine the minimum number of operations in a correct sequence that displays the given string.

# Input data

The input file `stiva.in` contains a single line which contains a string consisting only of uppercase letters.

# Output data

The output file `stiva.out` will contain a single line which contains the minimum number of operations in a correct sequence that displays the string from the input file.

# Constraints and clarifications

* The length of the string is $\leq 500$.

# Example 1

`stiva.in`
```
ABCACBA
```

`stiva.out`
```
15
```

