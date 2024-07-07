
An expression is considered, which may contain:

* operands, which are lowercase letters of the English alphabet;
* round brackets;
* the operator `/` symbolizing division;
* the operator `*` symbolizing multiplication.

The rules for evaluating such an expression are those in mathematics.

We aim to rewrite this expression in the form of a product in which factors may appear with positive or negative powers without using round brackets and in which we use the notation $xy$ for $x \cdot y$. 

Thus, $a/b$ is equivalent to $a^1b^{-1}, a*(c/b) \Leftarrow \Rightarrow a^1 c^1 b^{-1}, a/(b*c)*(a*b/c) \Leftarrow \Rightarrow a^2 c^{-2}$

# Task

Given the initial expression, determine the equivalent expression written as a product.

# Input data

The first line of the file `expresie.in` contains a string representing the given expression.

# Output data

Each line of the file `expresie.out` will contain an operand followed by **exactly one space** and an integer representing the power at which this operand appears in the expression written in the equivalent product form. The operands will appear in **alphabetical order**, and positive or zero powers will not be preceded by a sign.

# Constraints and clarifications

* The given expression has at most $20 \ 000$ characters.
* The given expression is correct and does not contain space characters.
* $10 \%$ of the tests will contain only the operator `*`.

# Example 1

`expresie.in`
```
a/b
```

`expresie.out`
```
a 1
b -1
```

# Example 2

`expresie.in`
```
a/(b*c)*(a*b/c)
```

`expresie.out`
```
a 2
b 0
c -2
```

# Example 3

`expresie.in`
```
(p/x)/((b/h/(x/x)))/(p/(b/(x/(h/(p)))))
```

`expresie.out`
```
b 0
h 2
p -1
x -2
```
