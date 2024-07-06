```markdown
A sequence $A$ consisting of $N$ integers, numbered from $1$ to $N$, is given. We call a subarray of the sequence $A$ any succession of consecutive elements in the form $A_i$, $A_{i+1}, \dots, A_j$, with $0 < i < j \leq N$.

# Task

Given the sequence $A$ with $N$ integers, you are required to answer $Q$ questions of the form: `i j k` ($0 < i < j \leq N$). For each question, determine how many numbers in the subarray $A_i, A_{i+1}, \dots, A_j$ have an occurrence frequency equal to $k$.

# Input data

The input file `fsecv.in` contains the nonzero natural numbers $N$ and $Q$ on the first line, as specified in the statement. On the next line, there are $N$ integers representing the values of the array $A$. On the following lines, the description of the $Q$ questions is found, one per line, in the format specified $i \ j \ k$.

# Output data

The output file `fsecv.out` will contain $Q$ lines. Each line will contain the answer to question $i$, with $1 \leq i \leq Q$.

# Constraints and clarifications

* $2 < N \leq 100 \ 000$; 
* $1 < Q \leq 100 \ 000$; 
* $0 < k \leq N$;
* $-100 \ 000 \leq A_i \leq 100 \ 000$; 

# Example

`fsecv.in`
```
11 3
1 2 4 3 2 5 6 4 5 2 1
1 6 2
2 7 3
4 11 1
```

`fsecv.out`
```
1
0
4
```

## Explanation

The subarray referred to in the first question is $1, 2, 4, 3, 2, 5$, and the answer is $1$.

The subarray referred to in the second question is $2, 4, 3, 2, 5, 6$, and the answer is $0$.

The subarray referred to in the third question is $3, 2, 5, 6, 4, 5, 2, 1$, and the answer is $4$.
```