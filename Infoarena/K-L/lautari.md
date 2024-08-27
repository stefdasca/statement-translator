## Task

Bossanip and Dicsi are going to one of the coolest parties in the kingdom. Bossanip cares deeply for his friend Dicsi, so he plans to surprise him on the night of the party. He knows that in front of the club where the party will be held, Dicsi's favorite musicians will be present, and he decides to pay them a considerable amount (Bossanip never looks at the money) to dedicate a song to his friend. Since we are talking about a world with evolved cultural standards, each musician will come to the party with their own musical instrument (represented by a positive natural $number$). Additionally, it is possible that two or more musicians will use the same type of instrument. Having known the musicians for a very long time, Bossanip knows the order in which they will arrive on the night of the party. He also knows exactly what kind of dedications Dicsi likes: not too simple, but not too complex either. Thus, a dedication must use at least $P$ and at most $Q$ types of different musical instruments. Dicsi doesn't mind if some instruments are used multiple times throughout a dedication. At the same time, within a dedication, the musicians must form a compact interval. Formally, if musicians with order $number$ $i$ and $j$ with $j \gt i$ are chosen for a dedication, then all musicians with order $index$ $k$, where $i \lt k \lt j$, must also be chosen. Taking all this information into consideration, Bossanip wants to choose a $subarray$ of musicians for his friend that meets the given requirements (don't forget, the $subarray$ must be to Dicsi's liking!). For this, he comes to you and asks: how many ways does he have to choose the band of musicians? Two ways are considered distinct if and only if the set of chosen musicians (the set of positions) is different.

## Input data

The input file `lautari.in` contains on the first line 3 natural $numbers$ $N$, $P$, $Q$. On the second line, it will contain the types of musical instruments used by musicians, in the order in which they arrive at the party (each musical instrument is assigned a natural $number$, and two instruments are of the same type if they are assigned equal $numbers$), separated by a space.

## Output data

The output file `lautari.out` will contain a single value, namely the total number of valid sequences.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq P \leq Q \leq N$

The values of the musical instruments are non-zero natural values less than or equal to $100\ 000$

For tests worth $10$ points $N \leq 200$

For tests worth $30$ points $N \leq 5\ 000$

## Example

`lautari.in`

`
5 2 3
1 3 3 2 3
`

`lautari.out`

`
9
`

`lautari.in`

`
3 1 1
1 1 1
`

`lautari.out`

`
6
`

## Explanation

The valid $subarrays$ for the first $example$ are:

`
1 3
1 3 3
1 3 3 2
3 3
3 3 2
3 2
3 2 3
2 3
`

The valid $subarrays$ for the second $example$ are:

`
1
1
1
1 1
1 1 1
`