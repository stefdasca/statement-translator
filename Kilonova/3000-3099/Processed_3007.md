I'm here to help. Let's translate the provided competitive programming problem statement from Romanian to English while maintaining the original format and syntax:

---

I have a friend who is a fashion designer. To create her designs, she sometimes dyes the materials and asks me in advance to help her. Today, she wants to dye a fabric of length $N$ cm using $C$ shades of the same color, coded from $1$ to $C$. Each cm of the fabric is colored with the same shade along the entire width, resulting in a striped fabric. Initially, I simulate the dyeing of the material using a computer, and then my friend intervenes: from cm $A$ to cm $B$, the intensity of the color needs to be changed by $X$ points (the intensity can increase or decrease, resulting in a different shade). After numerous such changes, let's say $M$ changes, my friend will be satisfied and will proceed to the actual dyeing of the fabric.

# Task

Write a program that determines and displays:
1. The maximum length of a piece of fabric of the same color after the initial dyeing;
2. How the fabric will look after my friend's modifications.

# Input data

The input file `culori.in` contains on the first line the requirement ($1$ or $2$). The next line contains three natural numbers $C \\ N \\ M$ separated by a space, representing the number of colors, the length in cm of the fabric, and the number of modifications made by my friend; the following line contains $N$ natural numbers separated by spaces, $c_1 \\ c_2 \\ c_3 \\dots c_N$, representing the color of each cm of the fabric after the initial dyeing, and the next $M$ lines each contain $3$ numbers: two natural numbers $A \\ B$, separated by a space, representing $A$ - the starting position and $B$ - the ending position where the intensity modification ends, and, separated by a space, an integer $X$ representing the value by which the intensity is modified.

# Output data

The output file `culori.out` will contain a single line on which will be written a natural number determined according to the requirement if the requirement is $1$, or $N$ natural numbers determined according to the requirement if the requirement is $2$.

# Constraints and clarifications

* $0 < N < 10 \ 001$
* $0 < C < 1 \ 000 \ 001$
* $0 < M < 200 \ 001$
* After all the modifications, the shades remain within the set $\{1, 2, \dots, C\}$
* $20$ points are awarded for requirement $1$, $70$ points for requirement $2$; $10$ points are awarded automatically

# Example 1

`culori.in`
```
1
3 8 2
1 1 2 2 2 2 3 3
2 5 1
5 8 -1
```

`culori.out`
```
4
```

## Explanation

The longest sequence of equal elements is $2 \ 2 \ 2 \ 2$ and has $4$ elements.

# Example 2

`culori.in`
```
2
3 8 2
1 1 2 2 2 2 3 3
2 5 1
5 8 -1
```

`culori.out`
```
1 2 3 3 2 1 2 2 
```

## Explanation

After the first modification, the array is: $1 \ 2 \ 3 \ 3 \ 3 \ 2 \ 3 \ 3$
After the second modification, it is: $1 \ 2 \ 3 \ 3 \ 2 \ 1 \ 2 \ 2$ 

---