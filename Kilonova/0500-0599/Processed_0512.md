By the **unification** operation of two natural numbers $a$ and $b$, we understand obtaining the largest number that can be formed from the distinct digits from the writing of number $a$ and the distinct digits from the writing of number $b$. For example, unifying $a = 727952$ with $b = 92868$ will yield the number $99876522$, because from $a$ we will use the digits $2, 5, 7, 9$, and from $b$ the digits $2, 6, 8, 9$. The largest number we can form with these digits is $99876522$.

The unification operation can also be applied to $k$ numbers, following the same rule: for each of the $k$ numbers, identify the distinct digits that appear in its writing, then determine the largest number that can be formed using all these digits. For example, unifying the numbers $112$, $223$, and $12334$ will yield $43322211$.

Given are two natural numbers, $n$ and $k$, and a sequence of $n$ natural numbers $a_1, a_2, ..., a_n$.

# Task

Determine and print:
1. the largest number of exactly $k$ digits from the given sequence;
2. the largest number that can be obtained by unifying two values located at adjacent positions in the given sequence;
3. the largest number that can be obtained by unifying $k$ values located at consecutive positions in the given sequence.

# Input data
The input file `unificare.in` contains on the first line a natural number $C$, representing the task that must be solved ($1$, $2$ or $3$), the second line contains $n$ and $k$, with the significance from the statement, and the third line contains the $n$ terms of the sequence specified in the order in the sequence. The numbers on the same line of the file are separated by a space.

# Output data
In the output file `unificare.out`:
* if $C = 1$, contain on the first line the largest number of $k$ digits from the given sequence;
* if $C = 2$, contain on the first line the largest number obtained by unifying two adjacent numbers in the sequence;
* if $C = 3$, contain on the first line the maximum value obtained by unifying $k$ values located at consecutive positions.

# Constraints and clarifications

* $C \in \{1,2,3\}$; $1 \leq n \leq 100\ 000$; $1 \leq k \leq n/2$;
* $0 \leq a_i \leq 100\ 000\ 000$, for any $1 \leq i \leq n$;
* For $20$ points, $C = 1$ and $k \leq 8$;
* For $5$ points, $C = 2$ and $n = 2$;
* For $10$ points, $C = 2$ and $0 \leq a_i \leq 9$, for any $1 \leq i \leq n$;
* For $35$ points, $C = 2$ and no additional constraints;
* For $15$ points, $C = 3$ and $k \leq 8$;
* For $15$ points, $C = 3$ and $k \leq n / 2$.

# Example 1

`unificare.in`
```
1
5 3
112 223 12334 561 289
```

`unificare.out`
```
561
```

## Explanation

$C = 1$, $n = 5$ and $k = 3$. In the sequence there are $4$ numbers that have exactly $3$ digits: $112$, $223$, $561$, and $289$, the largest being $561$.

# Example 2

`unificare.in`
```
2
5 3
112 223 12334 561 289
```

`unificare.out`
```
6543211
```

## Explanation

$C = 2$, $n = 5$ and $k = 3$, we do not use the value of $k$ and by unifying $a_3$ with $a_4$ we will get the largest value: $6543211$.

# Example 3

`unificare.in`
```
3
5 3
112 223 12334 561 289
```

`unificare.out`
```
9865432211
```

## Explanation

$C = 3$, $n = 5$ and $k = 3$. The largest value that can be obtained is $9865432211$ and we obtain it by unifying $a_3$ with $a_4$ and $a_5$.