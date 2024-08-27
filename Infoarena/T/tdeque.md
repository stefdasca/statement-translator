## Task

A permutation of order $N$ is given. You have at your disposal a data structure called TDeque which allows the following operations:
1. $pushNext$, which adds the next element of the permutation to the right end of the structure, if it exists.
2. $frontToBack$, which moves the element from the right end of the structure to the left end.
3. $backToFront$, which moves the element from the left end of the structure to the right end.
We want to sort the elements of the given permutation in ascending order using the data structure presented above.

For example, if we have the permutation $1 \ 3 \ 2 \ 5 \ 4$, a way to sort this permutation is by applying the following operations:
0. Initially, the structure is empty: $()$
1. $pushNext$, the structure becomes: $(1)$
2. $pushNext$, the structure becomes: $(1, 3)$
3. $frontToBack$, the structure becomes: $(3, 1)$
4. $pushNext$, the structure becomes: $(3, 1, 2)$
5. $backToFront$, the structure becomes: $(1, 2, 3)$
6. $pushNext$, the structure becomes: $(1, 2, 3, 5)$
7. $frontToBack$, the structure becomes: $(5, 1, 2, 3)$
8. $pushNext$, the structure becomes: $(5, 1, 2, 3, 4)$
9. $backToFront$, the structure becomes: $(1, 2, 3, 4, 5)$

Display the minimum number of operations required to sort the permutation as well as the operations that need to be performed.

## Input data

The input file $tdeque.in$ contains on the first line the natural number $N$, and on the second line $N$ distinct natural numbers with values between $1$ and $N$, representing the permutation of order $N$ from the problem statement.

## Output data

The output file $tdeque.out$ will contain on the first line a number $M$, representing the number of operations performed to sort the permutation. The second line will contain exactly $M$ characters, representing the operations performed. The $i$-th character will be $1$ if operation $i$ is of type $pushNext$, $2$ if the operation is of type $frontToBack$, or $3$ if it is of type $backToFront$.

## Constraints

$1 \leq N \leq 1000$ 

You will receive $50\%$ of the points if your solution is correct and the number of operations performed is $\leq 1\,000\,000$

You will receive another $50\%$ of the points if your solution is correct and the number of operations performed is the minimum possible for the given input data.

## Example

`tdeque.in`
```
3
1 2 3
```

`tdeque.out`
```
3
111
```

`tdeque.in`
```
4
3 4 1 2
```

`tdeque.out`
```
6
111122
```

## Explanation

For the first example, the permutation is already sorted. So, the answer is $3$.

For the second example, by applying the operations from the output file, the structure will behave as follows: $() \rightarrow (3) \rightarrow (3, 4) \rightarrow (3, 4, 1) \rightarrow (3, 4, 1, 2) \rightarrow (2, 3, 4, 1) \rightarrow (1, 2, 3, 4)$.