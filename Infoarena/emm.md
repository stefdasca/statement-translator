## Min-max Expressions

Consider an expression that contains natural numbers, parentheses, and the binary operators $m$ and $M$. $m$ is the minimum operator and $M$ is the maximum operator. Thus, the result of the operation $A m B$ is the minimum value between $A$ and $B$, while the result of the operation $A M B$ is the maximum value between $A$ and $B$. For example, the result of $2m7$ is $2$, and the result of $9M8$ is $9$. The two operators have the same priority. This means that if there are no parentheses, they will be evaluated left to right. For example, the result of $1M22m13m789$ is $13$.

## Task

Given an expression that contains natural numbers, parentheses, and these two operators, find the result obtained.

## Input data

The first line of the file `emm.in` contains the given expression. There will be no spaces, and the line ends with an end-of-line character (which is not part of it).

## Output data

Print on the first line of the file `emm.out` the result obtained after evaluating the expression.

## Constraints and clarifications

The length of an expression will be less than or equal to $100\ 000$

The numbers that appear in the expression will be natural numbers between $0$ and $1\ 000\ 000\ 000$

## Examples

`emm.in` `emm.out`

`178` `178`

`178m66m234M89m54M13M22m67` `54`

`(((178)))` `178`

`(1m1m1M1M1m1M1M1m1M0)m1M1` `1`

`(12m23M13m192)M(90m89m88m87)m((298M7)M2)` `87`