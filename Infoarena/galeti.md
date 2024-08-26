Buckets

Dorel has $N$ buckets numbered from $1$ to $N$. Bucket $i$ has a capacity $C_i$ (the capacities are natural numbers). An overflow order is a permutation $P$ of length $N$ with the following meaning: if bucket $P_i$ is filled, the excess pours into bucket $P_{i+1}$. The excess from bucket $P_N$ does not pour into any bucket. Initially, Dorel's buckets have the overflow order $Q$. For this, he wants to determine the minimum amount of water $X_Q$ to pour sequentially into the buckets (he pours water into buckets in the order $1, 2, \dots N$) so that in the end the buckets are full of water. Then, Dorel wants to find an overflow order $R$, for which the amount of water $X_R$ poured sequentially into the buckets (in the order $1, 2, \dots N$) is minimal.

## Task

Help Dorel solve the problem described above.

## Input data

The first line of the file `galeti.in` will contain the number $N$ as described above.
The 2nd line contains $N$ numbers $Q_1, Q_2, \dots Q_N$ separated by a space which describe the initial overflow order $Q$.
The 3rd line contains $N$ numbers $C_1, C_2, \dots C_N$ separated by a space which describe the capacities of the buckets.

## Output data

In the file `galeti.out`, print on the first line the amount of water $X_Q$ as described above.
The second line will contain $N$ numbers $R_1, R_2, \dots R_N$ which describe the overflow order $R$ for which $X_R$ is minimal.
On the third line, print $X_R$ as described above.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$1 \leq C_i \leq 10^9$ for any $i$ from $1$ to $N$

for 30% of the points:
$1 \leq N \leq 600$

$1 \leq C_i \leq 10000$ for any $i$ from $1$ to $N$

for 50% of the points:
$1 \leq N \leq 1000$

Both $X_Q$ and $X_R$ must be natural numbers.

Any overflow order $R$ for which $X_R$ is minimal is acceptable.

## Example

`galeti.in`

```
4
1 2 3 4
4 2 3 2
```

`galeti.out`

```
4
2 3 4 1
3
```

## Explanation

With the initial overflow order, the minimum requested value is 4, and the quantities in the buckets after each pouring are as follows:
```
4 0 0 0
4 2 2 0
4 2 3 2
4 2 3 2
```

With the new overflow order, the minimum requested value is 3, and the quantities in the buckets after each pouring are as follows:
```
3 0 0 0
3 2 1 0
3 2 3 1
4 2 3 2
```
There is no access order by which the buckets can be filled by pouring less than 3 liters sequentially.