Assume we have $n$ prime numbers denoted as $a_1, a_2,..., a_n$ sorted in strictly increasing order. We form a strictly increasing sequence $b$ whose elements are all multiples of these $n$ prime numbers such that common multiples appear only once. Assume that the numbering of positions of the elements in the sequence $b$ also starts from $1$.

# Task
Write a program that reads the value of $n$ from the input file and then the $n$ elements of the sequence $a$, determines the element at position $m$ from the sequence $b$ and displays this value in the output file.

# Input data
The input file `numar.in` contains 
- The first line contains two natural numbers separated by a space which represent the value of $n$ and the value of $m$ respectively;
- The second line contains $n$ prime natural numbers separated by a space which represent the values of the elements of sequence $a$. These values are in strictly increasing order, and the last one is less than one million.

# Output data
The output file `numar.out` will contain on the first line a single value which represents the term at position $m$ from the sequence $b$.

# Constraints and clarifications
* For $30\%$ of tests  $n \leq 20, m \leq 1 \ 000, a_1 \leq 50$
* For the other $70\%$ of tests  $21 \leq n \leq 100, 1001 \leq m \leq 15 \ 000, 51 \leq a_1 \leq 1 \ 000$
* $a_n \lt 1 \ 000 \ 000$

# Examples

`numar.in`
```
3 10 
2 3 5
```

`numar.out`
```
14
```

`numar.in`
```
4 20
7 23 37 131
```

`numar.out`
```
98
```

`numar.in`
```
3 11111
977 1009 1031
```

`numar.out`
```
3726237
```

Explanations
---

The sequence $b$ is formed from values: `2,3,4,5,6,8,9,10,12,14,15,16,18,20,21,22…`
At position $10$ is the number $14$