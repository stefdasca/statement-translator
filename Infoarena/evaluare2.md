# Evaluation 2

Evaluate an arithmetic expression. It can contain: operands which are natural numbers, operators such as $+$ (binary operator, addition), $/$ (binary operator, division), $^$ (binary operator, exponentiation), $!$ (unary operator, reverses the value of the operand, e.g., $! 560$ gives $65$). Any two operators have different priorities (in increasing order, as given above, hence $+$ has the lowest priority). The operators $+$ and $/$ are applied from left to right. The operator $^$ is applied from right to left. The operator $!$, as any unary operator, is applied from right to left. Additionally, round brackets may appear to change the priority of the operators. For example, the expression: $5+( !! 10 + 3 ^ 2 ^ 3)/2$ has the value $3286$. It is obtained as follows: $5 + (1 + 3 ^ 8)/2 = 5+6562/2 = 5+3281 = 3286$.

## Input data

The file `evaluare2.in` contains on the first line the expression to be evaluated. 

## Output data

The file `evaluare2.out` contains on the first line the value of the evaluated expression. 

## Constraints

- The given string has a maximum of $100$ characters.
- The numbers that initially appear in the expression are natural numbers with a maximum of $3$ digits.
- The value to be printed fits within the $long long$ type.
- For $10 \%$ of the points, there are no parentheses, and only the $+$ operator is present.
- For another $10 \%$ of the points, there are no parentheses, and only the $+$ and $/$ operators are present.
- For another $40 \%$ of the points, only the $+$ and $/$ operators appear, and parentheses may also appear.
- For another $10 \%$ of the points, parentheses and the operators $+$, $/$, and $!$ appear.
- For another $10 \%$ of the points, parentheses and the operators $+$, $/$, and $^$ appear.
- The given expression is correct and does not contain other characters.
- It is guaranteed that correct execution of the operations does not result in division by $0$.
- None of the partial results obtained by performing the operations in order of priority exceed the $long long$ type's maximum value.

## Example

`evaluare2.in`
```plaintext
5+( !! 10+3 ^ 2 ^ 3)/2
```

`evaluare2.out`
```plaintext
3286
```