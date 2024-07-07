
A sequence $A=(A_1, A_2, \dots, A_N)$, consisting of $N$ positive natural numbers, is considered. Two numbers are considered neighbors if they are in adjacent positions ($A_i$ has as neighbors $A_{i-1}$ and $A_{i+1}$ for any $1<i<N$, $A_1$ has only $A_2$ as a neighbor, and $A_N$ has only $A_{N-1}$ as a neighbor).

If two neighboring elements $A_i, A_{i+1}$ share at least one common digit, they can be unified. The unification process consists of removing all common digits from $A_i$ and $A_{i+1}$ and concatenating the resultant number from $A_{i+1}$ to the resultant number from $A_i$, forming a new number. $A_i$ will be replaced with the new number, and $A_{i+1}$ will be removed from the sequence.

For example, $A_i=23814$ and $A_{i+1}=40273$ have common digits $2, 3, 4$. After unification, we get $A_i=817$, and $A_{i+1}$ is removed. Note that if, after removing common digits, the numbers begin with insignificant zeros, they will be removed before concatenation. If one of the numbers has no digits left after removing the common digits, the resulting number will have the remaining digits of the other number. If both $A_i$ and $A_{i+1}$ have no digits left after removing the common digits, both numbers will be removed from the sequence without being replaced by another value.

The order in which the unifications are made in the sequence is important: at each step, the first pair of neighboring elements $A_i \ A_{i+1}$ that can be unified is chosen, considering the sequence from left to right. (For example, considering $A_i=123, A_{i+1}=234, A_{i+2}=235$, $A_i$ is unified with $A_{i+1} \rightarrow A_i=14$, and further unification with the next number is not possible).

# Task

Given the sequence of $N$ natural numbers, determine:

1. The digit that appears most frequently in the writing of all $N$ numbers; if there are multiple digits with the same maximum frequency, the smallest digit will be retained.
2. The sequence obtained by performing the maximum number of unifications according to the rules described in the statement.

# Input data

The input file `unific.in` contains on the first line a natural value $N$, followed by the $N$ natural numbers in the sequence $A$, one per line.

# Output data

The output file `unific.out` will contain on the first line a natural number $c$ representing the digit that appears most frequently in the writing of all $N$ natural numbers. On the second line, a natural number $Nr$ representing the number of natural numbers remaining in the sequence after performing the maximum number of unifications. On the third line, the remaining $Nr$ natural numbers will be written, in order, separated by a space. If, after the unification process, all numbers are eliminated, the output file will contain a single line, where the most frequent digit in the writing of the $N$ natural numbers will be written.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* The numbers in the initial sequence, as well as the numbers obtained after unifications, will not exceed $10^{18}$;
* For the test data, the sequence obtained after unifications is nonempty.
* For $30\%$ of the tests $N \leq 1 \ 000$;
* For $70\%$ of the tests, the natural numbers in the sequence have non-zero digits.
* For correctly determining the first task, $10\%$ of the score per test is awarded. The full score is awarded for correctly solving both tasks.

# Example

`unific.in`
```
10
6
47
67
40
123
231
1238
331
2035
50007
```

`unific.out`
```
3
2
0 837
```

## Explanation

The digit that appears most frequently is $3$ (appearing $6$ times).

Unify: $47$ with $67 \implies 46$. Remaining sequence: $6 \ 46 \ 40 \ 123 \ 231 \ 1238 \ 331 \ 2035 \ 50007$

Unify: $6$ with $46 \implies 4$. Remaining sequence: $4 \ 40 \ 123 \ 231 \ 1238 \ 331 \ 2035 \ 50007$

Unify: $4$ with $40 \implies 0$. Remaining sequence: $0 \ 123 \ 231 \ 1238 \ 331 \ 2035 \ 50007$

Unify: $123$ with $231$, both numbers are left without digits, so both will be eliminated. Remaining sequence: $0 \ 1238 \ 331 \ 2035 \ 50007$

Unify: $1238$ with $331 \implies 28$. Remaining sequence: $0 \ 28 \ 2035 \ 50007$

Unify: $28$ with $2035 \implies 835$. Remaining sequence: $0 \ 835 \ 50007$

Unify: $835$ with $50007 \implies 837$. Remaining sequence: $0 \ 837$
