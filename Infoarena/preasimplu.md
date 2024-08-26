## Task

Too Simple!

On his way to international olympiads, Architect Ierdnac thought of the following problem: Let $b_i$ be a binary array with $N$ elements. Initially, all its bits are set to $0$. Let $flip(l, r)$ be an operation that changes the array elements as follows:
• If the rank of the element we refer to does not belong to the interval $[l, r]$, then the respective element remains unchanged;
• Otherwise, the element changes its value (i.e., from $0$ it becomes $1$ and, respectively, from $1$ it becomes $0$).

We are asked to determine the number of final arrays that can be obtained if exactly $K$ flip operations are performed. Since the answer can be quite large, it should be displayed modulo $10^9 + 7$. Seeing this problem there, Bossu' Frumosu' replied immediately with the already famous phrase "Too simple!" and suggested several methods to artificially complicate the problem. After long deliberations, the committee decided - the number of solutions should be displayed modulo an arbitrary non-zero natural number $MOD$! Unfortunately, Bossu' Frumosu' did not know how to solve the new problem, but Architect Ierdnac immediately exclaimed "But wait, it's easy!" and thus, the problem was included in the Junior Challenge 2016 problem set.

## Input Data

The input file `preasimplu.in` will contain the first line with a non-zero natural number $T$, representing the number of tests to follow. Then, the tests will be described on one line in the form $N \ K \ MOD$.

## Output Data

The output file `preasimplu.out` will contain $T$ lines, each containing the answer for the corresponding test from the input.

## Constraints

$1 \leq T \leq 250$

$1 \leq N, K \leq 300\ 000$

$2 \leq MOD \leq 10^6\ 007$

The sum of all $N$s in the file $\leq 600\ 000$

Subtask 1 (10 points):

$1 \leq N \leq 8$, $1 \leq K \leq 4$

- Each test in the group has $T = 32$ and each pair $(N, K)$ appears at most once in the input (Feedback test 2)

Subtask 2 (15 points):

$1 \leq N \leq 14$, $1 \leq K \leq 14$

- Each test in the group has $T = 52$ and each pair $(N, K)$ appears at most once in the input (however, the group's tests are not maximal with this property - otherwise, the time limit for such a small subtask would have to be increased far too much) (Feedback test 3)

Subtask 3 (25 points):

$1 \leq N \times K \leq 300\ 000$, and the sum of all tests in the current file in $N \times K$ $\leq 1\ 200\ 000$ (Feedback tests 7 and 8)

Subtask 4 (25 points):

$1 \leq N, K \leq 300\ 000$, $MOD = 10^9 + 7$ (Feedback tests 11 and 15)

Subtask 5 (25 points):

$Initial$ constraints (Feedback tests 17, 19, and 20)

## Example

`preasimplu.in`
```plaintext
1
2 1 1000
```

`preasimplu.out`
```plaintext
3
```

## Explanation

The initial array is $0 \ 0$. Using the operation $flip(1, 1)$, we obtain the array $1 \ 0$;

Using the operation $flip(2, 2)$, we obtain the array $0 \ 1$;

Using the operation $flip(1, 2)$, we obtain the array $1 \ 1$.

Thus, 3 different arrays can be obtained.