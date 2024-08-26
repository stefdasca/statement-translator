## Entropy

In general, you clean your room weekly, and you end up putting many things in the pantry, not thinking too much about what to do with them. You clean the pantry monthly and put things on the balcony that no longer fit. Today you are cleaning the balcony, and the situation is not too cheerful. According to your growth as a programmer, you will break the problem into smaller problems. Now you will deal with 3 boxes, each containing books, magazines, or newspapers. You probably should throw them all away, but you want to put all the books in box $1$, all the magazines in box $2$, and all the newspapers in box $3$. The boxes work like stacks, so the possible operations are to take an item from the top of one box and place it on the top of another box. You want to place all the items in their respective places using a reasonable number of operations.

## Input data

The input file `entropy.in` will contain on its first line the value $T$, representing the number of tests in the file. Each test contains $3$ lines, representing the content of box $1$, $2$, and $3$ respectively. A book is encoded by the character $a$, a magazine is encoded by the character $b$, and a newspaper is encoded by the character $c$. The top of the box is "to the right," i.e., the last character in the description of a box gives the type of the item at the top of that box. 

## Output data

The output file `entropy.out` will contain $T$ lines, each line describing the operations that solve the corresponding test. For reduced output size, the operations will be encoded as follows:
- A move from the top of box $1$ to the top of box $2$ will be encoded by the character $m$.
- A move from the top of box $1$ to the top of box $3$ will be encoded by the character $n$.
- A move from the top of box $2$ to the top of box $1$ will be encoded by the character $o$.
- A move from the top of box $2$ to the top of box $3$ will be encoded by the character $p$.
- A move from the top of box $3$ to the top of box $1$ will be encoded by the character $q$.
- A move from the top of box $3$ to the top of box $2$ will be encoded by the character $r$.

Thus, the description of operations will be a string of such characters. You can consult the example for clarifications.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq$ Number of items in a box $\leq 100$

The total number of operations used to solve a test among the $T$ must be at most $1300$.

Any sequence of operations that solves a test among the $T$ and respects the above length constraint is considered correct.

## Example

`entropy.in`
```
1
a
b
cba
```

`entropy.out`
```
qr
```

## Explanation

The first test describes a happy situation where it is enough to make two moves: the first from the top of box $3$ to the top of box $1$ and the second from the top of box $3$ to the top of box $2$. Any other solution that uses at most $1300$ moves is considered correct.