## Task

Petre Căpraru, a student at "Facultatea de Informatică şi Care Era Cealaltă Chestie?", has become very interested in the studies that his friend, Ştefan Şenilă, is doing in the field of cryptography. Petrică has thus decided to develop a new encryption algorithm, based on which he will do his bachelor's, doctorate, and perhaps even a wedding invitation when the time comes. The algorithm works as follows: Petrică wants to encrypt $N$ distinct prime numbers with values less than or equal to $1\ 000\ 000\ 000$. These are stored in the array $Prim[]$. To encrypt them, he will perform the following steps:
1. He will choose a random permutation of length $N$, call it $P$.
2. He will construct a new array $V$ obtained by the rule: $V[i] = Prim[i] * Prim[P[i]]$, for any $i$ in $[1, N]$.
3. If the elements of $V$ are distinct, the algorithm ends. Otherwise, go back to step 1.

Given the array $V$ after the algorithm has completed, recover the set of prime numbers, thus ruining Petrică's chances of having a decent future.

## Input data

The input file `streetcrypto.in` will contain on its first line the number of tests $T$. This is followed by $T$ tests, each in the following format: the first line will contain the number of values $N$ followed on the second line by $N$ distinct integer values.

## Output data

The output file `streetcrypto.out` will contain $T$ lines, each line containing the solution for the corresponding test, $N$ prime numbers printed in ascending order.

## Constraints

$1 \leq T \leq 100$

$1 \leq N \leq 50$

$1 \leq V[i] \leq 10^{18}$

## Example

`streetcrypto.in`
```
1
3
10 6 15
```

`streetcrypto.out`
```
2 3 5
```