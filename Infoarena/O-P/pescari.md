```markdown
Fishermen

In the territory of the village of Ştiucleni, there live $P$ fishermen and there is a number of lakes known only to the locals. They each have a coded map in the form of a rectangular matrix of dimensions $N$ x $M$ where the fishermen's houses are represented by the digit 1, portions of land covered by water are represented by the digit 2, and land between houses and ponds by the digit 0. Everyone knows that a good fisherman wakes up early in the morning to catch the best fishing spot on the pond. Thus, before the start of a new fishing season, every fisherman tries to devise a strategy to get to the pond as quickly as possible to catch the spot where the fish bite best. The strategy consists of finding the length of the road to the nearest pond. The length of a road is measured by the number of lands a fisherman has to cross, knowing that he can move from his position in all 8 possible directions. The fisherman can also pass through the yards of other fishermen, meaning he does not have to go around other houses.

## Task

Given a map of the village of Ştiucleni, you are asked to help each fisherman find the length of the road from his house to the nearest pond.

## Input data

The input file `pescari.in` will contain on the first line three integers $N$, $M$, and $P$ with the meaning described in the statement. The next $N$ lines will contain $M$ digits separated by a space, representing the coding of a portion of land.

## Output data

The output file `pescari.out` will contain $P$ lines. The $i^{th}$ line will contain an integer representing the length of the road from fisherman $i$ to the nearest pond. The fishermen are ordered by the row on which their house is found on the map, and in the case of a tie, by the column.

## Constraints and clarifications

$3 \leq N$, 
$M \leq 1000$

$1 \leq P \leq 10,000$ 

$P \leq (N x M) / 2$

The number of portions of land covered by water will not exceed 10,000.

The number of portions of land covered by water will not exceed $(N x M) / 2$.

One or more portions of land covered by water adjacent to each other form a pond.

There will always be at least one pond.

A house occupies a single portion of land.

Multiple adjacent digits 1 represent multiple houses.

For 10% of the tests $N$, $M = 3$.

For another 10% of the tests, there will be a single fisherman and a single portion of land covered by water.

## Example

`pescari.in`
```
10 10 6
0 0 0 0 0 1 0 0 0 0
0 0 2 2 2 0 0 0 0 0
0 0 0 2 2 2 0 0 1 0
0 0 0 2 2 2 2 0 0 0
0 0 0 2 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 2 2 0 0 0 0 0 1
0 2 0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0 0 0
```

`pescari.out`
```
3
2
1
3
5
```
```