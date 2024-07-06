The problem statement has been translated as requested:

Given a sequence $v$ consisting of $N$ non-zero natural elements, not necessarily distinct. We can apply one type of operation on the sequence: swapping two elements that are on consecutive positions.

# Task
Given a natural number $K$, find the smallest lexicographic sequence that can be obtained by applying at most $K$ swaps of elements on consecutive positions.

# Input data
In the file `lexicografic.in` the first line contains $T$, representing the number of tests. The next $T$ tests follow, each on 2 lines. The first line of a test contains two numbers $N$ and $K$ separated by space. The second line of a test contains the $N$ elements of the sequence separated by spaces.

# Output data
In the file `lexicografic.out`, $T$ lines will be printed, each corresponding to the answer for each test. The line corresponding to a test will contain the $N$ elements separated by spaces of the smallest lexicographic sequence obtained from the initial sequence, after applying at most $K$ swaps of elements on consecutive positions.

# Constraints and clarifications
* $1 \leq N \leq 250 \ 000$;
* $T \leq 2 \ 500$;
* in an input file the total sum of the lengths of the sequences corresponding to the $T$ tests will not exceed $250 \ 000$;
* $1 \leq K \leq N \cdot (N-1)/2$;
* $1 \leq v[i] \leq N$, for $1 \leq i \leq N$;
* Please pay attention to the data type required to read the value of $K$;
* To grant the score for a test file, it is necessary to correctly solve all the $T$ tests;
* For test cases worth $5$ points, it is guaranteed $K = N \cdot (N – 1) / 2$;
* For other test cases worth $7$ points, it is guaranteed $K = 1$;
* For other test cases worth $23$ points, it is guaranteed $T \leq 10, N \leq 50$;
* For other test cases worth $4$ points, it is guaranteed $T \leq 10, N \leq 100$;
* For other test cases worth $12$ points, it is guaranteed $T \leq 10, N \leq 500$;
* For other test cases worth $24$ points, it is guaranteed $T \leq 10, N \leq 2 \ 000$;
* A sequence $a_1,a_2,...,a_n$ is lexicographically smaller than another sequence $b_1,b_2,...,b_n$ if there exists an integer `p` less than or equal to `N` such that: $a_1 = b_1, a_2 = b_2, ... , a_{p–1} = b_{p–1}$, and $a_p < b_p$.

# Example

`lexicografic.in`

```
3
5 2
4 2 3 1 1
4 3
2 1 3 4
6 4
5 3 5 3 4 6
```

`lexicografic.out`

```
2 3 4 1 1
1 2 3 4
3 3 5 4 5 6
```

## Explanations

For the first test:
The sequence consists of $N = 5$ elements, namely $v=(4,2,3,1,1)$. We can perform $K=2$ swaps. Swapping the elements $v[1]$ and $v[2]$ we obtain the sequence $(2,4,3,1,1)$, then after swapping the elements $v[3]$ and $v[2]$ we obtain the smallest lexicographic sequence $(2,3,4,1,1)$.