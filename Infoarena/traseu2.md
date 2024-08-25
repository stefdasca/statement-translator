# Traseu2

We are given a rectangular matrix of size $N \times M$ containing distinct natural numbers or the character '#'. Find a path in the matrix that starts from the smallest element and traverses all elements in increasing order. Two consecutive elements in the path must be neighbors in the matrix (considering that an element in the matrix can have up to 8 neighbors).

## Input data

The input file `traseu2.in` contains on the first line the natural numbers $N$ and $M$ with the meaning from the statement. On the next $N$ lines, there will be $M$ elements that represent the description of the matrix. The elements will be either distinct natural numbers or the character "#". All elements are separated by spaces.

## Output data

The output file `traseu2.out` will contain the message "Nu exista solutie!" (without quotes) if there is no path with the required property, or the message "Exista solutie!" (also without quotes), followed by the description of the required path. The path description consists of printing on the second line of the output file a number $NR$, representing the number of elements in the path, and on the next $NR$ lines, triples of the form $x, y, z$ with the meaning that such a triple on line $i$ is the $i-2$th element in the path, the element being at coordinates $x, y$ in the matrix and having the value $z$.

## Constraints and clarifications

$1 \leq N, M \leq 70$  
The elements in the matrix are positive numbers less than $10^9$

## Example

`traseu2.in`
```
2 2 
1 3 
2 10
```

`traseu2.out`
```
Exista solutie! 
4 
1 1 1 
2 1 2 
1 2 3 
2 2 10
```

`traseu2.in`
```
3 1 
1 
# 
2
```

`traseu2.out`
```
Nu exista solutie!
```