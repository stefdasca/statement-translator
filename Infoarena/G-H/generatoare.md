## Task

We have $n$ number generators denoted by $G_1, G_2, \dots, G_n$. Generator $G_i$ randomly generates a natural number $a_i$ between $0$ and $m_i - 1$, each number having the same probability of being generated. We denote $vxor$ as the value $a_1 \: xor \: a_2 \: xor \dots \: xor \: a_n$. Determine the “expected value” for $vxor$ knowing that it is equal to the sum, where $Val$ is the set of values that can be obtained for $vxor$ and $p(v)$ is the probability that the value obtained for $vxor$ is $v$. Write a program that determines the “expected value” for $vxor$.

## Input data

The first line of the input file `generatoare.in` contains the natural number $n$ representing the number of generators. The next $n$ lines contain the numbers $m_1, m_2, \dots, m_n$, one on each line. More specifically, the value $m_i$ is on line $i+1$.

## Output data

The output file `generatoare.out` will contain a single line that contains the “expected value” for $vxor$ with exactly 3 decimals rounded.

## Constraints and clarifications

$1 \leq n \leq 50000$

$2 \leq m_i \leq 2^{30}$

For two natural numbers $a$ and $b$, we define $a \: xor \: b$ as the value obtained by applying the “exclusive or” operator on the binary representations of $a$ and $b$.

## Example

`generatoare.in`

`2`

`3`

`5`

`generatoare.out`

`2.200`

## Explanation

We have two generators. The first can generate the numbers $0, 1, 2$ and the second can generate the numbers $0, 1, 2, 3, 4$. So the pair $(a_1, a_2)$ can have the following values:

`(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)`.

This results in the following 15 values for $vxor$:

`0, 1, 2, 3, 4, 1, 0, 3, 2, 5, 2, 3, 0, 1, 6`.

We observe that the distinct possible values for $vxor$ are `0, 1, 2, 3, 4, 5 and 6`.

Thus, the values $0, 1, 2$ and $3$ each have a probability of $\frac{3}{15}$ and $4, 5$ and $6$ each have a probability of $\frac{1}{15}$.

Therefore, the “expected value” for $vxor$ is:

$(0 + 1 + 2 + 3) * (\frac{3}{15}) + (4 + 5 + 6) * (\frac{1}{15}) = 2.200$.