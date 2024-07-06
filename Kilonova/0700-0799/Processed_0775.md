```markdown
In the attic, Andrei found the cover of an old book belonging to his grandfather, and scattered through several boxes, the torn pages of this book. He thinks it would make his grandfather very happy if he could restore the book and bind its pages to the cover.

After gathering all the found pages, Andrei realizes that they are not in order and some of them are missing. Thus, he decides to bind together with a clip the pages that should be arranged consecutively in the book.

Knowing the number of each page in the book found by Andrei, determine the number of clips Andrei needs and the largest number of pages that have been bound together with a clip.

# Task

Write a program that determines the number of clips needed for the book's pages and the largest number of pages that have been bound together with a clip.

# Input data

The input file `pagini.in` contains:

- The first line contains the number $n$ of pages, and on the following $n$ lines, a single natural non-zero number, representing the number of a page in the book.

# Output data

The output file `pagini.out` will contain:

- The first line contains a single number representing the number of clips
- The second line contains a single number representing the largest number of pages that have been bound together with a clip.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* The values in the array are at most equal to $10^6$
* The tests and constraints have been updated for the year $2023$

# Example

`pagini.in`
```
12
11
40
27
21
13
10
5
2
4
25
26
12
```

`pagini.out`
```
3
4
```

## Explanation

Pages $10, 11, 12, 13$ have been bound with a clip.  
Pages $4$ and $5$ have been bound with a clip.  
Pages $25, 26, 27$ have been bound with a clip.
```