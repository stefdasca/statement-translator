Here is the translated text of the competitive programming problem statement:

---

Rareș received a book as a gift in which the pages are shuffled. He decided to read it, **turning the pages in a single direction, from the first page to the last**, in the order they are placed in the book, following the algorithm below:

> Look for the page numbered $x=1$ at the beginning.
> After reading a page numbered $x$, he looks among the pages following this page, turning the pages, for the page numbered $x+1$, without looking through the pages placed before the page numbered $x$. If he finds it, he will continue reading in the same way, and if not, he will close the book and, on the following day, he will resume reading from the page numbered $x+1$, which he will first search for by turning the book from the beginning.
> Rareș will proceed similarly on the following days until he reads the entire book.

# Task

Write a program that reads a natural number $n$, representing the number of pages in the book and $n$ distinct natural numbers $x_1$, $x_2$, $\\dots$, $x_n$, representing the order in which the $n$ pages are placed in the book, and which determines:
1. the number of days in which Rareș reads the book;
2. the first day on which Rareș read the most pages and the number of pages read on that day.

# Input data

The input file `carte.in` contains on the first line the number $n$ of pages in the book and on the next line $n$ distinct integers $x_1$, $x_2$, $\\dots$, $x_n$, separated by a space, representing the order in which the pages are placed in the book.

# Output data

The output file `carte.out` will contain on the first line, separated by a space, three numbers, representing, in order:

* the number of days in which Rareș reads the book;
* the number of the first day on which Rareș read the most pages;
* the maximum number of pages read in a day.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$;
* the pages of the book are numbered with distinct natural numbers from $1$ to $n$;
* reading the book implies reading each page in the book only once;
* the days on which Rareș reads the book are numbered consecutively, starting with the number $1$;
* for the correct solution to sub-point 1, $40\%$ of the score is awarded and for each requirement of sub-point 2, $30\%$ of the score is awarded.

# Example

`carte.in`
```
9
7 1 3 6 8 2 4 9 5
```

`carte.out`
```
4 2 3
```

## Explanation

- on the first day he reads pages $1,2$;
- on the second day he reads pages $3,4,5$;
- on the third day he reads page $6$;
- on the fourth day he reads pages $7,8,9$.

He finished reading the book in $4$ days and day $2$ is the first day on which he read the most pages ($3$).

---

Please review and correct any potential grammar or syntax errors:
- "turning the pages in a single direction" could also be phrased as "flipping through the pages in the same direction."
- "without looking through the pages placed before the page numbered $x$" could be simplified to "without looking at the pages before page $x$."
- "which he will first search for by turning the book from the beginning" could be corrected to "which he will search for by flipping through the book from the beginning first."

These corrections provide a clearer and more concise version of the instructions:

---

Rareș received a book as a gift in which the pages are shuffled. He decided to read it, **flipping through the pages in the same direction, from the first page to the last**, in the order they are placed in the book, following the algorithm below:

> Look for the page numbered $x=1$ at the beginning.
> After reading a page numbered $x$, he looks among the pages following this page, flipping through the pages, for the page numbered $x+1$, without looking at the pages before page $x$. If he finds it, he will continue reading in the same way, and if not, he will close the book and, on the following day, he will resume reading from the page numbered $x+1$, which he will search for by flipping through the book from the beginning first.
> Rareș will proceed similarly on the following days until he reads the entire book.

# Task

Write a program that reads a natural number $n$, representing the number of pages in the book and $n$ distinct natural numbers $x_1$, $x_2$, $\\dots$, $x_n$, representing the order in which the $n$ pages are placed in the book, and which determines:
1. the number of days in which Rareș reads the book;
2. the first day on which Rareș read the most pages and the number of pages read on that day.

# Input data

The input file `carte.in` contains on the first line the number $n$ of pages in the book and on the next line $n$ distinct integers $x_1$, $x_2$, $\\dots$, $x_n$, separated by a space, representing the order in which the pages are placed in the book.

# Output data

The output file `carte.out` will contain on the first line, separated by a space, three numbers, representing, in order:

* the number of days in which Rareș reads the book;
* the number of the first day on which Rareș read the most pages;
* the maximum number of pages read in a day.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$;
* the pages of the book are numbered with distinct natural numbers from $1$ to $n$;
* reading the book implies reading each page in the book only once;
* the days on which Rareș reads the book are numbered consecutively, starting with the number $1$;
* for the correct solution to sub-point 1, $40\%$ of the score is awarded and for each requirement of sub-point 2, $30\%$ of the score is awarded.

# Example

`carte.in`
```
9
7 1 3 6 8 2 4 9 5
```

`carte.out`
```
4 2 3
```

## Explanation

- on the first day he reads pages $1,2$;
- on the second day he reads pages $3,4,5$;
- on the third day he reads page $6$;
- on the fourth day he reads pages $7,8,9$.

He finished reading the book in $4$ days and day $2$ is the first day on which he read the most pages ($3$).