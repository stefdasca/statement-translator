Fingerprint

For any natural number $N$, a digit from the set $\{0, 1, 2, 3, 4, 5\}$, called fingerprint, is associated as follows: the positive difference between the sums of the digits at even and odd positions is calculated; if this difference is less than $10$, then the algorithm stops. Otherwise, the algorithm continues repeatedly applying it to the positive difference, until a digit less than $10$ is obtained, and if the digit is greater than $5$, then the digits $6, 7, 8, 9$ are replaced respectively with $5, 4, 3, 2$. For example, for the number $N = 90$ the fingerprint is $2$, and for $N = 91909091$ the fingerprint is $1$.

## Task
1) A natural number $N$ is given and you are tasked with determining its fingerprint.
2) Two natural numbers $P, Q$ and a digit $C$ from $\{0, 1, 2, 3, 4, 5\}$ are given, and you are tasked with determining the number of values between $P$ and $Q$, inclusive, that have a fingerprint equal to $C$.

## Input data

The input file `amprenta.in` contains on the first line the number $T$ representing the type of task. If $T == 1$, then the second line contains a natural number $N$. If $T == 2$, then the second line contains the natural numbers $P, Q$ and $C$, separated by spaces.

## Output data

The output file `amprenta.out` will contain on the first line a single natural number, corresponding to the task and the case $T$.

## Constraints

$0 \leq N \leq 10^{18}$

$0 \leq P \leq 10^{18}$

$0 \leq Q \leq 10^{18}$

For $30 \%$ of the tests, the positive difference between $P$ and $Q$ will be less than $10^{4}$

For another $20 \%$ of the tests, the positive difference between $P$ and $Q$ will be less than $10^{5}$

## Example

`amprenta.in`
```
1
29
```
`amprenta.out`
```
4
```
## Explanation

The positive difference is $7$, and the fingerprint will be $4$.

## Example

`amprenta.in`
```
2
1 9 2
```
`amprenta.out`
```
2
```

## Explanation

The numbers with a fingerprint equal to $2$ are $2$ and $9$.