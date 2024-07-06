For a natural number `a`, the *cost* is defined as the absolute value (the modulus) of the difference between `a` and the nearest prime number to `a`. For an array of $n$ natural numbers, located at positions numbered from $1$ to $n$, a sequence of $q$ operations is applied in order. An operation consists of a replacement and a display and is described in the form `i x p`, with the meaning:
* first, replace the element at position $i$ in the array with $x$;
* then display the minimum total cost of conveniently selected elements from $p$ distinct positions in the array.

# Task

Given $n$ and the $n$ elements of the array, write a program that determines:
1. the sum of the costs of all elements in the given array;
2. the results displayed after applying each of the $q$ operations, in the specified form.

# Input data

The input file `primprim.in` will contain:
* On the first line, a natural number $C$, representing the task that needs to be solved ($1$ or $2$);
* On the second line, the natural number $n$, as described;
* On the third line, the $n$ elements of the array, in order. 
If $C = 2$, the fourth line will contain the natural number $q$, representing the number of operations, and the following $q$ lines will contain the $q$ operations, one operation per line, in the form described. The numbers on the same line are separated by a space.

# Output data

If $C = 1$, the output file `primprim.out` will contain a single line that will print the sum of the costs of all elements in the array. 
If $C = 2$, the output file `primprim.out` will contain $q$ lines, on line $i$ being written the result displayed after executing the $i$-th operation from the input file.

# Constraints and clarifications
* $1 \leq q \leq 2 * 10^5$;
* $1 \leq i,p \leq n \leq 10^6$; $1 \leq x \leq 10^6$;
* The elements of the array are non-zero natural numbers $\leq 10^6$;
* For $20$ points, $C = 1$, $n = 1$;
* For $22$ points, $C = 1$, $1 \lt n \leq 1 \ 000$;
* For $28$ points, $C = 2$, $n \leq 1 \ 000$, $q \leq 10$;
* For $30$ points, $C = 2$ and there are no additional restrictions.

# Example 1

`primprim.in`
```
1
5
8 1 3 5 9
```

`primprim.out`
```
4
```

## Explanation

$C = 1, n = 5$, and the array is $8, 1, 3, 5, 9$. The costs of the elements are, in order, $1, 1, 0, 0, 2$, so the sum is $4$.

# Example 2

`primprim.in`
```
2
5
8 1 3 5 9
3
2 6 4
3 5 2
5 12 5
```

`primprim.out`
```
2
0
3
```

## Explanation

$C = 2, n = 5$, and the initial array is $8, 1, 3, 5, 9$. The array is subjected to $3$ operations:
- After the first operation, where $i = 2$, $x = 6$ and $p = 4$, the array becomes $8, 6, 3, 5, 9$. The minimum total sum is obtained by selecting the values at positions $1, 2, 3$, and $4$, the costs being $1+1+0+0=2$. 
- After the second operation, where $i = 3$, $x = 5$ and $p = 2$, the array becomes $8, 6, 5, 5, 9$. We select the values at positions $3$ and $4$ (both having the cost $0$).
- After the third operation, where $i = 5$, $x = 12$ and $p = 5$, the array becomes $8, 6, 5, 5, 12$. We select all the values, so the sum is $1 + 1 + 0 + 0 + 1 = 3$.