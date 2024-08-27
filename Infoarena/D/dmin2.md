# Dmin2

To get to her grandmother's house, Little Red Riding Hood needs to cross the Bright Forest. In the forest, there are $N$ clearings (for simplicity, we will consider that initially Little Red Riding Hood is in clearing $1$ and her grandmother's house is in clearing $N$). The clearings are connected by $M$ paths, and Little Red Riding Hood can only move along the paths and through the clearings (otherwise, she will be eaten by the Big Bad Wolf). We know that no matter which path the girl chooses, she will visit at least $4$ clearings to reach her grandmother's house (including clearings $1$ and $N$). To help Little Red Riding Hood not get lost, the Brave Forester wants to arrange as many new paths through the forest as possible, but he wants to build the paths in such a way that whatever route the girl chooses, she visits at least $4$ clearings. Help the forester create a maximum number of new paths so that by walking through the forest, Little Red Riding Hood visits at least $4$ clearings. 

## Input data

The input file `dmin2.in` contains the first line two natural numbers $N$ and $M$ with the significance from the statement. Each of the next $M$ lines will contain a pair of numbers $x$ and $y$ with the significance that there is a path between clearing $x$ and clearing $y$.

## Output data

In the output file `dmin2.out`, write the maximum number of paths the forester can arrange!

## Constraints

$1 \leq N \leq 100000$

$1 \leq M \leq 300000$

We will consider that two paths will intersect only in a clearing. 

Between any two clearings, there will be at most one path. 

We know that Little Red Riding Hood can reach her grandmother's house using the initial $M$ paths.

## Example

`dmin2.in`
```
5 3
1 2
2 3
3 5
```

`dmin2.out`
```
3
```

## Explanation

The forester will arrange paths between $2$ and $4$, $3$ and $4$, and $4$ and $5$.