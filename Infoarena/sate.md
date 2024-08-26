# Villages

In a picturesque country, in a mountainous county, there are $N$ collinear villages numbered with natural numbers from $1$ to $N$. The villages are placed in order, from left to right, according to the numbers that identify them. Thus, village $1$ is the farthest to the left, while village $N$ is the farthest to the right. There are exactly $M$ pairs of villages for which the distance is known (expressed in kilometers). Based on this information, you need to determine the distance between villages $X$ and $Y$, if possible.

## Input data

The first line of the file `sate.in` contains $N$, $M$, $X$ and $Y$, where $N$ is the number of villages and $M$ is the number of relationships of the aforementioned form. Each of the next $M$ lines contains a triplet $(i, j, D)$, meaning that the distance between villages $i$ and $j$ $(i < j)$ is $D$ kilometers.

## Output data

The output file `sate.out` contains a single value indicating the determined distance between villages $X$ and $Y$.

## Constraints

$1 \leq N \leq 30\ 000$

$1 \leq M \leq 100\ 024$

For at least $45\%$ of the tests, $N \leq 300$

The given relationships are not contradictory

It is guaranteed that the distance between villages $X$ and $Y$ is uniquely determined by the given relationships

The distance between any two villages is a natural number expressed in kilometers

It is guaranteed that the distance between villages $1$ and $N$ does not exceed $20$ million

The distance between $X$ and $Y$ can always be determined based on the given information

## Example

`sate.in`
```
11 7 1 11
1 7 10
4 6 4
5 7 4
6 8 5
2 10 15
4 11 13
5 8 8
```

`sate.out`
```
18
```