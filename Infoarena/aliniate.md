## Task

In system architecture, the concept of "alignment" of data types is relevant; more precisely, a primitive data type must be positioned at an address that is a multiple of its length (for example, a $4$ $byte$ $integer$ must be at a position that is a multiple of $4$). This is quite useful in some implementations (for example, a node in a $std::set$ must be at a position that is a multiple of $8$; thus, the $pointers$ in that node to other $children$ always have $0$ in the last $3$ $bits$, and the $stl$ implementation of this container uses those bits to store information). This problem uses this concept. The boss of the company $AlignedGas$ sees value only in aligned things. He considers that a subarray $[x, y]$, of length which is a power of $2$, is aligned if and only if $y - x + 1$ divides $x$. He has in front of him an array of $10^9$ integer values, indexed from $0$. He chooses at most $100,000$ aligned subarrays, and calculates the product of the values in those subarrays, modulo $2^{32}$, noting these values. Unfortunately, his adversary $Hideyoshi$, the head of the $Oil \text{ and } Gas$ University of metropolis $B$, stole the sequence and modified some of the noted products. The boss now wonders: "Boss, is there a way to choose the $10^9$ values so that the products match the noted ones?"

## Input data

The input file $aligned.in$ contains, on the first line, the number $T$ of tests in the given file. The $T$ tests follow. A test will have, on the first line, the number $N$ of noted products. On the next $N$ lines, there will be one triplet $x$ $y$ $z$, which signifies: "the product of the values from $x$ to $y$, modulo $2^{32}$, is $z$".

## Output data

The output file $aligned.out$ will contain $T$ lines, each containing the result for each test, in order. For each test, if there exists an array of $10^9$ values that satisfies the given constraints, print $1$; otherwise, print $0$.

## Constraints and clarifications

$1 \leq T \leq 10$.

$0 \leq x \leq y \leq 10^9$

The given subarrays are aligned.

$0 \leq z < 2^{32}$.

$1 \leq N \leq 50,000$.

The sum of all $N$ values across all tests in a file is at most $100,000$.

For $5$ points, the subarrays in the input do not intersect, and $N \leq 100$.

For another $15$ points, $N \leq 100$.

For another $30$ points, the values in the array are odd.

The first feedback test corresponds to the first $subtask$, the second feedback test corresponds to the second $subtask$, the third and fourth feedback tests correspond to the third $subtask$.

## Example

`aligned.in`
```
3
2
0 1 2
0 0 1 2
0 1 2
0 0 4
2
0 0 1 0 0 2 1 0 0
```

`aligned.out`
```
1
0
0
```

## Explanation

The constraints in the first test are satisfied by choosing the values

$1, 2, 1, \dots$.