## Task

Oh no! Agent $P$ has fallen into Dr. Doofenshmirtz's trap! He revealed his evil plan to use his latest invention, the Perrynator, to eradicate all platypuses from the face of the Earth. But $Perry$ is always one step ahead. Once he escapes (in his well-known style), he finds the Perrynator's control panel. To his amazement, to save his species, he needs to find a secret permutation! Given the number $N$ of elements in the permutation, he has access to the following operation: ask, for a set of positions in the permutation, what is the minimum among the values at those positions. But $Doofenshmirtz$ makes life a nightmare! After each query, the elements outside the asked set are permuted one position to the left or right. Unfortunately, $P$ cannot tell you in which direction they rotate, so you are on your own.

## Interaction

Initially, the number $N$ is read from $stdin$. Your program is allowed to make queries by writing to the standard $output$: After each such query, the interactor will respond in $stdin$ with a number representing the minimum of the values at those positions, at the time of the query. When you are sure you have found the permutation, display a query of the form: representing the permutation at that moment. In short, you do not need to find the initial permutation, only the one after the queries. After each query, including the final one, you must print '\n' and flush the standard $output$. To flush, you can use the following table:

Limbaj         | Header necessary                 | Function
-------------- | -------------------------------- | -----------------------
C/C++          | ‎                                 | fflush(stdout) or cout.flush()
Pascal         | ‎                                 | flush(output)
Python         | ‎import sys                       | sys.stdout.flush()
Java           | ‎                                 | System.out.flush()
Rust           | ‎use std::io::{self,Write};       | io::stdout().flush().unwrap();

## Constraints

$1 \leq N \leq 100$

For tests worth 20 points, the shifting is done only to the right.

For other tests worth 20 points, $N \leq 4$.

For at most 205 queries (excluding the final one), the score on the test is 100%.

For more than 205 queries (excluding the final one), the score on the test is 50%.

For more than 10000 queries (excluding the final one), the score on the test is 0%.

## Example

`stdin`
```
5
3
2
```
`stdout`
```
? 1 3
? 2 1 4
! 5 3 4 2 1
```

## Explanation

The secret permutation was $[5, 3, 4, 2, 1]$. After the first query, $Perry$ receives the number 3, indicating that the value at position 3 is 3, and the permutation could become:

* $[5, 2, 3, 4, 1]$, which means shifting to the left.

* $[5, 1, 2, 3, 4]$, which means shifting to the right.

because position 3 remains the same while the others can be shifted left or right. The Perrynator chose $[5, 1, 2, 3, 4]$, meaning to the right.

Similarly, after the second query, Perry receives $\min(5,2) = 2$, the permutation could become:

* $[5, 3, 4, 2, 1]$, to the right.

* $[4, 5, 3, 2, 1]$, to the left.

The Perrynator chose $[4, 5, 3, 2, 1]$, meaning to the left, and Perry simply guessed it and saved his species. We remind you that the Perrynator is not under our control either, we are helping $Perry$, so we also don't know in which direction it chooses to shift.