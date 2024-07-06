> The blue lake of the woods  
> Yellow water lilies load it;  
> Trembling in white circles  
> It shakes a boat.  
> Mihai Eminescu, The Lake

# Task

GrandPaPà, the ancient and legendary guardian of the lake in the Emineian poem "The Lake," discovered one morning $k$ square yellow water lilies on the water's surface. The water surface can be encoded as a matrix of $n$ rows and $m$ columns.

The water lily with identifier $i$ ($1 \le i \le K$), side length $lat$ and corners in regions $(l_i,c_i)$, $(l_i,c_i+lat-1)$, $(l_i+lat-1,c_i)$ and $(l_i+lat-1,c_i+lat-1)$ will cover the entire corresponding submatrix with the value $i$. It is guaranteed that no two water lilies overlap, but two water lilies can touch edges.

If a region is not covered by any water lily, then the corresponding element in the matrix will have a value of $0$.

This problem has multiple tasks. Depending on the task number $C$ ($1 \le c \le 3$), you will need to display:

* If $c=1$, display $3$ numbers, `lmax`, `number` and `id` &mdash; the maximum side length of a water lily, the number of water lilies with the maximum side length, and the minimum identifier of a water lily with the maximum side length, respectively.
* If $c=2$, GrandPaPà will take $Q$ photos of the lake, the $i$-th photo including the submatrix with top-left and bottom-right corners in regions $(l_{1_i},c_{1_i})$, respectively $(l_{2_i},c_{2_i})$. For each photo, display the number of water lilies included **completely** in the photographed submatrix.
* If $c=3$, similar to task $2$, GrandPaPà will take $Q$ photos of the lake. For each photo, display the number of water lilies included **partially or completely** in the photographed submatrix.

# Input data

The input file `lacul.in` will contain:

On the first line, it will contain the task number $c$ ($1 \le c \le 3$).

On the second line, it will contain three numbers $n$, $m$ and $k$ ($1 \le n,m \le 100$, $1 \le k \le n \cdot m$) &mdash; the dimensions of the matrix and the number of water lilies, respectively.

On each of the following $n$ lines, it will contain $m$ numbers, the elements of the matrix ($0 \le a_{i,j} \le k$).

If $c=2$ or $c=3$, on the $n+3$-rd line of the input file, it will contain $q$ ($1 \le q \le 100\ 000$) &mdash; the number of photos.

On the next $q$ lines, it will contain the coordinates of the corners from the top-left and bottom-right of the photos
($1 \le l_1 \le l_2 \le n$, $1 \le c_1 \le c_2 \le m$).

# Output data

If $c=1$, display in the output file `lacul.out` $3$ numbers: the maximum side length of a water lily, the number of water lilies with the maximum side length, and the minimum identifier of a water lily with the maximum side length.

If $c=2$, print for each of the $q$ photos from the input file the number of water lilies included **completely** in the photographed submatrix.

If $c=3$, print for each of the $q$ photos from the input file the number of water lilies included **partially or completely** in the photographed submatrix.

# Constraints and clarifications

- For 20 points, $c=1$;
- For 40 points, $c=2$;
- For the remaining 40 points, $c=3$.
- For 10 points for each of the tasks $c=2$ and $c=3$, all water lilies have a side length of $1$;
- For 20 points for each of the tasks $c=2$ and $c=3$, $k \le 100$;

# Example 1

`lacul.in`

```
1
9 10 7
0 0 0 0 1 1 0 0 0 0
2 2 0 0 1 1 7 7 7 7
2 2 0 0 0 0 7 7 7 7
0 4 4 4 3 0 7 7 7 7
0 4 4 4 0 0 7 7 7 7
0 4 4 4 5 5 5 5 6 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
```

`lacul.out`
```
4 2 5
```

## Explanation 

For the first example, there are $2$ water lilies with the maximum side length $lmax=4$. These have identifiers $5$ and $7$, of which $5$ is the smallest.

# Example 2

`lacul.in`

```
2
9 10 7
0 0 0 0 1 1 0 0 0 0
2 2 0 0 1 1 7 7 7 7
2 2 0 0 0 0 7 7 7 7
0 4 4 4 3 0 7 7 7 7
0 4 4 4 0 0 7 7 7 7
0 4 4 4 5 5 5 5 6 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
4
1 1 9 10
2 1 5 9
5 4 6 9
1 2 8 8
```

`lacul.out`
```
7
2
1
3
```

## Explanation

For examples $2$ and $3$, the four photos capture the following submatrices:

~[submatrici.png|width=70%|align=center]

- All $k=7$ water lilies are included completely in the first photo.
- The water lilies with identifiers $2$ and $3$ are included completely in the second photo.
- The water lily $6$ is the only water lily included completely in the third photo.
- The water lilies $1$, $3$ and $4$ are included completely in the fourth photo.

# Example 3

`lacul.in`

```
3
9 10 7
0 0 0 0 1 1 0 0 0 0
2 2 0 0 1 1 7 7 7 7
2 2 0 0 0 0 7 7 7 7
0 4 4 4 3 0 7 7 7 7
0 4 4 4 0 0 7 7 7 7
0 4 4 4 5 5 5 5 6 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
0 0 0 0 5 5 5 5 0 0
4
1 1 9 10
2 1 5 9
5 4 6 9
1 2 8 8
```

`lacul.out`
```
7
5
4
6
```

## Explanation

- All $k=7$ water lilies are included completely in the first photo.
- The water lilies with identifiers $2$ and $3$ are included completely in the second photo. The water lilies with identifiers $1$, $4$ and $7$ are included only partially.
- The water lily $6$ is the only water lily included completely in the third photo. The water lilies $4$, $5$ and $7$ are included only partially.
- The water lilies $1$, $3$ and $4$ are included completely in the fourth photo. The water lilies $2$, $5$ and $7$ are included only partially.