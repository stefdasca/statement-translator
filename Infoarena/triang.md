# Triang

Andreea learned at school what an equilateral triangle is. Fascinated by these geometric figures, she draws $N$ points with real number coordinates on a plane. However, she does not realize how many equilateral triangles she has drawn, so she asks for your help!

## Input data

The first line of the file `triang.in` contains the number $N$ of points. The next $N$ lines contain the coordinates of the $N$ points in the form $( x \; y )$. 

## Output data

The first line of the file `triang.out` will contain the number of equilateral triangles drawn by Andreea. 

## Constraints and clarifications

$3 \leq N \leq 1\ 500$  
$-10\ 000 \leq x, y \leq 10\ 000$  
There will not be two points with identical coordinates, and any point can be used to form multiple equilateral triangles. A triangle is equilateral if it has all angles and sides equal. If you use real numbers in your program, it is recommended to use `double` types for C/C++, and Pascal respectively. For testing the equality of two real numbers, it is recommended to use a precision of $10^{-3}$ 

## Example

`triang.in`  
$3$  
$0 \; 0$  
$4 \; 0$  
$2 \; 3.4641016$

`triang.out`  
$1$