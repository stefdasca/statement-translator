A number is called a *palindrome* if when read from left to right it is identical to the number read from right to left. For example, the numbers $131$ and $15677651$ are palindromes. A number that is not a palindrome can be transformed into a palindrome by adding one or more digits to its right.

Given an array of $n$ natural numbers, write a program that solves the following two tasks:
1. Determine the minimum total number of digits that need to be added so that each value in the array is a palindrome;
2. Considering that we can add at most $S$ digits, determine the maximum number of consecutive palindrome terms in the obtained array.

# Input data
The input file `palindrome.in` contains on the first line the number $C$, representing the task that needs to be solved ($1$ or $2$). The second line contains a natural number $n$, representing the number of values in the array. On the next $n$ lines, there are the $n$ numbers in the array, one number per line. If $C = 2$, the last line of the input file will contain the natural number $S$ representing the maximum number of digits that can be added.

# Output data
The output file `palindrome.out` will contain a single line with the answer to task $C$ from the input file.

# Constraints and clarifications

* $1 \leq n \leq 50000; 0 \leq S \leq 500000$;
* The numbers in the array have at most $50$ digits;
* For $15$ points, $C = 1$ and $n = 1$;
* For $10$ points, $C = 2$, $S = 0$, $1 < n \leq 100$ and the numbers in the array have at most $18$ digits;
* For $14$ points, $C = 1$, $1 < n \leq 1000$ and the numbers in the array have at most $18$ digits;
* For $15$ points, $C = 2$, $S > 0, 1 < n \leq 1000$ and the numbers in the array have at most $18$ digits;
* For $16$ points, $C = 2$, $1000 < n \leq 50000$ and the numbers in the array have at most $18$ digits;
* For $13$ points, $C = 1$, $1000 < n \leq 50000$ and the numbers in the array have between $19$ and $50$ digits;
* For $17$ points, $C = 2$, $1000 < n \leq 50000$ and the numbers in the array have between $19$ and $50$ digits;

# Example 1

`palindrome.in`
```
1
5
12232
131
12345
0
7717
```

`palindrome.out`
```
7
```

## Explanation

$C = 1, n = 5$. 

- To transform $12232$ into a palindrome we need to add a minimum of two digits ($1223221$);
- For $12345$, we need to add a minimum of $4$ digits ($123454321$);
- For $7717$, we need to add a minimum of one digit ($77177$);
- The numbers $131$ and $0$ are already palindromes.

In total $2+4+1=7$.

# Example 2

`palindrome.in`
```
2
7
12232
131
12345
0
7717
1244
215809
4
```

`palindrome.out`
```
3
```

## Explanation

$C = 2, n = 7, S = 4$, so at most $4$ digits can be added.

We can add the $4$ digits to the number $12345$ resulting in a sequence of length $3$ consisting only of palindromes ($131 \\ 123454321 \\ 0$). 
Another option is to add one digit to $7717$ and two digits to $1244$ to get a sequence of length $3$ consisting only of palindromes ($0 \\ 77177 \\ 124421$).

For any other option, the obtained sequence of palindromes has fewer terms.