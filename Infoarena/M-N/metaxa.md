## Metaxa

Gigel is a professional alcoholic, who consumes the magical serum, also known as Metaxa (having very refined tastes), daily in industrial quantities. He lives in a humble house with an extraordinarily large yard. His yard contains some fences in the form of convex polygons. These can also intersect, as the fences were mounted while Gigel was under the influence of the divine elixir, thus forming smaller convex polygons. Gigel, having spent all his money on buying his favorite drink, ran out of funds to beautify his home. So, to "decorate" his garden, he considered it a Cartesian reference $XOY$ and placed the Metaxa bottle caps at integer coordinate points, including on fences if necessary (you can imagine how much free time Gigel has). One day, Gigel ran out of drink, and out of sadness he began to ask existential questions. One of the questions that went unanswered, because Gigel no longer knows how to count, is: What is the intersection among his fences that contains the most Metaxa caps? Gigel, longing for an answer to this question, asks you to find this intersection, telling him how many caps there are within it.

## Task

Display the maximum number of Metaxa caps contained in an intersection of at least $2$ polygons.

## Input data

The input data is read from the file `metaxa.in`. The first line contains a number $T$ representing the number of tests in the input. For each test, an initial number $N$ is read, representing the number of fences. For each fence, a number $A_i$ is read, representing the number of vertices of polygon $i$, and after $A_i$ pairs of coordinates $(x_v , y_v)$ marking each vertex of the polygon. The vertices are read in a counterclockwise direction.

## Output data

The output data is displayed in the file `metaxa.out`. On each line, for each test, the maximum number of Metaxa caps found in an intersection is printed.

## Constraints and clarifications

$1 \leq T \leq 23$

$1 \leq N \leq 23$

$3 \leq A_i \leq 23$

$-1\,000\,000 \leq x_v , y_v \leq 1\,000\,000$

For precision, it is guaranteed that the vertices of the fences and the places where they intersect are at lattice points.

If there is no intersection, the answer $0$ is displayed. Polygons can have common sides but since the vertices are integers, then this side in their intersection will obviously have whole vertices. 

## Example

`metaxa.in`

```
2
4
4 1 1 4 1 4 4 1 4
4 2 3 5 3 5 5 2 5
4 16 11 18 11 18 13 16 13
4 17 12 19 12 19 14 17 14
2
3 1 0 3 0 2 1
3 1 0 2 -1 3 0
```

`metaxa.out`

```
6
3
```