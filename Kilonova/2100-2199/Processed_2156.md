```markdown
# Task

Alex finds in the attic of his house a safe on which the following text is written: you can open this safe only if you determine, following certain rules, a cipher consisting of decimal digits, using $N$ given natural numbers formed from non-zero digits. The safe can be opened with one or more numbers, the important thing is that they are correctly determined.
The cipher required to open the safe is one of the numbers with the property that their digits can be permuted to obtain numbers, which can be found in the given numbers by deleting some of the digits. For example, for two given numbers $41611$ and $4343112$, we get 8 such numbers: $411, 141, 114, 14, 41, 11, 4, 1$. By deleting the third and last digits from $41611$, we obtain $411$, and by deleting the digits in positions $1, 2, 4,$ and $7$ from $4343112$, we obtain $411$ and so on for the other numbers.

Knowing the $N$ numbers, the number of variants for the cipher needed to open the safe must be determined, modulo $30 \\ 313$.

# Input data

The file `cifru.in` contains on the first line $N$, the number of numbers, and on the following $N$ lines, each containing a natural number formed only from non-zero digits.

# Output data

The output file `cifru.out` will contain on the first line the number of variants modulo $30 \\ 313$, for the cipher needed to open the safe.

# Constraints and clarifications

* $1 \leq N \leq 10$; 
* A number in the input file has at most $10 \\ 000$ digits.  
* The $N$ natural numbers do not contain the digit $0$.

# Example 1

`cifru.in`
```
2
41611
4343112
```

`cifru.out`
```
8
```

## Explanation

The numbers $411, 141, 114, 14, 41, 11, 4, 1$ meet the required condition.

# Example 2

`cifru.in`
```
3
4411222377788
7133144722288
4122213733388
```

`cifru.out`
```
11231
```
```