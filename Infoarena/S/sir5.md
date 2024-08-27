# Sir5

Although he hoped for a remote-controlled car, Marian received a problem from Santa. Outraged, he wants to send Santa the solution (along with some nice greetings), but for this, he needs your help. A binary string (composed only of the characters $1$ and $0$) is given, and you need to place closed intervals ( $0$ or more) of given length $L$ over this string, with the following properties: any two intervals do not intersect; intervals will be fully included in the string (the ends are not allowed to exceed the boundaries of the string); any interval must contain at least one $1$ inside it; Determine in how many ways these intervals can be placed over the string, modulo $666013$. The string will be given as an array of $M$ elements: $A_1, A_2, \dots, A_M$, with the meaning: the first $A_1$ elements of the string have the value $1$, the next $A_2$ elements have the value $0$, the next $A_3$ are $1$, the next $A_4$ are $0$, and so on.

## Input data

The input file `sir5.in` contains on the first line two natural numbers $M$ and $L$, separated by a space, with the meaning from the statement. The second line contains $M$ natural numbers, separated by a space, numbers which represent the elements of the array $A$.

## Output data

The output file `sir5.out` will contain on the first line a single natural number, which signifies the number of ways in which closed intervals of length $L$ can be placed over the binary string, with the properties from the statement, modulo $666013$.

## Constraints

$2 \leq M \leq 30$

$2 \leq L \leq 30$

$1 \leq A_i \leq 1\ 000\ 000\ 000$

$L \leq A_1 + A_2 + \dots + A_M \leq 1\ 000\ 000\ 000$

Two placements are considered distinct if the number of intervals differ or if there is a position where an interval starts in one placement, but not in the other. It is not mandatory for each element of the string to be covered by an interval. Don't forget that the case where no interval is placed is also valid.

## Example

`sir5.in`

```
4 3
3 2 2 3
```

`sir5.out`

```
19
```

## Explanation

The binary string corresponding to the example is: $1110011000$.

Examples of correctly added intervals:

$111[001][100]0$, $11[100]11000$, $1[110]0[110]00$.

Examples of incorrectly added intervals:

$1110011[000]$ $\rightarrow$ because inside the interval there is no $1$.

$111[00[1]10]00$ $\rightarrow$ because the intervals intersect.