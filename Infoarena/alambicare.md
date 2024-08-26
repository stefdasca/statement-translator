# Alambicare

Tanaka began using a still to distill some milk. Bored, he finds an extraordinary thing he can do with his still. Specifically, for a sequence of numbers $a_1\ a_2\ \dots\ a_n$, he can divide it into 2 potentially empty parts, $b_1\ \dots\ b_k$ and $c_1\ \dots\ c_{n-k}$, reverse them, turning them into $b_k\ \dots\ b_1$ and $c_{n-k}\ \dots\ c_1$, and then combine them, generating the sequence $b_k\ \dots\ b_1\ c_{n-k}\ \dots\ c_1$. Such an operation is called an alambicare. Now, his cousin Uivlis wants to use the still for esoteric purposes, to sort numbers. Specifically, Uivlis has a sequence of $N$ numbers $v_1\ \dots\ v_N$ on which he will apply $Q$ operations of 2 types:

Operation format

Operation effect

1 st dr x

Add $x$ to $v_{st}$, $\dots$, $v_{dr}$

2 st dr

We ask if Tanaka can sort the subarray $v_{st}$, $\dots$, $v_{dr}$ using his still. If he can, then we also want to know the minimum number of alambicares needed.

Can you help Uivlis? We are sure he will give you 100 points if you succeed :)

## Input data

The input file `alambicare.in` will contain on the first line $N$ and $Q$. The second line will contain the initial values of $v$, in order. The next $Q$ lines will contain Uivlis’ operations, in the format from the table above.

## Output data

The output file `alambicare.out` will contain the answers for all type 2 operations, each on a separate line. The line of a query for which sorting is not possible will contain the number $-1$. The line of a query for which sorting is possible will contain the number of operations used.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 200\,000

1 $\leq$ $Q$ $\leq$ 200\,000

For 10 points, $N$ $\leq$ 20

$Q$ $\leq$ 20

For another 10 points, $N$ $\leq$ 1000

$Q$ $\leq$ 1000

For another 30 points, there are only type 2 operations.

The values of $v$ initially do not exceed, in absolute value, $10^9$.

The values of $x$ do not exceed $10^9$ in absolute value.

Responsible milk consumption is recommended, and the still should only be used by those properly trained.

## Example

`alambicare.in`
```
5 3
1 2 3 4 5
1 3 3 -10
2 2 4
2 1 5
```

`alambicare.out`
```
1
-1
```