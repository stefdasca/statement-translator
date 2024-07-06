We call the "mirror" of the non-zero natural number $a$, the number $b$, obtained by modifying each digit in its binary representation. For example, for $a=22_{(10)}=10110_{(2)}$, we obtain $01001_{(2)}=9_{(10)}=b$.

# Task

Given the natural numbers $N$, $K$, and $N$ non-zero natural numbers, write a program that:
1. Transforms the terms of the given sequence into their binary representation, forming a new sequence by concatenating the binary digits. From this sequence, determine and display, separated by a space, all base $10$ representations corresponding to adjacent subarrays of exactly $K$ binary digits, traversed from left to right. If the last subarray does not have exactly $K$ binary digits, it will not be considered.
2. Apply $K$ transformations to the initial sequence, replacing at each step any term with its "mirror". No further operations will be performed on the terms that become zero. After performing the $K$ transformations, determine the longest subarray of numbers that have the digit $1$ in the same position in their binary representation. If there are multiple such subarrays of maximum length, the leftmost one is displayed.

# Input data

The input file `mirror.in` contains on the first line the number $C$, representing the task. The second line contains the natural numbers $N$ and $K$. The third line contains the $N$ numbers of the sequence separated by spaces.

# Output data

If $C=1$, then the output file `mirror.out` will contain the required numbers separated by a space, as stated in the problem. If $C=2$, then in the output file `mirror.out` print on the first line the maximum length of the determined subarray, and on the next line, separated by spaces, the position of the first and last term in the subarray (the first position is $1$).

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* $0 \leq K \leq 30$;
* The elements of the sequence are less than $2 \ 000 \ 000 \ 001$;
* For $30\%$ of the tests, the task will be $C=1$.

# Example 1

`mirror.in`
```
1
4 2
7 8 2 11
```

`mirror.out`
```
3 3 0 1 1 1
```

## Explanation

$7_{(10)}=111_{(2)}$; $8_{(10)}=1000_{(2)}$; $2_{(10)}=10_{(2)}$; $11_{(10)}=1011_{(2)}$; The concatenated sequence is: $\textbf{\underline{11}}11\textbf{\underline{00}}01\textbf{\underline{01}}01\textbf{\underline{1}}$ and grouped by $2$ we have the numbers: $11_{(2)}=3_{(10)}$; $11_{(2)}=3_{(10)}$; $00_{(2)}=0_{(10)}$; $01_{(2)}=1_{(10)}$; $01_{(2)}=1_{(10)}$; $01_{(2)}=1_{(10)}$.

# Example 2

`mirror.in`
```
2
5 1
37 72 101 50
116
```

`mirror.out`
```
3
1 3
```

## Explanation

After one transformation, the numbers in base 2 are:
~[img1.jpg|align=center|width=50em]

The longest subarray has length $3$, formed by the numbers $37$, $72$, $101$ starting at position $1$ and ending at position $3$. There is another such subarray $(101, 50, 116)$, but the leftmost one is chosen.