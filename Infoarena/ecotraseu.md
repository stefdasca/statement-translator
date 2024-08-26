## Ecopath

In the old town center of Copenhagen, cars do not circulate. Therefore, tour companies park their hop-on hop-off buses near the intersections at the edge. The city is modeled so that between any two intersections there is a unique simple path. The intersections at the extreme of a single street are bus stops, while those connecting multiple streets are tourist attractions. Each street in Copenhagen has an associated advantage. For example, on streets with negative advantages, young people from nonprofit organizations are strategically positioned to seek donations, while on streets with positive advantages, there are shops with almost free beer. The sum of the advantages of the streets forming a path is the advantage of that path. A simple path with advantage $0$, with distinct bus stops at the ends, is called an ecopath. Tourism companies know that there is an ecopath in the city, but they would like to find its endpoints so they can park the buses there.

## Input data

The first line of the input file `ecotraseu.in` contains the number $T$ of tests. Each test then begins on a new line. The first line of a test contains the number $N$ of intersections. The following lines contain triplets of numbers separated by spaces, where each triplet of the form $x$ $y$ $a$ represents the two intersections $x$ and $y$, followed by the advantage of the street $a$. The file ends with an end-of-line character.

## Output data

The output file `ecotraseu.out` contains $T$ lines, each with two numbers separated by space, indicating the endpoints of an ecopath for a given test. The file ends with an end-of-line character.

## Constraints and clarifications

$1 \leq x$, $y \leq N \leq 10^5$

$\|a\| \leq 10^4$

$1 \leq T \leq 20$

At most 10 tests have $1 \leq N \leq 10^4$

At most 10 tests have $10^4 \leq N \leq 10^5$

## Example

`ecotraseu.in`
```
2
2
1 2 0
3
1 2 -1
1 3 1
1
```

`ecotraseu.out`
```
1 2
2 3
```

## Explanation

There are two tests. In the first test, the path $1 - 2$ is an ecopath. In the second test, the path $2 - 1 - 3$ is an ecopath.