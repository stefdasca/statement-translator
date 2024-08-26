Cuantictiori

A geometric progression of length \(n\) with ratio \(q\) is a sequence of natural numbers \(a_1, a_2, \dots, a_n\) for which the relationship \(a_{i+1} = a_i \cdot q\) holds. It can be proven that the number of geometric progressions of length \(n\) with the first value equal to \(k\) is equal to the largest natural number \(d\) with the property that \(d\) is a divisor of \(k\). A quantum progression of length \(n\) with ratio \(q\) is a sequence of natural numbers \(b_1, b_2, \dots, b_n\) for which the relationship \(b_{i+1} = b_i \cdot q + 1\) holds. How many distinct quantum progressions of length \(n\) have the first value between 1 and \(k\)?

## Task

## Input data

The first line of the input file will contain the number \(t\) of queries. The next \(t\) lines will contain 2 values each: \(k\) and \(n\) with the meanings from the statement.

## Output data

The output file will contain \(t\) values on different lines. The value on line number \(i\) will contain the answer to the \(i\)-th query.

## Constraints

$t \leq 10^5$ 

$n \leq k \leq 10^{18}$ 

Subtask worth 10 points: \(q \leq 3\)

Subtask worth 50 points: \(k \leq 10^6\)

Subtask worth 40 points: $\dots$

## Example

`cuantictiori.in`
3
30 2
149808 3
4230675774 3

`cuantictiori.out`
10
24
282

## Explanation

The first 10 quantum progressions of length 2 are: 
4, 8 
8, 16 
8, 32 
9, 27 
16, 32 
16, 64 
16, 128 
25, 125 
27, 81 
27, 243