Sure, here is the translated competitive programming problem statement:

---

Gică and Lică work in a toy factory, in different shifts. This year, the factory owner decided to make and sell “mărțișoare.” The finished mărțișoare are placed in consecutively numbered boxes. The boxes are arranged in strictly increasing and consecutive order of their numbers. Gică needs to take each box in order, tie a red and white string to each mărțișor and then put them back in the box.

In each shift, Gică writes on a magnetic board, using magnetic digits, in strictly increasing order, the numbers of the boxes for which he tied strings to the mărțișoare. When Gică’s shift ends, Lică, who works the next shift, comes and packages the boxes with the numbers on the board and sends them to the stores. Everything goes smoothly until one day, when two digits on the board demagnetize and fall, leaving two empty spots. Lică notices this, picks them up, and puts them randomly back on the board in the two empty spots. The only thing he takes into account is that the digit $0$ cannot be the first digit of a number.

~[martisoare.png]

# Task

Write a program that reads the natural numbers $N$ (representing the number of numbers written on the board) and $c_1, c_2, \ldots, c_N$ (representing the numbers written, in order, on the board, after Lică filled the two empty spots with the fallen digits) and determines:

* the two digits that were swapped, if after filling the empty spots, they changed the sequence of numbers written by Gică;
* the maximum number written on the board by Gică.

# Input data

The input file `martisoare.in` contains:

- On the first line, the natural number $N$ representing the number of numbers on the board.
- The second line of the file contains, in order, the $N$ numbers $c_1, c_2, \ldots, c_N$, separated by a space, representing, in order, the numbers existing on the board, after Lică filled the two empty spots with the fallen digits.

# Output data

The output file `martisoare.out` will contain:

- On the first line, two digits, in increasing order, separated by a space, representing the two digits that were swapped or `0 0` if the two magnetic digits that fell did not change the sequence of numbers written by Gică after being placed back on the board.
- The second line will contain a number representing the maximum number in the sequence of consecutive numbers written by Gică on the board.

# Constraints and clarifications

* $4 \leq N \leq 100\ 000$;
* $1 \leq c_i \leq 100\ 000$;
* $N$, $c_1$, $c_2$, $\\dots$, $c_N$ are natural numbers;
* the two digits that fell off the board may come from the same number;
* For solving task (a), 60% of the points are awarded, and for solving task (b), 40% of the points are awarded.

# Example 1

`martisoare.in`
```
5
65 22 27 28 29
```

`martisoare.out`
```
2 6
29
```

## Explanation

Gică wrote on the board, in order, the numbers: $25$, $26$, $27$, $28$, $29$

The digit $2$ from the first number and digit $6$ from the second number were swapped. The largest number written by Gică on the board is $29$.

# Example 2

`martisoare.in`
```
4
95 96 97 89
```

`martisoare.out`
```
8 9
98
```

## Explanation

Gică wrote on the board, in order, the numbers: $95$, $96$, $97$, $98$

The digits of the last number were swapped. The largest number written by Gică on the board is $98$.

# Example 3

`martisoare.in`
```
5
35 36 37 38 39
```

`martisoare.out`
```
0 0
39
```

## Explanation

Gică wrote on the board, in order, the numbers: $35$, $36$, $37$, $38$, $39$

The sequence of numbers was not changed, the largest number being $39$.