Mrs. Teacher told the children in the third grade that they are big enough to write their math assignments on the computer, in a text file. The last assignment involves solving an arbitrary number of simple exercises. Each exercise asks to calculate the sum of two natural numbers. The children must write each exercise on a separate line and end the line with a semicolon. Within the exercises, there must not be a single space!

Costel, a student skilled in math but also in using the computer, writes his homework conscientiously and then emails it to Gigel, his best friend (but less diligent $\\dots$). Gigel receives the assignment with joy, opens the file and $\\dots$ surprise: none of the exercises were in place anymore! Spaces appeared where you didn't expect them, some exercises were written on $2$ or more lines, and some exercises were missing one of the terms or the result!

# Task

Write a program to restore the assignment to the form required by the teacher. Each exercise will be written on a separate line, without any spaces. Each line will end with a “;” (semicolon). Additionally, you will have to find the missing numbers!

# Input data

The input data is read from the file `adun.in`, which contains an unspecified number of lines with exercises in the form: $term_1$ + $term_2$ = $result$; 

$term_1$, $term_2$ or $result$ may be missing. On one line there can be multiple equations or an equation can be written on multiple lines. An exercise may contain any number of spaces.

# Output data

The output data will be printed in the file `adun.out`, which contains, on separate lines, the exercises restored to the form: $term_1$ + $term_2$ = $result$; 

# Constraints and clarifications

* The input file contains at most $50$ lines.
* Each line in the input file has a maximum of $250$ characters.
* The terms that appear in the exercises are natural numbers less than or equal to $5 \ 000 \ 000 \ 000$.
* In the input file, the digits of a number are not separated by spaces.

# Example

`adun.in`
```
  12 + 2= ; 16
+ 300 = 316; + 3 =10;
  3000 + = 4000 ;
```

`adun.out`
```
12+2=14;
16+300=316;
7+3=10;
3000+1000=4000;
```