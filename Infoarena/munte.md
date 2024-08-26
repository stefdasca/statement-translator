# Mountain

Gheorghe wants to conquer a mountain. He has certain information about the mountain. He knows how tall the mountain is and what the distance is to the other side of the mountain. He also has a list of special points he must pass through, knowing their heights and the order in which they appear; he does not know the distance between these points. The mountain consists of 3 types of terrain. Type 1: ascending terrain, where the mountain rises by one meter vertically for each meter horizontally. Type 2: flat terrain. In this section, the terrain neither rises nor falls. Type 3: descending terrain, where the mountain falls by one meter vertically for each meter horizontally.

## Task

Given all this information, $N$ (the maximum height of the mountain, assuming the mountain starts at level $0$ and ends at level $0$), $D$ - the horizontal distance of the mountain, and the height at each special point, Gheorghe wants to know how many possible ways there are to traverse the mountain.

## Input data

The first line of the file `munte.in` will contain the number $N$ - the maximum height of the mountain, $D$ - the horizontal distance of the mountain, and $K$ - the number of special points. The next $K$ lines contain the heights of the special points.

## Output data

The first line of the file `munte.out` will contain $P$ - the number of possible ways to traverse the mountain. Gheorghe starts at level $0$ and must finish at level $0$. Only the start and end have the level $0$.

## Constraints and clarifications

$1 \leq N \leq 50$

$1 \leq D \leq 100$

$0 \leq K \leq 50$

$0 \leq P \leq 2^{63} - 1$

## Examples

`munte.in`
```
2 5 0
```
`munte.out`
```
3
```

### Explanations

The 3 different possibilities are: not a valid traversal because the mountain's height is not 2, but 1.

`munte.in`
```
2 5 2
2
2
```
`munte.out`
```
1
```

### Explanations

The only possible traversal is the one above.

`munte.in`
```
3 8 4
2
2
3
1
```
`munte.out`
```
7
```