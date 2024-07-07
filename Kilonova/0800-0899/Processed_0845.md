
A sequence $x_1, x_2, \dots, x_n$ consisting of $n$ distinct natural numbers is considered. A maximum number of contiguous neighboring elements in the sequence of the form $x_i, x_{i+1}, \dots, x_{k-1}, x_k, x_{k+1}, \dots, x_j$ ($1 \leq i < k < j \leq n$) with the property that $x_i < x_{i+1} < \dots < x_{k-1} < x_k > x_{k+1} > \dots > x_j$, is called a *mountain* with the peak $x_k$. Two mountain sequences have at most one common element in the sequence. A mountain sequence has at least $3$ elements. An example of a sequence formed with the values $3 \\ 4 \\ 6 \\ 8$ contains no mountain sequence, while one formed with the values $3 \\ 4 \\ 8 \\ 1 \\ 2 \\ 5 \\ 0$ contains $2$ mountain sequences: $3 \\ 4 \\ 8 \\ 1$ and $1 \\ 2 \\ 5 \\ 0$. 

After determining all the mountain sequences and their peaks, the peaks of the mountain sequences are removed from the sequence, and the procedure continues repeatedly with determining the new mountain sequences and their peaks from the newly obtained sequence. The procedure stops when the sequence no longer contains any mountain sequence. 

# Task

Write a program that reads the numbers $n, x_1, x_2, \dots, x_n$ and then determines:

1. the number of mountain sequences in the initial sequence;
2. the total number of mountain sequences obtained starting from the initial sequence until one that no longer contains any mountain sequence;
3. the number of elements in the final sequence that no longer contains mountain sequences.

# Input data

The input file `munte.in` contains on the first line the number $n$, and on the next line the natural numbers $x_1, x_2, \dots, x_n$ separated two by two by a space.

# Output data

The output file `munte.out` will contain on the first line a natural number according to task $1$, on the second line a natural number according to task $2$, on the third line a natural number according to task $3$.

# Constraints and clarifications

* $3 \leq n \leq 100$;
* $0 \leq x_i \leq 100\ 000$;
* Correctly solving task $1$ earns $20$% of the score.
* Correctly solving task $2$ earns $40$% of the score.
* Correctly solving task $3$ earns $40$% of the score.
* For the given tests, it is ensured that the initially given sequence contains at least one mountain sequence.

# Example

`munte.in`

```
8
1 2 5 0 6 9 3 4
```

`munte.out`

```
2
4
4
```

## Explanation

1. There are two mountain sequences: $1 \\ 2 \\ 5 \\ 0$ and $0 \\ 6 \\ 9 \\ 3$
2. After removing the peaks of the mountain sequences, the new sequence is $1 \\ 2 \\ 0 \\ 6 \\ 3 \\ 4$. This sequence contains $2$ mountain sequences: $1 \\ 2 \\ 0$ and $0 \\ 6 \\ 3$. After removing the peaks of the mountain sequences, the new sequence is $1 \\ 0 \\ 3 \\ 4$. The new sequence no longer contains any mountain sequence. In total, there are $4$ sequences.
3. The final sequence that no longer contains mountain sequences $1 \\ 0 \\ 3 \\ 4$ has $4$ elements.
