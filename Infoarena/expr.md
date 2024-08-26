Expr

Acarie, an excellent student, has problems with his homework for the algebraic structures seminar. He reduced the problem to a simple one, involving operations with sets. However, there are too many operations and it's already time to go out. Help him get out of this predicament. 

## Task

Write a program that finds the result of a given valid expression.

## Input data

In the file `expr.in`, a string of characters without spaces is given. This string of characters can contain the following elements:
- operands - these are sets, described by a brace ( $\{$ ) followed by the numbers that are part of that set (in increasing order) separated by commas ( , ) and ending with another brace ( $\}$ )
- operators - which can be parentheses, or one of the following operations (which have the same priority):
  - $* \text{ - intersection}$
  - $+ \text{ - union}$
  - $- \text{ - difference}$
  - $\% \text{ - symmetric difference: } A \% B = (A-B)+(B-A) = (A+B)-(A*B)$ 

## Output data

Write the result of the expression in the file `expr.out` as a single set (following the format of the sets in the input).

## Constraints and clarifications

- The length of the string $\leq 100\ 000$
- The number of distinct values that appear in the entire expression $\leq 8\ 000$
- $0 \leq \text{values that appear in sets} \leq 2\ 000\ 000\ 000$ (integers)
- Maximum depth of parentheses $\leq 100$
- Maximum number of operations $\leq 10\ 000$
- The empty set is represented by ${\{} \}$
- The numbers in the resulting set will be displayed in increasing order

## Example

`expr.in`
```
{1,2,3,4}%({1,2,3,4}*{}+{1,2}+{5,6}-{1})
```

`expr.out`
```
{1,3,4,5,6}
```