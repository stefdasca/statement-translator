## Task

The Federal Republic of Serbanistan was separated from its Southern neighbor, the Federal Republic of Popanistan, by a wall. This wall is divided into $Z$ adjacent sections and has only one guard, initially located at section $1$. The wall was erected to prevent immigrants from Popanistan from entering Serbanistan illegally, but over time, the situation in Serbanistan deteriorated, so now the wall's role is to keep its own citizens inside the country. Today, $N$ of these citizens want to escape by climbing over the wall. For each of the $N$ citizens, the time needed to climb the wall is known: the $i$-th citizen needs $time[i]$ seconds to jump over the wall. At each moment in time, at most one citizen will attempt to scale the wall. They will choose one of the $Z$ sections of the wall to do so. When a citizen starts climbing, the guard will head towards them at a speed of one wall section per second. If the citizen finishes climbing before the guard reaches the respective section, the citizen escapes and the guard stops moving, remaining in place. If the guard reaches the section exactly in the last second of the citizen's climb, the citizen still manages to escape. You need to find an escape order for the citizens and the section of the wall each citizen will climb so that the maximum number of them can successfully escape.

## Input data

The input file `wall.in` will contain on its first line the values $N$ and $Z$, representing the number of citizens who want to escape from Serbanistan, respectively the number of sections of the wall. The next $N$ lines will contain, the $i$-th line containing the number of seconds required for the $i$-th citizen to scale the wall. 

## Output data

The output file `wall.out` will contain on its first line the value $MAX$, representing the maximum number of citizens who can successfully escape. The next $N$ lines will contain two values each: the index of the citizen who will be sent to escape at that time (in the order given in the input file), and the section of the wall they will climb. For your solution to be correct, the sequence of indices must form a permutation, and each displayed section must be within the interval $\left[1 \dots Z\right]$. Of course, by following this strategy exactly $MAX$ citizens must successfully escape. If there are multiple correct solutions, any of them will be accepted. Note that all $N$ escapees must attempt to jump the wall at some point, regardless of the outcome of this attempt.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq Z \leq 100\ 000$

$1 \leq time[i] \leq 100\ 000$ 

## Example

`wall.in` 
```
3
5
1
1
2
```

`wall.out` 
```
3
1 5
2 5
3 5
```

`wall.in` 
```
3
5
4
4
3
```

`wall.out` 
```
3
1 5
2 1
3 5
```

## Explanation

In example $1$, the wall is long enough for all citizens to jump over it through section $5$ without being caught by the guard. After citizen $1$ passes, the guard will be in section $2$. After citizen $2$ passes, the guard will be in section $3$, and after citizen $3$ passes, the guard would be in section $5$. We notice that even though the guard reached section $5$ in the last second of citizen $3$'s climb, the latter successfully escaped. If the guard had arrived one second earlier, things would have been different. 

In example $2$, citizen $1$ will climb the wall on section $5$ and will succeed in escaping, at which point the guard will be in the same section. Citizen $2$ will cross the wall at section $1$, and the guard will turn back to catch them but will not succeed. When citizen $3$ starts climbing section $5$, the guard will be in section $1$ and will head towards section $5$ again, failing once more to catch the climbing citizen.