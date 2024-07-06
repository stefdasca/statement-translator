King Rufus wants to determine the heir to his fortune, meaning he wants to give the password to his safe to the smartest of his sons. Initially, the king had the password $X$ made up of $N$ non-zero digits and a key code $Q$ (a natural number with exactly $9$ digits, distinct, all non-zero). In each of the $K$ years of his reign, using the key code $Q$, Rufus modified a sequence of digits in the password to arrive at the final password $P$.

For each sequence, the position $S$ of the first digit in the sequence and the position $D$ of the last digit in the sequence are known. Thus, the sequence is made up of the digits located at positions $S$, $S+1$, $S+2$, $\dots$, $D$ in the password $X$.

Modifying a sequence in $X$ involves replacing each occurrence of the digit $1$ with the first digit of $Q$, then each occurrence of the digit $2$ with the second digit of $Q$, $\dots$, each occurrence of the digit $9$ with the last digit of $Q$.

To decide the heir, the king gives his sons the final password $P$, the key code $Q$, the number $K$ of years of reign, and the $K$ modified sequences and asks them to find: the initial password $X$, the **minimum position $Z$** in the password $X$ that appeared in the most sequences modified by the king during his $K$ years of reign, and the distinct digits that occupied position $Z$ during those $K$ years.

# Task
Write a program that reads the numbers $Q$, $N$, $K$, the $N$ digits of the final password $P$, and the $K$ pairs of positions $S$ and $D$, and solves the following two tasks:
1. Determine the initial password $X$;
2. Determine the **minimum position $Z** and the distinct digits that occupied this position during the $K$ years of reign.

# Input Data

The input file `mostenire.in` contains:
- The first line contains a natural number $C$ representing the task that needs to be solved ($1$ or $2$).
- The second line of the file contains the three natural numbers $Q$, $N$, and $K$, separated by a space.
- The third line of the file contains the $N$ digits of the final password $P$, separated by a space.
- Each of the following $K$ lines contains two natural numbers $S$ and $D$, separated by a single space, representing a pair of positions.

# Output Data

If $C=1$, the output file `mostenire.out` will contain on the first line the $N$ digits of the initial password $X$, separated by a space, in the order in which they appear in $X$, representing the answer to task $1$.

If $C=2$, the output file `mostenire.out` will contain on the first line the natural number $Z$, and on the second line the distinct digits that appeared at the **minimum position $Z$**, representing the answer to task $2$. These will be displayed in ascending order, separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$;
* The natural number $Q$ is made up of exactly $9$ digits, distinct and non-zero;
* The positions of the digits in the password $X$ are numbered with distinct consecutive numbers $1$, $2$, $\dots$, $N$;
* $1 \leq K \leq 100$;
* For all pairs of positions modified by the king: $S \leq D$;
* At least one digit in the password $X$ will be replaced;
* For correctly solving task $1$, $50$ points are awarded;
* For correctly solving task $2$, $50$ points are awarded.

# Example 1

Input file `mostenire.in`
```
1
712534698 12 4
1 4 7 1 3 4 7 1 4 8 1 8
2 4
6 11
3 9
1 7
```

Output file `mostenire.out`
```
2 7 3 5 4 1 3 3 7 9 2 8
```

## Explanation

The task is 1, $N=12$, $K=4$.

~[mostenire.png]

# Example 2

Input file `mostenire.in`
```
2
712534698 12 4
1 4 7 1 3 4 7 1 4 8 1 8
2 4
6 11
3 9
1 7
```

Output file `mostenire.out`
```
3
1 2 3 7
```

## Explanation

The task is $2$, $N=12$, $K=4$.
$P=(1\ 4\ 7\ 1\ 3\ 4\ 7\ 1\ 4\ 8\ 1\ 8)$
The positions that appeared in the most sequences are: $3, 4, 6, 7 \rightarrow Z=3$, and the distinct digits that occupied this position are $3, 2, 1, 7$. These digits will be written in the file in ascending order.