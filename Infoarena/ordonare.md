# Sorting

Petrică, bored with socializing and trees, decided to find a new hobby: cleaning. He found a rather peculiar room (extremely long, but very narrow, so narrow that it can be represented as the $Ox$ axis). He found $n$ objects in the room, located at various coordinates on the $Ox$ axis. However, some of these objects were at identical coordinates, a situation intolerable given Petrică’s new obsession. Thus, he decided to move the objects so that they are all at distinct coordinates. To move an object by $+1$ or $-1$ on the $Ox$ axis, Petrică needs one second. He wants to find the minimum time (in seconds) required to organize the room according to his criterion. The time needed for Petrică to move between $2$ objects without moving them is negligible.

## Task

## Input data

The input file `ordonare.in` contains on the first line $n$, the number of objects, and on the second line $n$ integers $x(i)$, representing the coordinates of the objects.

## Output data

The output file `ordonare.out` contains a single number, the minimum time required by Petrică.

## Constraints

$n \leq 250000$ 

$-1000000000 \leq x(i) \leq 1000000000$ 

The tests are grouped!

Each of the following test sets represents a group.

The rest of the tests (those that do not meet other conditions than the initial ones) are also grouped.

For $5$ points,

$n \leq 5$ 

$-3 \leq x(i) \leq 3$ (test $1$)

For another $10$ points,

$n \leq 50$ 

$-30 \leq x(i) \leq 30$ (test $2$)

For another $10$ points,

$n \leq 100$ 

$-50 \leq x(i) \leq 50$ (test $3$)

For another $10$ points,

$n \leq 5000$ 

$-1000 \leq x(i) \leq 1000$ (tests $4$, $5$)

For another $20$ points,

$n \leq 5000$ (tests $6$, $7$, $8$)

Objects can be moved to coordinates smaller than $-1000000000$ or larger than $1000000000$ to obtain the optimal solution!

## Example

`ordonare.in`  
$5$  
$1 \ 2 \ 2 \ 3 \ 4$  

`ordonare.out`  
$2$

`ordonare.in`  
$2$  
$-1 \ -2$  

`ordonare.out`  
$0$

`ordonare.in`  
$4$  
$4 \ 4 \ 3 \ 1$  

`ordonare.out$  
$1$

## Explanation

In the first example, Petrică moves the object from coordinate $1$ to coordinate $0$ and one of the objects from coordinate $2$ to coordinate $1$, taking him a total of $2$ seconds.

In the second example, although it seems more complicated because the numbers are negative, Petrică doesn’t need to do anything since the objects are already at distinct coordinates.

In the third example, Petrică moves one of the objects from coordinate $4$ to coordinate $5$.