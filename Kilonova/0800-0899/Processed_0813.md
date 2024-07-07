Consider an integer $N$ and a sequence of $M$ non-zero decimal digits. Determine if the number $N$ can be the result of a simple arithmetic expression (without parentheses), consisting exclusively of the digits from the given sequence and the arithmetic operators designated for addition and subtraction ($+, -$).

# Task

Write a program that reads the numbers $N$ and $M$ from the first line of the input file and the sequence of $M$ digits from the next line, and determines and prints the found expression or the value 0 if no solution exists.

# Input data

The input file `adunscad.in` contains on the first line the integers $N \\ M$, separated by a space, representing the value that needs to be obtained from evaluating the expression and the number of digits in the sequence. The second line of the input file contains the sequence of $M$ non-zero digits, separated by a space.

# Output data

The output file `adunscad.out` will contain on the first line the determined expression, if a solution exists, or the value $0$ if no solution exists.

# Constraints and clarifications

* $-180 \\leq N \\leq 180$;
* $2 \\leq M \\leq 20$;
* In the given sequence, digits can repeat.
* All digits in the sequence must also appear in the arithmetic expression, in the same order as they were read.
* In the arithmetic expression, any digit must be preceded by an operator; if the first digit is preceded by the + operator, it is not included in the expression. The arithmetic expression does not contain spaces.
* If the solution is not unique, a correct solution will be displayed.

# Example 1

`adunscad.in`
```
21 4
3 9 1 8
```

`adunscad.out`
```
3+9+1+8
```

# Example 2

`adunscad.in`
```
-1 4
1 2 3 5
```

`adunscad.out`
```
-1+2+3-5
```

# Example 3

`adunscad.in`
```
-7 7
1 1 1 1 1 1 1
```

`adunscad.out`
```
-1-1-1-1-1-1-1
```

# Example 4

`adunscad.in`
```
12 3
1 2 3
```

`adunscad.out`
```
0
