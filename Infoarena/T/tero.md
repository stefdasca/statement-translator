# Tero

After successfully fulfilling all his duties as mayor, Dubluveu is elected President of Romania. At his first meeting with the Romanian Intelligence Service (SRI), he is informed of an imminent terrorist attack. Fortunately, SRI knows the terrorists' plans. According to the report, the wrongdoers intend to attack the Capital and the Port City on the Black Sea. Romania has $N$ cities numbered from $1$ to $N$, connected by $M$ bidirectional roads of different lengths. The Capital is numbered $1$, and the Port City is numbered $N$. A proposed solution by the head of SRI is that all roads between the targeted objectives should be guarded by the $S$ soldiers of the army. Thus, the President could order the placement of soldiers on a road, as close as possible to one of the bordering cities, but not in the cities (to avoid panic). Being a person who thinks deeply about the situation, Dubluveu posed the following problem: If the terrorists manage to attack one of the target cities, the soldiers should be mobilized as quickly as possible to the attacked city. Fortunately, all soldiers have a constant speed of $1m/s$, and the time required to mobilize a soldier is equal to the maximum distance to the two cities. Unfortunately, the plan must first be theoretically prepared, and since time is very short, an experienced programmer will be needed to accomplish this.

## Task

The Presidency has tasked you with implementing the plan against the terrorists. Therefore, you need to find an arrangement of the $S$ soldiers such that any road from $1$ to $N$ is guarded, soldiers are not placed in the city, and their total mobilization time is minimal.

## Input data

The first line of the input file `tero.in` will contain $3$ numbers $N$, $M$, and $S$ with the meanings provided in the statement. The following $M$ lines will contain three integers $i$, $j$ and `dist`, indicating that there is a road of length `dist` between city $i$ and city $j$.

## Output data

The output file `tero.out` will contain, on a single line, a real number with exactly one decimal place, representing the minimum mobilization time.

## Constraints

$1 \leq N \leq 700$  
$1 \leq M \leq 131072$  
$1 \leq S \leq M$  
The number of soldiers is large enough to block all roads from $1$ to $N$  
Any number of soldiers can be placed on a road  
The length of a road does not exceed $100000$

Scoring will be given based on the absolute difference between your answer and the committee's answer:  
$10$ points/test if the difference $\leq 0.1$  
$5$ points/test if $0.1 < difference \leq 34.5$  
$3$ points/test if $34.5 < difference \leq 69$  
$1$ point/test if $69 < difference \leq 103.5$  
$0$ points/test if the difference is $> 103.5$

## Example

`tero.in`  
```
5 6 3
1 2 2
1 3 1
1 4 1
3 4 3
2 5 1
4 5 2
```

`tero.out`  
```
1.5
```

## Explanation

If the first soldier is placed on the edge from $1$ to $2$, at a distance of $1.5$ from $1$ and $0.5$ from $2$, then the distance from $1$ to the soldier is $1.5$, and the distance from $5$ to the soldier is also $1.5$. The maximum among the distances is $1.5$. If the other soldiers are placed on the edge from $4$ to $5$, at a distance of $1.5$ from $5$ and respectively $0.5$ from $4$, the distance from $1$ to the soldiers is $1.5$ and the distance from $5$ is also $1.5$. The maximum among distances is $1.5$. This is the minimum mobilization, as any other arrangement would result in a higher value.