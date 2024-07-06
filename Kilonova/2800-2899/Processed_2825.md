In the glorious year 2051, ChatGPT 42, a master archaeologist, discovered a cookbook, a remnant of human civilization, which had been extinct for almost 26 years.

# Task

The master now wants to recreate a human delicacy: smoked gherkins. He has to follow $N$ steps but is a bit confused: the recipe, like any respectable recipe written in 2024, talks about the author's childhood, then about the ingredients, then a funny story by the author, etc. To recreate the recipe, our little robot needs to sort the steps and asks for your help.

The $N$ steps to follow, represented by numbers from $0$ to $N - 1$, and saved in the array $V$ (elements $V[0], \dots, V[N - 1]$), are in a random order (a permutation) and need to be sorted in ascending order. The little robot can remember 5 numbers in *variables* $A$, $B$, $C$, $D$, and $E$ (initially, all variables have the value $0$). Additionally, the constant variables $Z$ and $N$ contain the value $0$ and $N$, respectively, the number of steps to follow.

The instructions the robot can execute are:
- `IF_LESS_GOTO r1 r2 x` — if the value of the variable `r1` is less than the value of the variable `r2`, then the next operation the robot executes is `x`;
- `IF_DIFF_GOTO r1 r2 x` — if the value of `r1` is different from the value of `r2`, then the next operation the robot executes is `x`;
- `IF_SAME_GOTO r1 r2 x` — if the value of `r1` is equal to the value of `r2`, then the next operation the robot executes is `x`;
- `ASSIGN r1 r2` — saves in `r1` the value of `r2`. The variable `r1` must be **non-constant** (i.e., different from $Z$ and $N$).
- `INC r` and `DEC r` — increases or decreases the value saved in the **non-constant** variable `r`.
- `PLOAD r` — in the **non-constant** variable `r`, the step at position `r` is saved (`r` becomes $V[$`r`$]$). The value of `r` must be between $0$ and $N - 1$.
- `PSWAP r1 r2` — swaps the values in $V[$`r1`$]$ and $V[$`r2`$]$ (i.e., $V[$`r1`$]$ becomes $V[$`r2`$]$ and vice versa). The values of `r1` and `r2` must be between $0$ and $N - 1$ inclusive.
- `END` — ends the program execution.

After executing an operation, the robot executes the next operation, unless the operation specifies otherwise. If it reaches the end of the operations or the `END` operation is executed, the execution stops.

# Input data
The single line from the standard input contains the number $N$, the length of the array $V$.

# Output data
An output program that sorts the array $V$ with the $N$ steps in ascending order. If there are multiple possible solutions, then any of them will be accepted.

**Note:** For the exact format in which the operations must be displayed, see the examples.
# Constraints and clarifications
- $2 \le n \le 100\, 000$
- The generated program cannot perform more than $5 \cdot 10^6$ operations.
- The generated program cannot have more than $1\, 000$ instructions.
- To simplify the testing of the solutions, in the "Attachments" section on the side (or [here](validator.cpp)), you can download a validator for your solution.

|#|Score|Constraints|
-|-|-
|1|10|$N=3$|
|2|15|$N=4$|
|3|15|$N\le 15$|
|4|20|$N\le 100$|
|5|20|$N\le 5\, 000$|
|6|20|No additional constraints|

# Example 1
`stdin`
```
2
```
`stdout`
```
0. INC A
1. PLOAD A
2. PLOAD B
3. IF_LESS_GOTO B A 5
4. END
5. ASSIGN A Z
6. ASSIGN B Z
7. INC B
8. PSWAP A B
```
# Example 2
`stdin`
```
2
```
`stdout`
```
0. ASSIGN A N
1. DEC A
2. ASSIGN B Z
3. ASSIGN C A
4. ASSIGN D B
5. PLOAD C
6. PLOAD D
7. IF_DIFF_GOTO N Z 9
8. END
9. IF_LESS_GOTO C D 11
10. END
11. PSWAP A B
```
## Explanation
Assuming the value of the permutation is $V = \\{1,0\\}$. The operations performed by the robot are as follows:
1. The executed line is $0$. `ASSIGN A N`.
- $V = \\{ 1, 0 \\}$
- $A = 2$, $B = 0$, $C = 0$, $D = 0$, $E = 0$
2. The executed line is $1$. `DEC A`.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 0$, $D = 0$, $E = 0$
3. The executed line is $3$. `ASSIGN C A`.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 1$, $D = 0$, $E = 0$
4. The executed line is $4$. `ASSIGN D B`.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 1$, $D = 0$, $E = 0$
5. The executed line is $5$. `PLOAD C`.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 0$, $D = 0$, $E = 0$
6. The executed line is $6$. `PLOAD D`.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 0$, $D = 1$, $E = 0$
7. The executed line is $7$. `IF_DIFF_GOTO N Z 9`.
- $N$ is different from $Z$ ($2 \neq 0$), so we jump to instruction $9$.
- $V = \\{ 1, 0 \\}$
- $A = 1$, $B = 0$, $C = 0$, $D = 1$, $E = 0$
8. The executed line is $9$. `IF_LESS_GOTO C D 11`.
- $C$ is less than $D$, so we jump to instruction $11$. $V = \\{ 1, 0 \\}$.
- $A = 1$, $B = 0$, $C = 0$, $D = 1$, $E = 0$
9. The executed line is $11$. `PSWAP A B`.
- $V = \\{ 0, 1 \\}$
- $A = 1$, $B = 0$, $C = 0$, $D = 1$, $E = 0$
10. The program execution stops, and the array $V = \\{0, 1\\}$ is sorted.
# Example 3
`stdin`
```
2
```
`stdout`
```
0. INC B
1. PLOAD A
2. PLOAD B
3. IF_LESS_GOTO A B 6
4. INC D
5. PSWAP C D
6. END
```
