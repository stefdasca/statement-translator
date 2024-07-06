~[slang1.png|align=right]

SLang is a version of the Scratch application that provides seven instructions of type $I1$, $I2$, $I3$, $I4$, $I5$, $I6$, $I7$ presented in the adjacent image. A correct program is a sequence of instructions that follows the following rules:

1. It begins with an instruction of type $I1$ and ends with an instruction of type $I7$.
2. Between the instruction of type $I1$ and the instruction of type $I7$, there will be one, two, or more instructions of types $I2$, $I3$, $I4$, $I5$, or $I6$, without using two instructions of the same type; each of these instructions may contain other instructions, according to the specified rules.
3. The body of an instruction of type $I4$ may contain one or two movement instructions (i.e., of type $I2$ or $I3$) and cannot contain instructions of other types.

For example:

~[slang2.png]

4. Each of the two branches of an instruction of type $I5$ (the 'if' branch and the 'else' branch) may contain one or two instructions of type $I2$ or $I3$ and cannot contain instructions of other types.
5. The body of an instruction of type I6 may contain one, two, or more instructions of types $I2$, $I3$, $I4$, $I5$, or $I6$, without using two instructions of the same type; similarly, each of these instructions may contain other instructions, according to the specified rules.

The nesting level of a correct program will be equal to the number of instructions of type $I6$ present in the program.

| Example of a correct program with three instructions of type $I6$ (program with nesting level $3$). | Example of an incorrect program because an instruction of type $I5$ cannot contain an instruction of type $I6$. |
| -- | -- |
| ~[slang3.png] | ~[slang4.png] |

# Task

Given the natural number $K$, representing the nesting level, write a program that solves the following tasks:
1. Determine the number of distinct correct programs with nesting level $K$;
2. Determine the minimum number of instructions and the maximum number of instructions that can exist in a correct program with nesting level $K$.

# Input data

The input file `slang.in` contains the following data:
- The first line contains a natural number $c$ representing the task that needs to be solved ($1$ or $2$).
- The second line contains the natural number $K$, representing the nesting level.

# Output data

If $c=1$, then only task $1$ will be solved, in which case the first line of the output file `slang.out` will contain a natural number representing the last six digits of the number of distinct correct programs with nesting level K.
If $c=2$, then only task $2$ will be solved. In this case, the output file `slang.out` will contain in the first line two natural numbers separated by a space, representing the minimum number of instructions and the maximum number of instructions of a correct program with nesting level $K$.

# Constraints and clarifications

- $0 \leq K \leq 1\ 000$
- Two programs are distinct if in the corresponding sequences of instructions there is at least one position where there are instructions of different types.
- It is guaranteed that, for the test data, the first of the $6$ requested digits is non-zero.
- For a correct solution of each task, $50$ points are awarded.

# Example 1

`slang.in`
```
1
0
```

`slang.out`
```
8674
```

## Explanation

The task is $1$.
There are $8\ 674$ distinct correct programs with nesting level $0$.

# Example 2

`slang.in`
```
2 0
```

`slang.out`
```
3 12
```

## Explanation

The task is $2$.
The minimum number of instructions in a correct program with nesting level $0$ is $3$. An example of such a program is:

~[slang5.png]

The maximum number of instructions in a correct program with nesting level $0$ is $12$. An example of such a program is:

~[slang6.png]