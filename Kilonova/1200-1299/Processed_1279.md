A function call is a string consisting of the name of the called function (an uppercase English alphabet letter), followed by the list of actual parameters of the function, enclosed in round brackets. In the list of actual parameters, there can be $1$, $2$, $\dots$ up to $10$ parameters, separated by commas. An actual parameter can be a constant (an Arabic digit), a variable (a lowercase English alphabet letter), or another function call.

For example: $F(2,a,G(c),G(H(x)))$

The called function is $F$ with $4$ parameters. The first actual parameter is the constant $2$, the second is the variable $a$, the third is the call of the function $G$ (a function with a single parameter – the variable $c$), the fourth is the call of the function $G$ (which has as parameter the call of the function $H$).

The number of parameters of a function is called arity. A function can be called any number of times, but each time the number of specified parameters in the call must equal the function's arity.

Each of the functions involved in the call can be explained with the help of an arithmetic expression in the form:

$F(a,b,c,\dots) =$ arithmetic_expression

The parameters specified in the function explanation are called formal parameters. If the function has the arity $n$, when we explain the function, the formal parameters are named using the first $n$ lowercase letters of the English alphabet in order. In the arithmetic expression that explains the function, only the formal parameters of the function (named as specified with the first $n$ lowercase letters of the English alphabet) appear as variables.

The arithmetic expression explaining a function consists of one or multiple terms separated by the operators `+` (signifying addition) or `-` (signifying subtraction). A term consists of one or multiple factors separated by the operator `*` (signifying multiplication). A factor can be a constant (Arabic digit), a variable (a formal parameter of the function), or an arithmetic expression enclosed in round brackets.

The value obtained from a function call is achieved by **sequentially** replacing the formal parameters with the actual parameters, then performing the specified operations in the arithmetic expression that explains the function.

# Task

Given a function call, the values of the variables involved in this call, as well as the explanations of the functions used in this call, determine the value obtained from this call.

# Input data

The input file `apel.in` contains on the first line the string representing the function call. The following lines contain the values of the variables, one variable per line in the form: $variable_{name} = value$. The subsequent lines explain the functions involved in the call on the first line, in the form described in the statement.

# Output data

The output file `apel.out` will contain a single line that will have a whole number representing the value obtained from the call in the input file.

# Constraints and clarifications

* The arity of a function is less than or equal to $10$.
* Any line in the input file has a maximum of $250$ characters.
* The values of the variables are natural numbers of up to $3$ digits.
* The value obtained from the function call is in the interval $[-2 \cdot 10^9, 2 \cdot 10^9]$.

# Example 1

`apel.in`
```
F(2,a,G(c),G(H(x)))
x=3
a=0
c=1
H(a)=2*a-3
G(a)=2*a*a-5*a+6
F(a,b,c,d)=a*b*c-2*d*c+4*a*c
```

`apel.out`
```
-30
```

## Explanation

The function $F$ has $4$ parameters. The first formal parameter $(a)$ is replaced by the first actual parameter $(thus has the value $2)$.

The second formal parameter $(b)$ is replaced by the second actual parameter, so it has the value of the variable $a$(which is $0)$.

The third formal parameter $(c)$ is replaced by the third actual parameter $(the call $G(c))$ therefore has the value $2 \cdot 1 \cdot 1 - 5 \cdot 1 + 6 = 3$.

The fourth formal parameter $(d)$ receives the value of the fourth actual parameter $(the call $G(H(x)))$ which is $2 \cdot H(x) \cdot H(x) - 5 \cdot H(x) + 6 = 2 \cdot (2 \cdot x - 3) \cdot (2 \cdot x - 3) - 5 \cdot (2 \cdot x - 3) + 6 = 9$.

Therefore, the value of the function call $F$ is: $2 \cdot 0 \cdot 3 - 2 \cdot 9 \cdot 3 + 4 \cdot 2 \cdot 3 = -30$.