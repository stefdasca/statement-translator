# Hero's Call: Northrend!

"By order of his royal highness, King Varian Wrynn, all able-bodied citizens of the Alliance are to report to Recruitment Officer Blythe at Valiance Keep in Borean Tundra. The Valiance Expedition needs your help to keep the forces of the Scourge under control and safeguard civilized lands! Make your way to the Stormwind Docks and take the ship north to Valiance Keep. For the glory and honor of the Alliance!"

Rewards

You will receive: 50 - 100 points of experience (if completed within 2.5 hours)

It is time for one of the last heroes of Azeroth, named Leeroy Jenkins, to answer King Varian Wrynn's call to battle against the army led by the Lich King. In Azeroth, there are $N$ cities numbered from $1$ to $N$, connected by exactly $N - 1$ "bidirectional" portals. Portal $i$ will take our hero Leeroy from city $A[i]$ to city $B[i]$, if he pays a fee of $C[i]$ silver coins, or vice versa (from city $B[i]$ to $A[i]$, for the same fee). It is guaranteed that there is a way to travel between any two cities. As can be seen, his mission is to reach the city $Valiance\ Keep$, numbered $X$, to speak to Officer Blythe. Leeroy would prefer not to spend too much on his way to this city, as he needs a considerable amount of coins to buy a new, more powerful weapon. Therefore, when leaving a city, Leeroy ensures at each step to access the cheapest portal (the portal having the lowest cost) connected to the city he is in and leading to a city not yet visited. Knowing that Leeroy is allowed to leave from any city different from $Valiance\ Keep$ (city $X$), display how many paths leading Leeroy to $Valiance\ Keep$ (city $X$) exist.

## Input data

The input file `northrend.in` contains on the first line the natural numbers $N$ $X$, separated by a space. On each line $i$ of the next $N - 1$, there will be 3 natural numbers $A[i]$ $B[i]$ $C[i]$, with the following meaning: there is a portal connecting city $A[i]$ to city $B[i]$, having cost $C[i]$.

## Output data

The output file `northrend.out` will contain a single natural number, representing the number of paths leading Leeroy to $Valiance\ Keep$ (city $X$).

## Constraints and clarifications

$1 \leq N \leq 100\,000$ \
$1 \leq X \leq N$ \
$1 \leq C \leq 10^9$

It is guaranteed that no two portals have the same cost.

## Example

`northrend.in`
4 4
1 2 2
2 3 1
2 4 3

`northrend.out`
0

`northrend.in`
5 3
1 2 1
2 3 2
3 4 3
2 5 4

`northrend.out`
2

## Explanation

For the first example:
1. If Leeroy leaves from city $1$, he will traverse the cities $1 \rightarrow 2 \rightarrow 3$, stopping in city $3$.
2. If Leeroy leaves from city $2$, he will traverse the cities $2 \rightarrow 3$, stopping in city $3$.
3. If Leeroy leaves from city $3$, he will traverse the cities $3 \rightarrow 2 \rightarrow 1$, stopping in city $1$.

Therefore, the number of paths leading him to city $4$ is $0$ (zero).

For the second example:
Leeroy can reach city $3$ if he leaves from city $1$ or city $4$.