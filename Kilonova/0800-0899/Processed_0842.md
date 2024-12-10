Gică and Lică work at a toy factory, in different shifts. This year the factory owner decided to make and sell mărțișoare. The finished mărțișoare are placed in consecutively numbered boxes. The boxes are arranged in a strictly increasing and consecutive order according to their numbers. Gică must take, in order, each box, tie a red and white string to each mărțișor, and then put them back into the box.

In each shift, Gică writes on a magnetic board, using magnetic digits, the numbers of the boxes for which he has tied strings to the mărțișoare, in strictly increasing order. When Gică's shift ends, Lică, who works in the following shift, comes and packages the boxes with the numbers on the board and sends them to the stores. Everything goes smoothly until one day, when two digits on the board demagnetize and fall off, leaving two blank spots. Lică notices this, picks them up from the floor, and randomly places them back on the board in the two blank spots. The only rule he follows is that the digit $0$ cannot be the first digit of a number.

~[martisoare.png]

# Task

Write a program that reads the natural numbers $N$ (representing the number of numbers written on the board) and $c_1$, $c_2$, \dots, $c_N$ (representing the numbers written, in order, on the board after Lică has filled the two blank spots with the fallen digits) and determines:

* the two digits that were swapped, if filling the spots changed the sequence of numbers originally written by Gică;
* the maximum number that was written on the board by Gică.

# Input data

The input file `martisoare.in` contains on the first line the natural number $N$, representing the number of numbers on the board. The second line of the file contains, in order, the $N$ numbers $c_1$, $c_2$, ..., $c_N$, separated by spaces, representing, in order, the numbers that exist on the board after Lică filled the two blank spots with the fallen digits.

# Output data

The output file `martisoare.out` should contain on the first line two digits, in increasing order, separated by a space, representing the two digits that were swapped, or `0 0` if replacing the fallen magnetic digits onto the board didn't change the sequence of numbers written by Gică. The second line should contain a number representing the maximum number in the consecutive sequence written by Gică on the board.

# Constraints and clarifications

* $4 \leq N \leq 100 \ 000$;
* $1 \leq c_i \leq 100 \ 000$;
* $N$, $c_1$, $c_2$, $\\dots$, $c_N$ are natural numbers;
* the two digits that fall off the board may come from the same number;
* For solving task a), you will receive 60% of the score, and for task b), you will receive 40% of the score.

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

The digit $2$ from the first number and the digit $6$ from the second number were swapped. The largest number written by Gică on the board is $29$.

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

The digits in the last number were swapped. The largest number written by Gică on the board is $98$.

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