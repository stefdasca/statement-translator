Here is the translated text according to your specifications:

---

Andrei, fascinated by the beauty of ancient mathematics, discovered a magical numerical sequence. This sequence is constructed by simple rules starting from an initial number $X$ and consists of all prime numbers greater than or equal to $X$.

However, being very curious, Andrei also discovered an ancient ritual that can be applied starting from this initial number $X$ and using the previously constructed magical sequence. Depending on when it is applied, this ritual follows these rules:

* If no ritual has been applied to $X$ yet, then the first number in the magical sequence will be added to $X$.
* If several rituals have been applied to $X$ and the most recent involved adding a number from the magical sequence, then the first number from the magical sequence that has not yet been used will be subtracted from $X$.
* If several rituals have been applied to $X$ and the most recent involved subtracting a number from the magical sequence from $X$, then the first number from the magical sequence that has not yet been used will be added to $X$.

The process continues until Andrei completes $N$ such rituals. Now, Andrei wants to find out what the value of $X$ is after the $N$ rituals and how many times the absolute value of $X$, after applying at least one ritual, was a prime number.

# Input data

The input file `prime.in` contains on the first line two integers, $X$ and $N$, separated by space.

# Output data

The output file `prime.out` will contain two lines. The first line will contain the value of $X$ after the $N$ rituals. The second line will contain how many times, during the performance of these rituals, the absolute value of $X$ was a prime number.

# Constraints and clarifications

* $1 \leq X \leq 10^6$
* $1 \leq N \leq 10^5$
* It is guaranteed that $N$ and $X$ are chosen so that any number used in a ritual $\leq 10^7$
* For tests worth $50$ points, $N \leq 10^4$.
* For other tests worth $50$ points, there are no additional constraints.

# Example 1

`prime.in`
```
2 9
```

`prime.out`
```
18
2
```

## Explanation

Starting from the initial number $X = 2$, the magical sequence generated according to the rules is $2, 3, 5, 7, 11, 13, 17, 19, 23,\dots$
* Initially $X = 2$.
* After the first ritual $X$ becomes $2 + 2 = 4$
* After the second ritual $X$ becomes $4 - 3 = 1$
* After the third ritual $X$ becomes $1 + 5 = 6$
* After the fourth ritual $X$ becomes $6 - 7 = -1$
* After the fifth ritual $X$ becomes $-1 + 11 = 10$
* After the sixth ritual $X$ becomes $10 - 13 = -3$, whose absolute value is a prime number.
* After the seventh ritual $X$ becomes $-3 + 17 = 14$
* After the eighth ritual $X$ becomes $14 - 19 = -5$, whose absolute value is a prime number.
* After the ninth ritual $X$ becomes $-5 + 23 = 18$.

# Example 2

`prime.in`
```
51 6
```

`prime.out`
```
37
1
```

## Explanation

Starting from the initial number $X = 51$, the magical sequence generated according to the rules is $53, 59, 61, 67, 71, 73,\dots$
* Initially $X = 51$.
* After the first ritual $X$ becomes $51 + 53 = 104$
* After the second ritual $X$ becomes $104 - 59 = 45$
* After the third ritual $X$ becomes $45 + 61 = 106$
* After the fourth ritual $X$ becomes $106 - 67 = 39$
* After the fifth ritual $X$ becomes $39 + 71 = 110$
* After the sixth ritual $X$ becomes $110 - 73 = 37$, whose absolute value is a prime number.

# Example 3

`prime.in`
```
47797 3
```

`prime.out`
```
95596
0
```

## Explanation

Starting from the initial number $X = 47\ 797$, the magical sequence generated according to the rules is $47\ 797, 47\ 807, 47\ 809,\dots$
* Initially $X = 47\ 797$
* After the first ritual $X$ becomes $47\ 797 + 47\ 797 = 95\ 594$
* After the second ritual $X$ becomes $95\ 594 - 47\ 807 = 47\ 787$
* After the third ritual $X$ becomes $47\ 787 + 47\ 809 = 95\ 596$

---