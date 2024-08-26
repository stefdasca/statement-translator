## Objectives

In a peculiar city, there are $N$ intersections and $M$ one-way streets between these intersections. This means that from one intersection to another where there is a street, travel can only be done in one of the two possible directions. By closely analyzing the city's street map, the local police have concluded that from some intersections, it is impossible to reach other intersections by traveling only in the direction allowed by the streets. The city hall wants to build a new train station and a museum that will attract numerous tourists. The locations for the buildings will be in two different intersections. Due to the street system, things are complicated because it is possible that tourists who arrive at the train station cannot reach the intersection where the museum is located, for example, by taking a taxi. Therefore, the police will have to change the direction of some streets to make this possible. The company that will build both the museum and the train station provides $T$ offers specifying the location of both constructions. For each offer, the city hall must identify the minimum number of streets whose direction needs to be changed so that tourists can travel from the train station to the museum.

## Input data

The input data is read from the file `obiective.in`. The first line of the file contains two natural numbers, $N$ and $M$, the number of intersections and the number of one-way streets between these intersections. Each of the following $M$ lines contains a pair of natural numbers $(u, v)$, indicating that there is a street oriented from $u$ to $v$. After the street system description, the number of offers, $T$, follows. Each of the next $T$ lines, up to the end of the file, describes an offer. An offer consists of the indices of two intersections, the first index representing the intersection where the train station will be built and the second the intersection where the museum will be built.

## Output data

The output data is printed in the file `obiective.out`. On the $i$th line of this file contains the minimum number of streets that need to be reoriented to ensure there is at least one road from the train station to the museum, according to the placement of these buildings from the $i$th offer in the input file.

## Constraints and clarifications

$4 \leq N \leq 32\ 000$  
$5 \leq M \leq 64\ 000$  
$1 \leq T \leq 100\ 000$

For the initial orientation of the streets, it is guaranteed that however we choose 3 intersections $A$, $B$, $C$, such that we can reach from $A$ to $C$ and from $B$ to $C$, then we can reach either from $A$ to $B$, or from $B$ to $A$ (possibly both). If the orientation of the streets is ignored, it is possible to reach from any intersection to any other. Between any two intersections, there is at most one street.

## Example

`obiective.in`
```
5 6
1 3
2 1
3 2
2 4
4 5
3 4
3
4 3
5 1
2 0
```

`obiective.out`
```
1
1
2
```

## Explanation

For the second offer, we can redirect the streets $4 \to 5$ and $2 \to 4$ to make it possible to travel from intersection $5$ to intersection $1$.