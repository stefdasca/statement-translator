Bazaconii

Andrew and Maria are two kids who are always up to some mischief. Their latest mischief was losing a sheet of paper on which a sequence of $N$ natural numbers was written. They don't remember the numbers anymore, but they remember $M$ relations of the form $i$ $j$ $k$ meaning that the $\text{xor}$ sum of the numbers at positions $i$ and $j$ in the sequence is $k$. The children tried to reconstruct the original sequence based on these relations but failed, so they are asking for your help. They also wish that if there are multiple sequences of numbers that satisfy all the relations, they know only the smallest sequence in lexicographical order.

## Input data

The input file `bazaconii.in` contains on the first line the number $T$, representing the number of tests to be described. This is followed by $T$ tests, with the first line of each test containing $N$ and $M$, separated by a single space, having the meaning from the statement. Next, there are $M$ lines, each containing three natural numbers separated by a single space, $i$, $j$, and $k$, having the meaning from the statement.

## Output data

The output file `bazaconii.out` will contain $T$ lines, with line $i$ containing the answer for the $i$-th test from the input file. If there is no sequence that meets the conditions, it will print only the number $-1$, otherwise it will print $N$ natural numbers separated by a single space, representing the smallest lexicographical sequence that meets all the conditions.

## Constraints and clarifications

For $20\%$ of the tests $N \leq 7$ and it is guaranteed that the optimal solution will have all values less than or equal to $20$

$1 \leq T \leq 10$

$1 \leq N, M \leq 10\,000$

For each triplet $i$ $j$ $k$, $1 \leq i, j \leq N$ and $0 \leq k \leq 2\,000\,000\,000$

To obtain the $\text{xor}$ sum of two natural numbers, the numbers are written in binary representation, and each bit of the result will be $1$ only if the corresponding bits of the two numbers are different; otherwise, it will be $0$.

## Example:

$0 \text{ xor } 1 = 1$, $1 \text{ xor } 0 = 1$, $1001 \text{ xor } 1100 = 0101$. In C/C++ there is the operator " $\hat{ }$ " which performs this operation, and in pascal there is the " $\text{xor} $" operator. A sequence $X$ is smaller in lexicographical order than a sequence $Y$ if there exists a $k$ such that $X_i = Y_i$ for any $i < k$ and $X_k < Y_k$.

## Example

`bazaconii.in`
2
2 2
1 2 3
1 2 1
2 1
1 2 1

`bazaconii.out`
0 1
-1

## Explanation

For the second test, a possible solution was $1 \, 0$, but the sequence $0 \, 1$ is the smallest in lexicographical order.