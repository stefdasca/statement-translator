# Spiral

Consider a 2-dimensional array that contains integer numbers. We define a spiral as the path through the matrix that, starting from the top-left corner, traverses element by element the first row, descends the last column, traverses the last row from right to left, ascends the first column, and then continues with the second row, the penultimate column, the penultimate row, and the second column, etc. The path stops somewhere in the array after all the elements have been traversed. Each element is visited exactly once.

## Task

Determine if the spiral of the given array forms an arithmetic progression. By arithmetic progression, we mean a sequence of numbers in which the difference between any two consecutive numbers is the same (for a sequence of $N$ numbers, $a_i - a_{i+1} = dif$, $i = 1, 2, \dots, n - 1$). If the answer is affirmative, determine the value of the last element in the spiral; otherwise, display the values of the first two elements in the spiral whose difference is not equal to the difference between the checked element values.

## Input data

The first line of the input file `spirala.in` contains two natural numbers ($nrlin$ and $nrcol$), representing the number of lines and the number of columns in the array, respectively. The next $nrlin$ lines contain $nrcol$ integer numbers each. Any two numbers in the file are separated by a space.

## Output data

If the spiral forms an arithmetic progression, the first line of the output file `spirala.out` will contain the word $YES$. The following line will contain the value of the last element in the spiral. If the spiral does not form an arithmetic progression, the first line of the output file `spirala.out` will contain the word $NO$. The following line will contain two natural numbers, representing the first two numbers in the given array for which the arithmetic progression property is not met.

## Constraints

$2 \leq nrlin \leq 100$

$-32000 \leq tablou_{i,j} \leq 32000$ 

(i = 1, 2, $\dots$, $nrcol$, j = 1, 2, $\dots$, $nrlin$)

## Examples

`spirala.in`
```
3 3
1 3 5
15 17 7
13 11 9
```

`spirala.out`
```
YES
17
```

`spirala.in`
```
2 3
-1 -3 -5
-15 -5 -7
```

`spirala.out`
```
NO
-7 -5
```