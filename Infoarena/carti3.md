# Carti3

Gigel is passionate about reading and has many books. He is bored and since he already has some books on his desk arranged in a single stack, he wants to stack the rest on top of the existing ones on his desk. However, as he has plenty of free time, sometimes he takes the stack in hand, book by book from top to bottom, and places it next to the current stack, still in the form of a stack. Thus, the operations he performs are adding a book to the top of the stack or rotating the stack.

## Input data

The input file `carti3.in` contains on the first line 2 numbers $N$ and $C$. $N$ represents the number of operations that will be performed and $C$ represents the initial number of books on the desk. The second line contains $C$ numbers $c_1, \dots, c_c$, where $c_1$ represents the book at the top of the stack, and $c_c$ the book at the bottom. The third line contains $N$ numbers, which are the operations Gigel performs. $-1$ means a rotation of the stack, while a natural number represents the book that is added on top of the stack.

## Output data

The output file `carti3.out` will contain the books on the desk in top-to-bottom order after performing the $N$ operations. Each book is printed on a new line.

## Constraints and clarifications

$$1 \leq C \leq 1\ 000$$

$$1 \leq N \leq 1\ 000\ 000$$

The books are given as natural numbers that can be represented by 32-bit signed integers.

## Example

`carti3.in`

```
4 3
1 2 3
7 -1 3 5
```

`carti3.out`

```
5
3
3
2
1
7
```

## Explanation

The stack after each operation (the leftmost book is the top of the stack):

$$1 \ 2 \ 3 \rightarrow 7 \ 1 \ 2 \ 3 \rightarrow 3 \ 2 \ 1 \ 7 \rightarrow 3 \ 3 \ 2 \ 1 \ 7 \rightarrow 5 \ 3 \ 3 \ 2 \ 1 \ 7$$