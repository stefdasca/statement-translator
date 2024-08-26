## Cupa Berii

Gigel is trying to lead a healthy life and has started jogging; he participates in many competitions each year, but of course, his favorite race is the Beer Cup. The Beer Cup takes place on a road of length $N$ Km. The road is straight, starting at position $0$ and ending at position $N$. The road has one lane in each direction. There are $M \leq 4 \cdot N$ beer brands sponsoring the race, and each brand has a zone where it offers beer to the participants. For each brand, the interval $x,y$ where that brand offers beer is given (if $x<y$ then the stand is on the direction from left to right, otherwise the stand is on the direction right to left). Multiple stands can overlap in the same interval. The Beer Cup is not like any other competition; the participants must drink a beer at each KM where there is a beer stand, and they can choose the type of beer they will drink if there are multiple options. However, participants do not have to necessarily cover the entire route $(0 \to N \to 0)$. They can start from any position $P1$ (a natural number) and must move RIGHT to another position $P2 > P1$ (a natural number), covering the route $P1 \to P2$. They are, however, required to make the return trip, namely $P2 \to P1$. Gigel wants to participate in the Beer Cup but has one slightly special request. He wants to drink the maximum number of beers from at least one brand of beer and wants to do this either at the beginning of the route $(P1 \to \dots )$ or immediately after returning $(\leftarrow P2)$. Gigel asks for your help and wants to know in how many ways he can choose his route. (Analyze the example for clarifications) The Beer Cup takes place on $T \leq 10$ distinct routes.

## Task

For each of the $T$ routes calculate the number of possibilities Gigel has to choose his route.

## Input data

The first line of the `drumuri.in` file contains the number $T$, followed by $T$ tests. Each test starts with a line containing $N$ and $M$, as described in the statement. The next $M$ lines contain three numbers $x_i, y_i$.

## Output data

The file must contain $T$ lines, on line $i$ the answer for the $i$-th route.

## Constraints

$1 \leq T \leq 10$  
$1 \leq N \leq 100\,000$  
$1 \leq M \leq 400\,000$  
For each stand $x \neq y$  
The stands will be fully included on the road.  
The Beer Cup normally takes place on a circuit and you must drink a beer at the beginning of each lap of the circuit $\dots$  
The Beer Cup 2015 has not been announced yet $\dots$

## Example

`cupaberii.in`  
```
2
4 4
1 3
2 4
3 4
4 1
10 1
1 9
```

`cupaberii.out`  
```
5
2
```

## Explanation

For the first route, Gigel has the following options:  
$0 - 4$ (drinks on the return the type $4$ of beer $4 \to 1$)  
$1 - 3$ (drinks on the way type $1$ of beer)  
$1 - 4$ (drinks on the way type $1$)  
$2 - 4$ (drinks on the way type $2$)  
$3 - 4$ (drinks on the way type $3$)  

For the second route, Gigel has $2$ options:  
$1 - 9$  
$1 - 10$ (type $1$ $\dots$)  

Gigel cannot start at position $0$ because he must drink all beers of one type at the beginning. He cannot go $9 \to 0$ because the beer stand is on the left to right direction.