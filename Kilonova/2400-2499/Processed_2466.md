> "The 'T' is not pronounced." - An international olympiad participant

# Task

Four words can **form** a square such that two of them occupy the top and bottom sides, and the other two occupy the left and right sides. The words on the horizontal sides are read from left to right, and the words on the vertical sides are read from top to bottom. Notice how in the corners, pairs of words share the same letter. In the adjacent image, a possible combination of words is illustrated: `INFO`, `ANNA`, `IARĂ` and `OCNA`:

~[WhatsApp Image 2024-03-06 at 23.15.13.jpeg|align=center]

Given a list of words with equal lengths, your task is to count how many different squares you can form. **You cannot use the same word more than once to form a square.** Two squares are different if they differ by at least one character.

# Input data

The input file `full-house.in` contains on the first line $N$, the number of given words.
The next $N$ lines contain the words in *uppercase* Latin letters. The words are pairwise distinct and of the same length.

# Output data

The output file `full-house.out` will contain the required answer as specified in the problem statement.

# Constraints and clarifications

* $N \le 10^5$
* The given words are **pairwise distinct and have the same length**
* The maximum length of a word is $10$ characters
* We guarantee that in our tests, the answer fits in a 64-bit integer type (long long in C/C++).
* For $30$ points, $N \le 100$

# Example 1

`full-house.in`
```
4
NIVA
HLAD
HSIN
DEDA
```

`full-house.out`
```
2
```

# Example 2

`full-house.in`
```
6
BAKA
BARA
BALC
CALC
ARHC
BLIC
```

`full-house.out`
```
8
```

