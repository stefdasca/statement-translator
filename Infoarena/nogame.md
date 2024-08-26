## Task

Before Sora and Shiro can challenge the god Tet to a duel, they must first conquer all 16 races. Fortunately, Sora has entered a game where he can conquer all 16 races simultaneously. Each of the 16 races has a different binary operation at their disposal. We know that when using binary operations, calculations are performed only between values of $0$ and $1$. A binary operation is defined by the set of values between any 2 elements. Specifically, let's denote the binary operation by $@$ . The binary operation can be applied in 4 cases: between $0$ and $0$ ; between $0$ and $1$ ; between $1$ and $0$ ; and between $1$ and $1$. Depending on the nature of the binary operation, each calculation results in $0$ or $1$. In total, there are $2 * 2 * 2 * 2 = exactly 16$ such operations (the xor, and, and or operations are $3$ well-known operations and are $3$ out of these $16$ operations). Sora has at his disposal $16$ arrays of elements of length $N$. These were formed as follows: Initially, there is an array of length $N$ (let's denote it by $A$). Each of the 16 races applied its operation to the array $A$ as follows: if we denote for a race its binary operation by $@$, the resulting array will be: $A[1]; A[1] @ A[2]; A[1] @ A[2] @ A[3]; \dots ; A[1] @ A[2] @ A[3] @ \dots @ A[i]; \dots ; A[1] @ A[2] @ A[3] @ \dots @ A[N]$. After performing the calculations, each race printed the resulting array. Unfortunately, Sora has only the $16$ resulting arrays, but not the initial array $A$ and does not know for any array what type of operation was applied to it. Given a set of $16$ arrays, Sora's job is to determine the initial array $A$, or to print $-1$ if there is no such array.

## Input data

The input file `nogame.in` will contain on the first line a natural number $T$, the number of tests. Each test set will contain on the first line a natural number $N$ representing the length of the array. The next $16$ lines contain $N$ numbers each, representing the $16$ arrays.

## Output data

The output file `nogame.out` will contain $T$ lines, with the answer for test $i$ on line $i$.

## Constraints and clarifications

$1 \leq T \leq 1000$

$1 \leq N \leq 1000$

All values in the file do not exceed $1\ 000\ 000\ 000$

If there are multiple solutions, print the lexicographically smallest solution

If we have $a @ b$ operations, they are performed up to the most significant bit of the two numbers.

Specifically, if $a = 5(101)$ and $b = 3(11)$, the operation $a @ b$ will be applied only to the last $3$ bits. There are operations where $0 @ 0 = 1$, hence $3 @ 5$ will yield a result in $3$ bits (if more bits were involved, all bits from the $4$th onward would become $1$ because both $3$ and $5$ have the $4$th bit equal to $0$ and $0 @ 0 = 1$).

## Example

nogame.in

`1`

`5` 

`7 7 7 7 7`

`7 0 7 0 8`

`7 4 3 2 10`

`7 8 0 30 1`

`7 0 0 0 0`

`7 12 11 30 23`

`7 11 7 25 14`

`7 8 7 24 7`

`7 3 3 1 0`

`7 15 15 31 31`

`7 4 0 0 0`

`7 3 7 1 8`

`7 15 15 31 31`

`7 7 7 7 15`

`7 12 8 30 23`

`7 11 3 29 10`

`7 12 8 30 23`

nogame.out

`7 7 8 24 23`