# The Digit

Gigel, being bored, was playing during his math class, drawing on a piece of paper. Unfortunately, the teacher saw him and told him he would get a grade of $4$ if he didn't solve the following problem: for a given value $N$, he has to determine the last digit of the sum $1^1 + 2^2 + \dots + N^N$.

## Task

Write a program to help Gigel determine the last digit of this sum for $T$ given values of $N$.

## Input data

The first line of the file `cifra.in` will contain the number $T$. The next $T$ lines will contain the values of $N$ for which the answer must be found.

## Output data

The $T$ lines of the file `cifra.out` will contain the answers for the given values of $N$ from the input file.

## Constraints and clarifications

$1 \leq T \leq 30\ 000$  
ATTENTION!  
$1 \leq N < 10^{100}$.  
The numbers must be read as strings!  
A score is given for a test only if all $T$ values in the output file are correct.

## Example

`cifra.in`  
```
5
1
2
3
4
5
```

`cifra.out`  
```
1
5
2
8
3
```

## Explanations

$1^1 = 1$  
$1^1 + 2^2 = 1 + 4 = 5$  
$1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32 \Rightarrow 2$  
$1^1 + 2^2 + 3^3 + 4^4 = 1 + 4 + 27 + 256 = 288 \Rightarrow 8$  
$1^1 + 2^2 + 3^3 + 4^4 + 5^5 = 1 + 4 + 27 + 256 + 3125 = 3413 \Rightarrow 3$