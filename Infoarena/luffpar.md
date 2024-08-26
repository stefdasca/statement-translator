Luffpar

Bluff recently discovered a sequence of round brackets in the grey machine. For unknown reasons, he wants to perform the following operations based on the new discovery: 
operation of type $1$: given $l$ and $r$, two valid positions of the sequence, modify all brackets between $l$ and $r$ inclusive – thus, the brackets ‘$(‘$ become ‘$)$’ and ‘$)$’ become ‘$(‘$
operation of type $2$: given $l$ and $r$, two valid positions of the sequence, determine if the subarray of brackets between $l$ and $r$ represents a correct parenthesis. Formally, a correct parenthesis is constructed according to the following rules:
$<$correct parenthesis$>$ $=$ $<$empty sequence$>$
$<$correct parenthesis$>$ $=$ “$(“$ $+$ $<$correct parenthesis$>$ $+$ “$)$”
$<$correct parenthesis$>$ $=$ $<$correct parenthesis$>$ $+$ $<$correct parenthesis$>$

The following are examples of correct parenthesis sequences: $()$, $(()())$, $(()())()$, $(()())(()())$
The following are examples of incorrect parenthesis sequences: $))$, $)($, $(()))$, $())($, $(()()))($
Given the initial bracket sequence, as well as the operations that Bluff wants to perform, help him respond to the type $2$ operations.

## Input data

The first line of the file `luffpar.in` will contain the number $n$, representing the length of the bracket sequence. The second line will contain exactly $n$ characters, representing the bracket sequence. The characters will be only round brackets: $( $ or $)$. The third line will contain the number $m$ representing the number of operations Bluff wants to perform. The next $m$ lines will contain three integers each: $type$ $l$ $r$, which describe each operation that needs to be applied. $type$ can be $1$ or $2$, identifying the type of operation that needs to be applied. $l$ and $r$ describe the subarray on which the operation needs to be applied, and the positions of the sequence are numbered from $1$.
It is guaranteed that, for any operation,
$1 \leq l \leq r \leq n$.

## Output data

In the file `luffpar.out` print the responses corresponding to type $2$ operations. A response can be $1$ for a correctly parenthesized sequence, or $0$ otherwise.

## Constraints

$1 \leq n \leq 200\ 000$
$1 \leq m \leq 200\ 000$

for $20\%$ of the tests:
$n, m \leq 1000$

for another $30\%$ of the tests, it is guaranteed that each type $1$ operation will be applied on a subarray of length exactly $1$, so $l = r$ will be true for all type $1$ operations.

## Example

`luffpar.in`
``` 
5
()(()
5
2 1 2
1 4 5
2 3 4
2 1 4
2 4 5
```
`luffpar.out`
``` 
1
0
1
1
0
```

## Explanation

The subarray corresponding to the first operation is $()$, which is a correct parenthesis, so $1$ is printed. After the second operation, the sequence becomes: $()()($
The subarray corresponding to the next operation is now $()$, which is a correct parenthesis.
The subarray corresponding to the next operation is now $()()$, which is a correct parenthesis.
The subarray corresponding to the next operation is $)($, which is not a correct parenthesis, so $0$ is printed.