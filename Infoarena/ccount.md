## Task

Consider the following sequence: $A(1) = 1$. $A(2) = 1$. $A(i) = x * A(i - 1) + y * A(i - 2)$, for any $i$ greater than or equal to $3$. A list of positions $P_1, P_2 \dots P_k$ is given, indicating that the values $A(P_1), A(P_2), \dots A(P_k)$ are known. It is considered that the values $A(1)$ and $A(2)$ are also known, even if the numbers $1$ and $2$ might not be included in the list $P$. The computation procedure for a certain term of the sequence, let's call it $A(n)$, is as follows:
```
int F(int n) {
    if $A(n)$ is known then return the value of $A(n)$;
    calcule_totale++;
    return the value F(n - 1) + F(n - 2);
}
```
What will be the value of the global variable $calcule_totale$ after calling $F(n)$?

Since this number can be very large, the result will be displayed mod $9007$.

## Input data

The input file `ccount.in` will contain on its first line the number $N$ and the number $K$, representing the index of the term for which we are providing the answer, and respectively the number of elements in the list $P$. The second line will contain $K$ numbers, representing the list $P$.

## Output data

The output file `ccount.out` will contain the answer to the problem mod $9007$.

## Constraints

$1 \leq N \leq 10^5$

$A$ mod $B$ refers to the remainder of the division of number $A$ by number $B$.

After calling the function $F(n)$, the value $A(n)$ does not become known further on. Thus, $F(n)$ will be called as many times as necessary for a certain value of $n$.

The following relationships are valid and may be necessary to compute the result without exceeding C++ data types:
$(A + B)$ mod $C = (A$ mod $C + B$ mod $C)$ mod $C$
$(A * B)$ mod $C = ((A$ mod $C) * (B$ mod $C))$ mod $C

## Example

`ccount.in`
```
6 1
5
```

`ccount.out`
```
3
```

## Explanation

The variable $calcule_totale$ is incremented in the calls $F(6)$, $F(4)$, $F(3)$. Observe that if $A(5)$ were not known, the answer would have been $7$.