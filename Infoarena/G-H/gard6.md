## Task

Tanaka, a resident of the village of Şuieb, was surprised to find that $N$ adjacent blocks of equal width and varying non-negative heights were built overnight in front of his house. Since these blocks obstructed his view of the picturesque landscape, he decided to build a fence so that he could no longer see the blocks. Tanaka will build the fence using $K$ rectangular planks. A plank is considered to cover a subarray of consecutive blocks if it has a height greater than or equal to the height of all blocks in the subarray and a width equal to the number of blocks in the sequence. Wanting to save money, Tanaka wants to know the minimum total area of wood required to cover all the blocks with $K$ planks.

## Input data

The first line of the `gard6.in` file will contain $N$ and $K$. The second line will contain the heights of the blocks, from left to right.

## Output data

The single line of the `gard6.out` file will contain the minimum required area.

## Constraints
1 $\leq$ $K$ $\leq$ $N$ $\leq$ $100\ 000$  
$N * K$ $\leq$ $250\ 000$  
The heights of the blocks do not exceed $1\ 000\ 000\ 000$ (Şuieb is still just a village; it doesn't have tall buildings).  
Blocks of height $0$ must also be covered by planks, possibly of height $0$.  
The interiors of the planks cannot intersect.  
For $19$ points, $N^2 * K$ $\leq$ $1\ 000\ 000$  
For another $32$ points, $N * K$ $\leq$ $75\ 000$ and the heights of the blocks do not exceed $20$.  
For another $24$ points, $N * K$ $\leq$ $75\ 000$ and the sequence of values is randomly generated.  
For another $10$ points, $N * K$ $\leq$ $150\ 000$.

## Example

`gard6.in`  
```
4 2  
1 2 3 4
```
`gard6.out`  
```
12
```

`gard6.in`  
```
5 2  
2 4 0 2 4
```
`gard6.out`  
```
18
```

`gard6.in`  
```
10 3  
910 884 805 589 529 436 427 291 46 13
```
`gard6.out`  
```
5767
```

## Explanation

In the first example, the total area of $12$ units can be achieved with a plank of width $2$ units and height $2$, followed by a plank of width $2$ units and height $4$.

In the second example, the total area of $18$ units can be achieved with a plank of width $1$ unit and height $2$ units, followed by a plank of width $4$ units and height $4$ units.