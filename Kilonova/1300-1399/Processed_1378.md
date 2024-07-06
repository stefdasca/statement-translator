~[Poza3.png|width=13em|align=right]

A 7-segment display is an electronic display device designed to show a __decimal digit__. These devices are widely used in digital clocks, electronic meters, and other devices for displaying numerical information. The $7$ segments are denoted by the letters `a`, `b`, `c`, `d`, `e`, `f`, `g`, as shown in the adjacent figure. Displaying one of the digits from $1$ to $9$ involves lighting up certain segments out of the $7$, as follows:
- Digit $1$: `b`, `c`
- Digit $2$: `a`, `b`, `d`, `e`, `g`
- Digit $3$: `a`, `b`, `c`, `d`, `g`
- Digit $4$: `b`, `c`, `f`, `g`
- Digit $5$: `a`, `c`, `d`, `f`, `g`
- Digit $6$: `a`, `c`, `d`, `e`, `f`, `g`
- Digit $7$: `a`, `b`, `c`
- Digit $8$: `a`, `b`, `c`, `d`, `e`, `f`, `g`
- Digit $9$: `a`, `b`, `c`, `d`, `f`, `g`

Designing various display systems must also consider the power required to display a digit. Lighting up one segment requires $1$ mW of power. Thus, depending on the digit displayed, the device requires a power equal to the number of segments lit up to display that digit. The power required to display a natural number is equal to the sum of the powers required to display each of its digits.

# Task

Write a program that reads two non-zero natural numbers $n$ and $p$, (number $n$ having all its digits non-zero) and calculates:

* the natural number $k$ representing the power required to display the number $n$;
* the largest natural number $t$, consisting only of non-zero digits, less than or equal to $n$, which requires for display a power of at most $p$ mW.

# Input data

The first line of the input file `7segmente.in` contains two non-zero natural numbers $n$ and $p$ (number $n$ having all its digits non-zero), separated by a space, as described above.

# Output data

The output file `7segmente.out` will contain on a single line, the two non-zero natural numbers $k$ and $t$ (number $t$ having all its digits non-zero), separated by a space, as described above.

# Constraints and clarifications

* $1 \leq n \leq 10^{19}$
* $2 \leq p \leq 150$
* For solving the first task, $20\%$ of the test score will be awarded.

# Example

`7segmente.in`
```
7654 12
```

`7segmente.out`
```
18 7511
```

## Explanation

The number $n$ is $7654$; the power required for display is $3 + 6 + 5 + 4 = 18$ mW, and the largest number, less than or equal to $7654$, consisting only of non-zero digits, which requires for display power of at most $12$ mW, is $7511$.