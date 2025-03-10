
> Ernő Szöollösi still approves this message.
> --- Ion Durduroiu, Dialogues of Power

Spring 2003. In Rytan, war has become a habit. The Zachodists are on a campaign to recapture certain territories currently under terrorist control. To stop the conflict in the city of Sprengjuaras, the support of Romanian forces was requested. The Romanian army sent its best-prepared unit to the battlefront: "The Red Deer", led by General Oliver Kipeläinien. Their task was to hinder terrorist actions until the Zachodist reinforcements arrived.

~[ernoszollosi.jpg|align=center|width=30%]
$$
\text{The Great Terror}
$$

Upon arriving at the location, Oliver Kipeläinien consulted the city map. It consisted of $N$ key strategic points and $M$ connecting roads to facilitate the transport of armaments. Due to the sandy terrain, armored vehicles could only traverse the roads in one direction, namely downhill. Thus, General Oliver Kipeläinien noticed the territory's resemblance to a **directed acyclic graph**.

The Romanians' goal was to keep the terrorists under control by reducing their area of influence while maintaining the same city traversal possibilities. The plan was simple: block certain roads by detonation and keep others, so that if it was initially possible to get from strategic point $X$ to strategic point $Y$, after removing the roads, transportation from $X$ to $Y$ would still be achievable.

Each road had an associated "cost", representing the amount of fuel needed to cross it. Sometimes, a lower-cost road significantly reduced traversal speed compared to a more costly road. However, Oliver Kipeläinien presented the unit with the plan to keep certain roads operational the next day, leaving the others to be blocked. His ingenuity proved to be of real use, recording zero Romanian casualties. The Zachodists took control of the city. In the country, the press praised the heroic acts of the general and his unit.

~[nasiriyah3.jpg|align=center|width=30%]
$$
\text{and the Operation of the Polish}
$$

Today, General Oliver Kipeläinien is running for presidential elections. Digging into his past, a team of journalists discovers the true face of the events at Sprengjuaras. Asking for a viewpoint from the Zachodists under whose command Oliver Kipeläinien was, they discover what the general's plan actually was: Oliver Kipeläinien chose exactly the roads with the minimum total cost to reduce the gasoline consumption and divert resources to the sound system to spend as much time partying in the tank, avoiding conflict until reinforcements arrived. The general's image is tarnished, and he loses the elections to his political enemy, Pătrățel.

# Task

You are part of the journalist team. Find out which roads Oliver Kipeläinien actually chose and what the minimum total fuel cost is.

# Input data

The first line of the input will contain two numbers, $N$ and $M$. This is followed by $M$ lines, each describing a road through $x_i$, $y_i$, and $c_i$, representing a road from point $x_i$ to $y_i$ whose cost is $c_i$.

# Output data

A single number will be printed, namely the minimum possible cost of roads in a plan that maintains the initial accessibility relations of the map.

# Constraints and clarifications

* $1 \le N \le M \le 50\ 000$;
* $1 \le x_i, y_i \le N$;
* $1 \le c_i \le 10^6$.

|#| Points | Constraints |
|-|---------|------------|
|1|    8    | $M \le 19$ |
|2|   12    | There is a chain of length $N$ |
|3|   12    | $M \le 80$ |
|4|   18    | $M \le 500$ |
|5|   20    | $M \le 5\ 000$ |
|6|   30    | No additional restrictions |

# Example

`stdin`
```
7 11
1 2 7
2 7 11
1 6 5
6 2 5
1 3 9
3 6 3
3 7 2
6 4 7
4 7 10
2 5 3
5 7 6
```

`stdout`
```
43
```

## Explanation

The roads chosen by Oliver Kipeläinien are the ones with indices $4$, $5$, $6$, $8$, $9$, $10$, and $11$.
