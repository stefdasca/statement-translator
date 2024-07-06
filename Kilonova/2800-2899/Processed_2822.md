```markdown
~[poza.png|align=right|width=15em]
Chef Alexandru received an order for the house specialty: a generous portion of garlic sauce cake.

For the cake, he needs exactly $X$ liters of garlic sauce. Chef Alexandru has at his disposal two bowls $A$ and $B$, each with a capacity of $C_A$ and $C_B$ liters, respectively, both initially empty.

Chef Alexandru can perform the following operations:
- `FILL [A/B]` — completely fill bowl $A$ or $B$ with $C_A$ or $C_B$ liters of garlic sauce, respectively;
- `EMPTY [A/B]` — completely empty bowl $A$ or $B$;
- `POUR [A/B] INTO [B/A]` — pour as much garlic sauce as possible from bowl $A$ (or $B$) into bowl $B$ (or $A$). If the source bowl has $x$ liters of garlic sauce and the destination bowl has $y$ free liters, Chef Alexandru will pour exactly $\min(x, y)$ liters.

# Task
Chef Alexandru needs your help: find a sequence of at most $10^6$ operations that will result in exactly $X$ liters of garlic sauce in one of the two bowls.

**Note:** Any valid solution is accepted, you do not need to minimize its length!

# Input data
The single line in the standard input contains three natural numbers $C_A$, $C_B$, and $X$ separated by a space, as described in the statement.

# Output data
If there is no solution, then the single line in the standard output must contain `IMPOSSIBLE`.

If there is a solution, then print the number of required operations on the first line of the standard output, and on the subsequent lines, in order, print the performed operations.

# Constraints and clarifications
- $1 \le X < C_A, C_B \le 100\ 000$

|#|Points|Constraints
-|-|-
|1|20|$X = 1$, $C_A = 2$ and $C_B \le 10$|
|2|20|$1 \le C_A, C_B \le 10$|
|3|30|$1 \le C_A, C_B \le 1\ 000$|
|4|30|No additional constraints|

# Example 1
`stdin`
```
3 2 1
```
`stdout`
```
2
FILL A
POUR A INTO B
```
# Example 2
`stdin`
```
1110 10101 110
```
`stdout`
```
IMPOSSIBLE
```
# Example 3
`stdin`
```
10 6 4
```
`stdout`
```
6
FILL B
POUR B INTO A
FILL A
FILL B
EMPTY B
POUR A INTO B
```
```