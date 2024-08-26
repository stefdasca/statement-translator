# Circle2

A photon was placed at time $0$ at the coordinates $(R, 0)$, inside a circle with the center at coordinates $(0, 0)$ and a radius of $R$ meters. The photon moves towards the point $(R\cos(\alpha), R\sin(\alpha))$ at a speed of $1$ meter per second (it is a very lazy photon). When it hits that point, the photon is reflected according to the usual rules of light reflection (see the figure below) and continues its journey inside the circle, changing direction each time it touches the contour of the circle. Determine the distance from the center of the circle to the location of the photon after exactly $S$ seconds from the start of its infinite journey. 

## Input data

The first line of the input file `circle2.in` contains the number of tests $T$. The following lines describe the $T$ tests. Each test consists of a line containing $3$ numbers: an integer $R$, a real number $\alpha$, and an integer $S$. 

## Output data

For each test, print in the output file `circle2.out` one line containing the distance between the point where the photon is located after $S$ seconds and the center of the circle. An error of $0.001$ is acceptable. 

## Constraints and clarifications

$1 \leq T \leq 560\ 000$  
$1 \leq R \leq 1000$  
$0 < \alpha \leq 180$  
$0 \leq S \leq 1\ 000\ 000\ 000$  

The angle $\alpha$ is expressed in degrees (not radians) and is given with at most $5$ decimal places. 

## Example

`circle2.in`  
`5`  
`10 135 10`  
`10 135 20`  
`10 135 40`  
`5 45 0`  
`5 45 45`  

`circle2.out`  
`3.902`  
`8.613`  
`7.281`  
`5.000`  
`4.725`