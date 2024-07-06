~~~~[papusa.png|align=right]

Matrioșka Doll is a wooden toy, hollow inside. Therefore, any other Matrioșka doll of smaller height can be placed inside it.
At a souvenir shop, there are $n$ Matrioșka dolls arranged in a row, equally distributed on two adjacent shelves. The dolls on the left shelf are placed in the first half positions: $1$, $2$, $\\dots$, $\\frac{n}{2}$, and the dolls on the right shelf are placed in the second half positions: $\\frac{n}{2}+1$, $\\dots$, $n$. By notation $\\frac{n}{2}$, we mean half the number $n$.
Ana and Iulia want to buy as many Matrioșka dolls as possible, but their father imposes the following rules:
* Iulia is allowed to choose dolls from the left shelf, and Ana from the right shelf;
* If multiple dolls are bought from a shelf, they must be on consecutive positions on that shelf;
* The first doll bought by a girl should be shorter than the second one, the second one shorter than the third one, and so forth, such that each doll can fit inside the next one bought;
* The last dolls bought must be at the ends of the shelves, and additionally:
	1. if the last doll bought by Iulia is in position $1$ then the last doll bought by Ana must be in position $n$;
	2. if the last doll bought by Iulia is in position $\\frac{n}{2}$ then the last doll bought by Ana must be in position $\\frac{n}{2}+1$

To be able to choose as many dolls as possible while adhering to these rules, the girls are allowed to perform the following operation simultaneously, until returning to the initial arrangement of the dolls:
* Iulia moves the doll from position $1$ to position $\\frac{n}{2}$, shifting all other dolls on her shelf one position to the left;
* Ana moves the doll from position $n$ to position $\\frac{n}{2}+1$, shifting all other dolls on her shelf one position to the right;

# Task

To help Iulia and Ana purchase together a maximum number of dolls, write a program that reads a natural number $n$ and the heights of the $n$ dolls and determines:

1. the number $M$ of operations performed simultaneously by the girls;
2. the maximum number $P$ of dolls that will be bought.

# Input data

The text file `papusa.in` contains the first line, a natural even number $n$, representing the number of dolls. The second line contains $n$ natural numbers separated by a space, representing the heights of the dolls placed on the two shelves, in order from position $1$ to $n$.

# Output data

The output file `papusa.out` will contain:

* on the first line, the natural number $M$;
* on the second line, the natural number $P$.

# Constraints and clarifications

* $2 \leq n \leq 1 \ 000$, $n$ is an even number
* $1 \leq$ heights of the dolls $ \leq 10 \ 000$
* If the maximum number of dolls is obtained without performing any moving operation then $M = 0$
* For all input tests, there is a single configuration for which the maximum number of dolls can be bought
* Solving task $1$ awards $40\\%$ of the points, solving task $2$ awards $60\\%$ of the points

# Example

`papusa.in`
```
8
5 7 2 4 6 10 14 8
```

`papusa.out`
```
2
7
```

# Explanation 

Iulia's shelf contains the dolls with heights $5$, $7$, $2$, $4$, and Ana's shelf contains the dolls with heights $6$, $10$, $14$, $8$. In this arrangement, Iulia and Ana can buy the dolls with heights $2 \ 4 \ 6$ or $5 \ 8$. At most $3$ dolls can be bought.
The configuration obtained after the first moving operation is: $7 \ 2 \ 4 \ 5 \ 8 \ 6 \ 10 \ 14$. In this arrangement, Iulia and Ana can buy the dolls with heights $2 \ 4 \ 5 \ 6 \ 8$ or $2 \ 7 \ 6 \ 10 \ 14$. At most $5$ dolls can be bought.
The configuration obtained after the second moving operation is $2 \ 4 \ 5 \ 7 \ 14 \ 8 \ 6 \ 10$. In this arrangement, Iulia and Ana can buy the dolls with heights $2 \ 4 \ 5 \ 7 \ 6 \ 8 \ 14$ or $2 \ 6 \ 10$. At most $7$ dolls can be bought.
The configuration obtained after the third moving operation is $4 \ 5 \ 7 \ 2 \ 10 \ 14 \ 8 \ 6$. In this arrangement, Iulia and Ana can buy the dolls with heights $2 \ 10$ or $4 \ 6$. At most $2$ dolls can be bought.
The maximum number of dolls bought is $7$ and it is obtained after the 2nd moving operation.