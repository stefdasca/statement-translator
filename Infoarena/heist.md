## Task

After playing MFA (Grand Theft Auto) too much, $Jimmy$ decided it's time to use what he learned, specifically how to rob a bank. After doing the hard part, which involved threatening people in the bank with a toy gun convincingly, $Jimmy$ reached the safe. Now, he asks you to help him open it. The safe has a string of $2 N$ bits inscribed on it.

To unlock it, you need to find an expression using $N$ boolean variables, which can contain (repeatedly):
- these variables
- the $\wedge$ (xor) operator (with low priority)
- the ! (not) operator (with high priority)
- opening and closing parentheses (with very high priority)

If by concatenating the results of the expression for each configuration of 0 and 1 of each variable, in a systematic order (check the example for a detailed explanation), matches exactly the string inscribed on the safe, then $Jimmy$ will become a very wealthy man. Unfortunately, since life is not always easy, it might be that there is no expression that can open the safe, in which case the key to the safe is $-1$.

## Input data

The input file `heist.in` will contain on the first line the number $N$ as specified in the statement. The next line will contain the string of $2^N$ bits.

## Output data

The output file `heist.out` will contain the number $S$ representing the length of the found expression, followed by the expression on the next line.

## Constraints

$1 \leq N \leq 20$

$1 \leq S \leq 500$

If the key to the solution is $-1$, then the value $-1$ will be printed on a single line.

The variables in the expression will be written as $N$ lowercase letters starting in increasing order from the letter $a$. If there are multiple expressions that generate the string of $2^N$ bits, any of them is acceptable. The $\wedge$ operation represents the exclusive disjunction operation performed on the bits of the operands. In Pascal, the corresponding operator is $\text{xor}$, and in C/C++ this operator is $\wedge$. For example, $20 \text{ xor } 14 = 26$. It is not guaranteed that the author of this statement knows how a safe works.

### Subtasks

- Subtask 1 (20 points, tests 1-2): $1 \leq N \leq 5$
- Subtask 2 (20 points, tests 3-4): $6 \leq N \leq 10$
- Subtask 3 (20 points, tests 5-6): $11 \leq N \leq 15$
- Subtask 4 (40 points, tests 7-10): $16 \leq N \leq 20$

## Example

`heist.in`

```
3
01101001
```

`heist.out`

```
9
!(!a^b)^c
```

`heist.in`

```
4
0000000000000000
```

`heist.out`

```
15
a^a^b^b^c^c^d^d
```

## Explanation

In the first example, `!(!a^b)^c` is a correct expression because:

When $a=0$, $b=0$, $c=0$ the expression has the value $0$

When $a=0$, $b=0$, $c=1$ the expression has the value $1$

When $a=0$, $b=1$, $c=0$ the expression has the value $1$

When $a=0$, $b=1$, $c=1$ the expression has the value $0$

When $a=1$, $b=0$, $c=0$ the expression has the value $1$

When $a=1$, $b=0$, $c=1$ the expression has the value $0$

When $a=1$, $b=1$, $c=0$ the expression has the value $0$

When $a=1$, $b=1$, $c=1$ the expression has the value $1$