## Task

Given a binary matrix (elements are $0$ or $1$) with $M$ rows and $N$ columns. A black component is a subset of elements with value $1$, with the property that it is possible to reach any element of the component from any other element of the component, directly or through other elements of the component, by moving in horizontal and/or vertical directions (thus, from one element you can go directly to one of the maximum $4$ neighboring elements around it). A black component is called compact if it does not contain any white element inside it (more precisely, if there is a cycle formed by part of the component elements, moving only in horizontal and vertical directions, which contains a white element inside, then the component is NOT compact). The size of a black component is equal to the number of elements it consists of. The depth of a black component is defined as $1 +$ the number of black components inside which it is included. Determine the total number of black components, the size of the largest black component, the total number of compact black components, and the size of the largest compact black component. Also, determine the maximum depth of a black component.

## Input data

The first line of the input file `bmap.in` contains two integers, separated by a space: $M$ and $N$. The following $M$ lines contain $N$ characters from the set $\{'0','1'\}$, not separated by spaces ($'0'$ $=$ white element, $'1'$ $=$ black element).

## Output data

The first line of the output file `bmap.out` will contain $2$ integers, separated by a space: the total number of black components and the size of the largest black component.

The second line will contain another $2$ integers, separated by a space: the number of compact black components and the size of the largest compact black component.

The third line will contain the maximum depth of a black component.

## Constraints and clarifications

$1 \leq M \leq 10000$

$1 \leq N \leq 1000$

If there is no compact black component, the size of the largest compact black component is considered to be $0$.

If there is no black component, the size of the largest black component is considered to be $0$ (as well as the maximum depth).

## Example

`bmap.in`
```
10 20
00001111111000011110
11110111101111010111
01110000111111001111
11111110000000001111
10000111111111010000
10111011111111011111
10101011111111010001
10111010001001010001
10000010111111010001
11111110001111010001
```

`bmap.out`
```
5 65
2 16
2
```

## Explanation

The binary matrix from the example is illustrated in the figure below. It is observed that there are $5$ black components (numbered from $1$ to $5$), of which components $1$, $2$, and $3$ are NOT compact. Component $4$ is compact because it does not contain any white squares inside. The largest black component has a size of $65$ (component $3$), and the largest compact black component has a size of $16$ (component $4$). Component $2$ has a depth of $2$ (being included in component $3$), while the other components have a depth of $1$.