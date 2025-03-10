Bogdan received a magical book with $N$ pages from his friend, Zâna Lalea, on his birthday from the library of the Magic Forest. To read this book, Bogdan must consume energy. For each digit in the pagination of the book, he needs to consume one unit of energy. In the Magic Forest, the digit $K$ is considered a *magic digit*, and for each occurrence of it in the page numbers of the book, the boy needs to consume an additional unit of super-energy.

# Task

Bogdan wishes to read the entire magical book but doesn't know if the reading will deplete all his energy before he reaches the end. Therefore, the boy asks you to help him and answer two questions:
1. What is the amount of energy Bogdan will need to read the entire book?
2. What is the amount of super-energy required to read the whole book?

# Input data

The first line will contain two natural numbers $C$, $N$, where $C$ represents the task that needs to be solved, and $N$ represents the number of pages in the book. If $C=2$, then the second line will also contain a number $K$, representing the *magic digit* from the Magic Forest.

# Output data

- If $C=1$, the first line will contain a natural number representing the number of energy units that Bogdan needs to read the entire book.
- If $C=2$, the first line will contain a natural number representing the number of super-energy units that Bogdan needs to use to be able to read the whole book.

# Constraints and clarifications

* $1 \leq C \leq 2$
* $1 \leq N \leq 100\ 000$
* $1 \leq K \leq 9$
* Page numbering starts with page $1$ and ends with page $N$.
* For $30$ points, $C=1$.
* For $5$ points, $C=2$ and $N \leq 99$.
* For another $10$ points, $C=2$ and $N \leq 999$.
* For another $25$ points, $C=2$ and $N \leq 9999$.
* For another $30$ points, $C=2$, without further additional constraints.

# Example 1

`stdin`
```
1 15
```

`stdout`
```
21
```

## Explanation

Task 1 is solved. Pages from $1$ to $9$ require one unit of energy each, and for pages from $10$ to $15$, two units of energy each are used. In total, Bogdan uses $9 \cdot 1 + 6 \cdot 2 = 21$ energy units.

# Example 2

`stdin`
```
2 46
2
```

`stdout`
```
15
```

## Explanation

Task 2 is solved. Bogdan uses one unit of super-energy for each of the pages $2$, $12$, $20$, $21$, $23$, $24$, $25$, $26$, $27$, $28$, $29$, $32$, and $42$, and for page $22$, two units of super-energy are used. In total, $1 \cdot 13 + 2 \cdot 1 = 15$ super-energy units will be used.