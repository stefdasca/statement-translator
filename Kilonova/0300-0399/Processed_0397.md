Let's consider first-degree equations of the form: `expression_1=expression_2`. The specified expressions consist of a succession of operands, between which there is the `+` sign or the `-` sign (with the well-known meaning of addition or subtraction, respectively). Each operand is either a natural number, a natural number followed by the letter `x` (the letter `x` representing the unknown), or just the letter `x` (which is equivalent to `1x`).

For example: `2x-5+10x+4=20-x`. Note that in our equations there are no parentheses and the unknown is always designated by the lowercase letter `x`.

# Task

Write a program that solves first-degree equations, in the format specified in the problem statement.

# Input data

The input file `ecuatii.in` contains a natural number $n$ on the first line, representing the number of equations in the file. Each of the following $n$ lines contains an equation.

# Output data

The output file `ecuatii.out` will contain $n$ lines, one for each equation from the input file. On line $i$, the solution of the equation from line $i+1$ of the input file will be written.

If the solution to the equation is a real number, it will be written with $4$ decimals. The answer is considered correct if the absolute difference between the correct solution and the contestant's solution is $< 0.001$.

If the equation admits an infinite number of solutions, the message `infinit` (in lowercase) will be written.

If the equation does not admit solutions, the message `imposibil` (also in lowercase) will be written.

# Constraints and clarifications
* $1 \leq n \leq 10$;
* The length of an equation does not exceed $255$ characters;
* The equations do not contain spaces;
* The natural numbers appearing in the equations are $\leq 1000$.

# Example

`ecuatii.in`
```
3 
2x-4+5x+300=98x
x+2=2+x
3x+5=3x+2
```

`ecuatii.out`
```
3.2527
infinit
imposibil
```