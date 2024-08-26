# Valentin

Valentin and Valentina are twins. For their birthday, they received from their parents an array consisting of $n$ integers. Valentin decided to keep only a few elements of the array so that their sum is the maximum possible and, furthermore, so that it is an even number. Being a good brother, he wants to give half of the sum to Valentina. While concentrating on the problem, he wants to get answers to two questions:

1. What is the value of the maximum even sum of a subsequence?
2. How many distinct subsequences exist with the maximum even sum?

## Input data

The input file `valentin.in` contains on the first line a natural number $v$. For all input tests, the number $v$ can only be $1$ or $2$. The second line of the file contains the natural number $n$. The following line contains the $n$ elements of the array, integers separated by spaces.

## Output data

If the value of $v$ is $1$, only the first task will be solved. In this case, the output file `valentin.out` will contain a single integer representing the value of the maximum even sum of a subsequence. If the value of $v$ is $2$, only the second task will be solved. In this case, the output file `valentin.out` will contain a single natural number representing the number of subsequences with the maximum even sum.

## Constraints

$1 \leq n \leq 600\,000$;

$-1\,000\,000\,000 \leq$ elements of the array $\leq 1\,000\,000\,000$;

the maximum sum can also be negative;

a subsequence contains at least one element;

two subsequences are considered distinct if they differ in at least one element position;

for all tests, the results will fit in the `long long` type (C/C++), respectively `int64` (Pascal);

for 50% of the tests, the value of $v = 1$,

for another 50% of the tests, the value of $v = 2$;

for 30% of the tests, the value of $n \leq 21$

for 45% of the tests, the value of $n \leq 1000$

for 60% of the tests, the value of $n \leq 50\,000$

## Example

`valentin.in`
`1`
`4`
`3 -3 0 -3`

`valentin.out`
`0`

## Explanation

$v=1$, the first task is solved, i.e.: the maximum even sum of a subsequence is $0$.

`valentin.in`
`2`
`4`
`3 -3 0 -3`

`valentin.out`
`5`

## Explanation

$v=2$, the second task is solved, i.e.: there are $5$ subsequences with the maximum even sum:

1. $(a_1, a_2) \rightarrow 3-3=0$
2. $(a_1, a_2, a_3) \rightarrow 3-3+0=0$
3. $(a_1, a_3, a_4) \rightarrow 3+0-3=0$
4. $(a_1, a_4) \rightarrow 3-3=0$
5. $(a_3) \rightarrow 0=0$