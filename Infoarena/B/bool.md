# Bool

Haralambie received a quite difficult assignment at school. He must evaluate a logical expression. This expression contains variables (uppercase English letters from $A$ to $Z$), constants ($TRUE$ and $FALSE$), round brackets $($ and $)$, and the logical operators $NOT$, $AND$, and $OR$. $NOT$ has the highest priority, $OR$ has the lowest priority. Initially, all variables are set to $FALSE$. Haralambie likes evaluating expressions, but variables sometimes change their values, and the expression needs to be re-evaluated. Alarmed by this, he decided to ask for your help! As mentioned above, a logical expression is defined in one of the following ways:

$$
\begin{align*}
\text{expression} & \quad \text{explanation} \\
TRUE & \\
FALSE & \\
c & \quad c - \text{uppercase letter of the English alphabet} \\
e & \quad e - \text{logical expression} \\
NOT \, e & \quad e - \text{logical expression} \\
e1 \, AND \, e2 & \quad e1 \, and \, e2 - \text{logical expressions} \\
e1 \, OR \, e2 & \quad e1 \, and \, e2 - \text{logical expressions} \\
\end{align*}
$$

## Task

The given expression must be evaluated along with the changes that occur to the values of the variables. For each variable change, re-evaluate the expression and display the result ($1$ for true and $0$ for false).

## Input data

The first line of the input file $bool.in$ contains the logical expression defined as above. The second line contains the number $N$ of variable changes. The third line contains $N$ characters between $A$ and $Z$, representing the variables whose values are modified.

## Output data

The output file $bool.out$ will contain a single line of length $N$. For each variable change, print a character representing the logical value of the expression: $1$ for true and $0$ for false.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq$ Length of the expression $\leq 1\ 000$

All letters that appear in the expression will be uppercase

There won't be more than one space between two characters in the expression

A variable that has the value $TRUE$ changes its value to $FALSE$, and a variable $FALSE$ changes to $TRUE$

## Example

$bool.in$
`
A AND ((B OR NOT C) OR ((TRUE)))
4
ABCA
`

$bool.out$
`
1110
`