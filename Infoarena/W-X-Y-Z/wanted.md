## Task

After some of you helped Gigel escape from jail by solving the gather problem, the police are now on his trail. There are $N$ cities, and it is known that Gigel is hiding in one of them. We have an infinite road which, for simplicity, will be considered identical to the $Ox$ axis of a Cartesian coordinate system. For each city $i$, the coordinates ( $X_i$ , $Y_i$ ) are known. Each city has a path parallel to the $Oy$ axis which connects it to the main road. Policeman Eduard is currently at the coordinates ( $0$ , $0$ ) and can go to any city using the main road and the respective paths. When he arrives in a city, he will ask the inhabitants about Gigel. They will tell him whether Gigel is in that city, or whether he is in a city with a larger or smaller $X$ coordinate. Help Eduard by telling him the minimum distance he has to travel in the worst-case scenario by choosing an optimal strategy to visit the cities.

## Input data

The input file `wanted.in` contains on the first line $N$, the number of cities. 
The next $N$ lines contain two integers $X_i$, $Y_i$ representing the coordinates of the cities.

## Output data

The output file `wanted.out` will contain the required distance.

## Constraints and clarifications

$1 \leq N \leq 200$

$-10\ 000 \leq X_i \leq 10\ 000$

$0 \leq Y_i \leq 10\ 000$

No two cities will have the same $X$ coordinates.

The result will not be greater than $2\ 000\ 000\ 000$.

## Example

`wanted.in`

```
4
-10 3
-5 2
5 4
8 2
```

`wanted.out`

```
32
```

## Explanation

Eduard goes to city $2$.

If he is told that Gigel is in a city with a smaller $X$ coordinate, he will go to city $1$ where he will find Gigel. In this case, the cost will be $5+2=7$ to reach city $2$ and $2+5+3$ to reach city $1$, totaling $17$.

Otherwise, he will go to city $3$, from where, if he does not find Gigel, he has to go to city $4$. The total cost in this case will be $32$.