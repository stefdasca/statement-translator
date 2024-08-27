# Reg

Algostorm has started programming intergalactic satellites in a programming language called SuperP++. A program in SuperP++ consists of a series of instructions (the names of these instructions are integers) that need to be executed in order. To be executed, an instruction must be read from registers (there are $K$ registers, and each register can hold at most one instruction at a time). If an instruction does not exist in the registers, it must be loaded before it can be executed. An instruction can be loaded into an empty register or into a used register, in which case the current instruction in that register is deleted (to free it up). Once deleted, an instruction can no longer be reloaded into any register, and encountering it in the program execution will interrupt the program. 

## Task

Algostorm wrote a program consisting of $N$ instructions. Knowing the number of registers $K$, determine the maximum number of instructions from Algostorm's program that can be executed before it is interrupted, following the loading and reading rules.

## Input data

The file `reg.in` contains on the first line a number $T$ representing the number of test cases that will follow. On the next $T$ lines, there are 5 numbers: $A$, $B$, $C$, $N$, $K$. Algostorm's program will be described by the following relationships ( $X_i$ being the $i$-th instruction, $i = 1 \dots N$ ):
$$X_1 = 1$$ 
$$X_i = (X_{i-1} * A + B * i) \mod C \, \text{for} \, i = 2 \dots N$$ 

## Output data

The output file `reg.out` will contain $T$ lines: for each test case will print on a line the maximum number of instructions from Algostorm's program that can be executed using exactly $K$ registers.

## Constraints and clarifications

$1 \leq N \leq 2\ 000\ 000$

$1 \leq T \leq 10$

$1 \leq A, B, C, K \leq 500\ 000$

$C$ is always prime

The sum of the number of instructions of all programs in an input file will not exceed $4\ 000\ 000$

For 70% of the input files $N \leq 400\ 000$

The instructions will be executed in order, from $1$ to $N$.

## Example

`reg.in`

```
2
1 1 7 5 1
2 3 5 8 2
```

`reg.out`

```
3
6
```