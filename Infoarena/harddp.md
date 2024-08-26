## Task

Sorin recently read "Legendele Olimpului", a book that opened the path to a grand destiny for him. Similar to Orpheus in search of Eurydice, he embarks on his initiation journey known as the "myth of descending into the basement". His path leads him to follow the algorithm of the longest common subsequence. The heavy wooden door closes behind him. The commission of the underworld gives him a string $A$ of $N$ characters consisting of $0$ and $1$. He must find a string $B$, of length $N$, also consisting of $0$ and $1$, such that the length of the longest common subsequence between $A$ and $B$ is minimal. Help Sorin transcend to the Olympic stage by solving the problem.

## Input data

The input file `harddp.in` will contain on the first line a natural number $T$, representing the number of tests. The second line contains $N$, an integer. The third line contains a binary string of length $N$ (without spaces between characters). The structure of the test repeats $T$ times.

## Output data

The output file `harddp.out` will contain $T$ lines, one for each test. A line should contain a binary string of length $N$.

## Constraints and clarifications

$1 \leq T \leq 75$

$1 \leq N \leq 1000$

Please do not tell the commission what Sorin would say!

## Example

`harddp.in`
```
1
3
100
```

`harddp.out`
```
011
```