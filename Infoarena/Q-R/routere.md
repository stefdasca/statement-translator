## Task

Mihai, upon arriving at the Aneraofni headquarters for a new workday, was convinced by the big boss of the organization to renovate the headquarters. The Aneraofni headquarters has the shape of a ring with $N$ rooms -- room $1$ is connected to rooms $N$ and $2$, room $2$ is connected to rooms $1$ and $3$, and so on. The essential part of the renovation consists of placing routers in the rooms of the headquarters. Routers can have various coverage radii. More precisely, all routers will have a non-zero natural quality $R$, chosen by Mihai, and will be able to cover a range of $R$ consecutive rooms. Due to the fragility of the electrical system in the Aneraofni headquarters, no two routers can cover the same interval. The renovation plan, which comes from the big boss of the organization, specifies that each room requires a signal from a certain number of routers. Mihai wonders: "In how many ways can I choose the quality of the routers, and in how many ways can I choose in which rooms to place them, such that the big boss's plan is satisfied?"

## Input data

The input file `routere.in` will contain, on the first line, the number $N$. The second line will contain the number of routers each room needs a signal from, in order.

## Output data

The output file `routere.out` will contain the required number, printed modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 1000$ 

$R < N$ 

$0 \leq number\ of\ routers\ each\ room\ needs\ a\ signal\ from \leq N$ 

For tests worth $21$ points, $N \leq 20$. 

For tests worth $39$ points, $N \leq 100$. 

Be careful! Just like in real life, the big boss can ask for something impossible.

## Example

Input file `routere.in`:
```
3 
1 1 1
```

Output file `routere.out`:
```
1
```

Input file `routere.in`:
```
5 
0 1 2 1 0
```

Output file `routere.out`:
```
1
```

Input file `routere.in`:
```
6 
1 2 2 1 1 1
```

Output file `routere.out`:
```
2
```

Input file `routere.in`:
```
3
0 0 0
```

Output file `routere.out`:
```
2
```

Input file `routere.in`:
```
20 
5 5 5 5 5 6 6 6 6 7 7 7 7 7 7 6 6 6 6 5
```

Output file `routere.out`:
```
59
```

## Explanation

In the first example, we choose $R = 1$ and place a router in each room.

In the second example, we choose $R = 2$ and place a router on the intervals $[2, 3]$ and $[3, 4]$.

In the third example, we choose $R = 2$ and place a router on the intervals $[1, 2]$, $[2, 3]$, $[3, 4]$, $[5, 6]$, or we choose $R = 4$ and place a router on the intervals $[2, 5]$, $[6, 3]$ (the interval $[6, 3]$ starts in room $6$ and continues in rooms $1$, $2$, and $3$).

In the penultimate example, we choose $R = 1$ or $R = 2$, and we do not place any router.