# Circles 2

Adriana has concluded that the disk is an interesting figure, even more so when it is formed from $M$ concentric $K$-numeric circles. A circle is $K$-numeric if along its contour, there are $3 \cdot K$ numbers with the property that there exists at least one choice of positions $x$, $y$, $z$ (on this circle) such that the following relationship holds: $a(x) + a(x+1) + \dots + a(y-1) = a(y) + a(y+1) + \dots + a(z-1) = a(z) + a(z+1) + \dots + a(x-1) = R$ and moreover $|x-y| = |y-z| = |z-x| = K$ ($a(i)$ is the $(x+i)$-th number on the circle).

## Task

Adriana asks you to count all disks with all the above properties, for a given $R$ and $M$.

## Input data

The first line of the file `cercuri2.in` will contain $R$ and $M$.

## Output data

The first line of the file `cercuri2.out` will contain the required number, taken modulo $666013$.

## Constraints and clarifications

$M \cdot (M-1) / 2 < R$  
$R < 20001$  
$a(x) > a(x+1) > \dots > a(y-1)$  
$a(y) > a(y+1) > \dots > a(z-1)$  
$a(z) > a(z+1) > \dots > a(x-1)$

Obviously, the first circle of the disk is $M$-numeric, the second circle is $(M-1)$-numeric, $\dots$, the last circle is $1$-numeric.

All the numbers on the circles are strictly positive natural numbers.

## Examples

`cercuri2.in`
```
9 3
```

`cercuri2.out`
```
1728
```