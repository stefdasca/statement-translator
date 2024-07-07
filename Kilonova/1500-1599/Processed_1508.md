Certainly! Here's the translated text according to your specifications:

---

During the activities in â€œOtherwise Weekâ€, the seventh-grade students want to help organize the books in the school library. Each book is labeled with a code that is expressed as a string of distinct characters. These can be the digits `0`, `1`, $\\dots$, `9` and the first ten lowercase letters of the English alphabet `a`, `b`, $\\dots$, `j`. The code uniquely identifies each book, meaning there will be no two books with the same code, but also the literary genre to which they belong. Books of the same literary genre have the identification code made up of the same characters, distinct, arranged in a different order.

We call paired codes two identification codes that have the same number of characters and differ by one character. For example, the codes `42a8` and `2c8a` are paired codes. On the other hand, the codes `42a8` and `248a`, respectively `42ab` and `248c`, are not paired codes.

# Task

Given the string of $N$ identification codes, write a program to solve the following tasks:

1. Determine the number of books from the most numerous literary genre and the number of literary genres that have this maximum number of books.
2. Determine the number of codes, from the string of $N$, which are paired codes with the last code in the string.

# Input data

The input file `carte.in` contains the first line a natural number $C$. For all tests, $C$ can only take the values $1$ or $2$. The second line contains the number $N$ of books in the school library, and on the next $N$ lines, a string of characters on each line, representing the code for identifying a book.

# Output data

If the value of $C$ is $1$, only the first task will be solved. In this case, the output file `carte.out` contains the first line the maximum number of books of the same literary genre, $MAX$, and the second line the number of literary genres that have exactly $MAX$ books.

If the value of $C$ is $2$, only the second task will be solved. In this case, the output file `carte.out` contains the first line the number of paired codes with the last code in the string of $N$.

# Constraints and clarifications

* $1 \leq N \leq 1 \\ 000 \\ 000$
* For correctly solving the first task, 60 points are obtained, and for correctly solving the second task, 40 points are awarded.

# Example 1

`carte.in`
```
1
8
1289f5
128905
129805
219805
12
1e2
12e
e21
```

`carte.out`
```
3
2
```

## Explanation

There are a maximum of $3$ books of the same literary genre. There are $2$ genres with a maximum number of books: `{128905, 129805, 219805}` and `{1e2, 12e, e21}`.

# Example 2

`carte.in`
```
2
10
1289f5
128905
5
12
129805
219805
218905
132
312
2189e5
```

`carte.out`
```
5
```

## Explanation

There are $5$ paired codes with `2189e5`: `1289f5, 128905, 129805, 219805, 218905`.

---