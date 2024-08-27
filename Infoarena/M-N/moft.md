## Task

Marcel is now in a very abstract universe. Numbers acquire feelings, and their whims become oversized. Thus, there are $S$ whimsical numbers, denoted $K_i$, and a multiset of initially empty numbers. It is worth mentioning that in a multiset a number can appear multiple times. The multiset undergoes $N$ operations:

$1 \ x$: number $x$ is inserted into the multiset. It is associated with an $id$ number equal to the smallest positive natural number that has not been associated with any other number before.

$2 \ id$: the number associated with $id$ is removed from the multiset. It is guaranteed that this number is in the multiset.

After each of these $N$ operations, each of the $S$ whimsical numbers asks what would be the number at position $K_i$ if we arranged the numbers in the multiset in ascending order.

Technical Details

To avoid overloading the output file with all the whims of the numbers and to ensure that only the most outstanding solutions will be scored accordingly, after each operation the number $P$ is calculated as the product of the answers to the $S$ questions, modulo $1.000.000.007$. If the question is invalid, i.e., $K_i >$ number of elements in the multiset, $P$ does not change (simulated as multiplication with the neutral element, which is $1$). Depending on it, the number to be inserted or removed is determined as follows:

If the input number is $H$, the value used is given by $H \ xor (P * t)$, where $t$ is a known value, either $0$ or $1$.

For the first operation, $P = 1$ is considered. The value of $P$ should not be printed, but used to calculate the final answer, which will be printed in the output, which is equal to $(P_1 * 0) \ xor (P_2 * 1) \ xor \dots \ xor (P_N * (N - 1))$, where $P_i$ denotes the value of $P$ after the first $i$ operations. Note that the value to be printed is not calculated modulo $1.000.000.007$!

## Input Data

The input file `moft.in` contains on the first line the number $t$, whose usefulness has been highlighted above, and the number $T$ of tests. The structure of each test is as follows:

The first line contains the number $S$,

the second line contains the $S$ numbers $K_i$,

the third line contains the number $N$ of operations,

and the following $N$ lines contain a pair $u \ H$, where $u$ is either $1$ or $2$, depending on the type of operation, and $H$ should be modified as explained above.

## Output Data

The output file `moft.out` contains, for each of the $T$ tests, one number, representing the final answer which is calculated as described.

## Constraints and Clarifications

$1 \leq H, K_i \leq 1.000.000.000$

$1 \leq T \leq 3$

$1 \leq N, S$

Scoring

In the evaluation, $20$ tests will be used, each worth $5$ points. They are organized as follows:

$1$ test: $t = 0$, $N \leq 1.000$, $S \leq 1.000$, no operations of type $2$

$1$ test: $t = 0$, $N \leq 1.000$, $S \leq 1.000$

$1$ test: $t = 0$, $N \leq 10.000$, $S \leq 300$

$1$ test: $t = 1$, $N \leq 10.000$, $S \leq 300$, no operations of type $2$

$1$ test: $t = 1$, $N \leq 10.000$, $S \leq 300$

$1$ test: $t = 0$, $N \leq 50.000$, $S \leq 20$, no operations of type $2$

$2$ tests: $t = 0$, $N \leq 50.000$, $S \leq 20$

$2$ tests: $t = 1$, $N \leq 50.000$, $S \leq 20$, no operations of type $2$

$3$ tests: $t = 1$, $N \leq 50.000$, $S \leq 20$

$1$ test: $t = 0$, $N \leq 200.000$, $S = 1$, no operations of type $2$

$1$ test: $t = 0$, $N \leq 200.000$, $S = 1$

$1$ test: $t = 1$, $N \leq 200.000$, $S = 1$, no operations of type $2$

$4$ tests: $t = 1$, $N \leq 200.000$, $S = 1$

## Example

`moft.in`

```
0 
3 
10 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
20 
1 
7 
1 
4 
1 
9 
1 
2 
1 
6 
1 
1 
1 
5 
1 
10 
1 
3 
1 
8 
2 
1 
2 
2 
2 
3 
2 
4 
2 
5 
2 
6 
2 
7 
2 
8 
2 
9 
2 
10 
1 
3 
20 
1 
7 
1 
4 
1 
9 
1 
2 
1 
6 
1 
1 
1 
5 
1 
10 
1 
3 
1 
8 
2 
1 
2 
2 
2 
3 
2 
4 
2 
5 
2 
6 
2 
7 
2 
8 
2 
9 
2 
10 
10 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
20 
1 
8 
1 
3 
1 
10 
1 
5 
1 
1 
1 
6 
1 
2 
1 
9 
1 
4 
1 
7 
2 
1 
2 
2 
2 
3 
2 
4 
2 
5 
2 
6 
2 
7 
2 
8 
2 
9 
2 
10 
```

`moft.out`

```
26034647 
217 
27243809 
```

## Explanation

```
7 
P=7 
4 7 
P=28 
4 7 9 
P=252 
2 4 7 9 
P=504 
2 4 6 7 9 
P=3024 
1 2 4 6 7 9 
P=3024 
1 2 4 5 6 7 9 
P=15120 
1 2 4 5 6 7 9 10 
P=151200 
1 2 3 4 5 6 7 9 10 
P=453600 
1 2 3 4 5 6 7 8 9 10 
P=3628800 
1 2 3 4 5 6 8 9 10 
P=518400 
1 2 3 5 6 8 9 10 
P=129600 
1 2 3 5 6 8 10 
P=14400 
1 3 5 6 8 10 
P=7200 
1 3 5 8 10 
P=1200 
3 5 8 10 
P=1200 
3 8 10 
P=240 
3 8 
P=24 
8 
P=8 
P=1 
------------------ 
P=1 
P=1 
9 
P=9 
7 
P=7 
6 
P=6 
4 
P=4 
4 
P=4 
4 
P=4 
3 
P=3 
3 
P=3 
3 
P=3 
3 
P=3 
3 
P=3 
5 
P=5 
5 
P=5 
8 
P=8 
10 
P=10 
P=1 
P=1 
P=1 
------------------ 
8 
P=8 
3 8 
P=24 
3 8 10 
P=240 
3 5 8 10 
P=1200 
1 3 5 8 10 
P=1200 
1 3 5 6 8 10 
P=7200 
1 2 3 5 6 8 10 
P=14400 
1 2 3 5 6 8 9 10 
P=129600 
1 2 3 4 5 6 8 9 10 
P=518400 
1 2 3 4 5 6 7 8 9 10 
P=3628800 
1 2 3 4 5 6 7 9 10 
P=453600 
1 2 4 5 6 7 9 10 
P=151200 
1 2 4 5 6 7 9 
P=15120 
1 2 4 6 7 9 
P=3024 
2 4 6 7 9 
P=3024 
2 4 7 9 
P=504 
4 7 9 
P=252 
4 7 
P=28 
7 
P=7 
P=1 
```