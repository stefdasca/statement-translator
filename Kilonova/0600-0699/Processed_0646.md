To win as much money as possible in the 6/49 lottery, LLM has devised the following strategy:

He placed all the natural numbers from 1 to 49 exactly once in every hat he found in his house. We mention that LLM has an infinite number of hats in his house (no one knows why). Now he has chosen $N$ hats and will draw 6 numbers from each. He noted on a sheet the $6 \times N$ numbers and gave you the sheet.

LLM has two types of questions for you, and he puts all his trust in you to answer the questions correctly so that he will manage to win the lottery.

# Task

If $P = 1$, find the maximum frequency of a digit in the $6 \times N$ numbers noted on the sheet.

If $P = 2$, find how many digits have the maximum frequency and what these digits are.

# Input data
The first line of the input file `loto.in` contains two natural numbers $P$ and $N$ separated by a space. The following $N$ lines contain $6$ numbers each, representing the numbers drawn by LLM from each hat.

# Output data

If $P = 1$, the first line of the output file `loto.out` contains a natural number representing the maximum frequency of a digit in the $6 \times N$ numbers. If $P = 2$, the first line of the output file `loto.out` contains a natural number representing the number of digits with the maximum frequency. The next line contains the digits with the maximum frequency, separated by a space.

# Constraints and clarifications
* $P = 1$ or $P = 2$;
* $1 \leq N \leq 100\ 000$;
* Each of the $6 \times N$ numbers is from $1$ to $49$;
* It is guaranteed that there are no two identical numbers drawn from the same hat;
* For 50 points, $P = 1$;
* For 50 points, $P = 2$.

# Example 1

`loto.in`
```
1 4
22 17 23 49 19 37
37 12 27 32 5 7
27 47 33 16 28 44
6 2 1 47 17 27
```

`loto.out`
```
10
```

# Example 2
`loto.in`
```
2 4
22 17 23 49 19 37
37 12 27 32 5 7
27 47 33 16 28 44
6 2 1 47 17 27
```

`loto.out`
```
2
2 7
```

# Explanation

There are two digits with the maximum frequency, namely $2$ and $7$. Both digits appear exactly $10$ times.