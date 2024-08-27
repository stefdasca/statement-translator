## Task

After travelling across seas and lands to find the meaning of life, a group of pirates returns disappointed to their homeland. Once back in the village where they grew up, each goes to their houses to rest and drown their sorrows in a glass of rum. At some point, in the middle of the night, the royal army is heard from afar. Scared they might get caught, our pirates think they need to leave the village and seek refuge as quickly as possible. Knowing it might take a long time to find a new shelter and each of them needing a certain (quite large, we might add) amount of rum to survive, they realize that before heading to one of the village exits, each of them needs to stop at one of the houses with rum reserves to resupply. Being under the influence of the traditional drink, not only do they fail to figure out the optimal route to the exit, but they can’t even distinguish all the roads in the village or how long they are (they even think some might have negative lengths). In real danger, the pirates ask for your help and, in return, they will offer you a bottle of rum (which is phenomenal because pirates are not known for their generosity, especially when it comes to their favorite drink). They offer you the following information to provide the best response: the number of houses in the village, the number of roads the pirates managed to distinguish, the roads themselves with "source house, target house, distance” format, the number of pirates, the number of houses from which they can resupply, the number of houses from which they can leave the village, the indices of the houses where the pirates are, the indices of the houses from which they can resupply, and the indices of the houses from which they can exit. The pirates await you to tell them, for each one of them, the minimum path so that they can resupply and then reach one of the exits. If the minimum path is less than $-10^{18}$ (the smallest number a pirate can count to), they ask you to display "-INF" (without quotes), and if a pirate has no valid path, they ask you to display "INF" (without quotes).

## Input data

The input file `peapesimaitulburi.in` contains on the first line the numbers $n$ and $m$, representing the number of houses and the number of roads offered by the pirates. The next $m$ lines each contain a triplet of the form $x$ $y$ $d$ with the significance that there is a road from house $x$ to house $y$ of distance $d$. The next six lines contain the number $p$, representing the number of pirates, $p$ numbers separated by spaces, representing the indices of the houses where each pirate is, the number $a$, representing the number of houses from which they can resupply, $a$ numbers separated by spaces, representing the indices of these houses, the number $i$, representing the number of houses from which they can exit the village, and $i$ numbers separated by spaces representing their indices.

## Output data

The output file `peapesimaitulburi.out` will display on $p$ lines the answers for each pirate. Line $i$ will contain the answer for pirate $i$.

## Constraints

1 \leq $n$ \leq 100000

1 \leq $m$ \leq 200000

1 \leq $x$ \leq $n$

1 \leq $y$ \leq $n$

-100000 \leq $d$ \leq 100000

1 \leq $p$ \leq $n$

1 \leq $a$ \leq $n$

1 \leq $i$ \leq $n$

All indices in the input are valid (within the range [1, $n$]).

If there is a road from house $u$ to house $v$, there is NO guarantee there is also a road from house $v$ to house $u$.

It is guaranteed that there is NO road from any house to itself.

It is guaranteed that there is NO more than one direct road between any two houses.

If there exists a road ($x$, $y$, $d$) with more than 2500 pairs of houses ($u$, $v$) having the property that one can reach both from house $u$ to house $v$ and from house $v$ to house $u$ passing through that road, since it means a lot of pirates know it, the chance that they made a mistake in its length is 0%. In other words, the length of this road is a natural number (not necessarily strictly positive).

You are strictly prohibited from attempting to steal a pirate's rum. Otherwise, the end could be tragic!

## Example

`peapesimaitulburi.in`

```
8 9
1 2 1
2 3 2
3 1 -3
2 4 6
4 5 -1
5 4 -2
3 6 -3
6 7 1
6 8 2
8
1 2 3 4 5 6 7 8
1
3
3
4 7 8
```

`peapesimaitulburi.out`

```
-INF
-INF
-INF
INF
INF
INF
INF
INF
```

`peapesimaitulburi.in`

```
8 9
1 2 1
2 3 2
3 1 -3
2 4 6
4 5 -1
5 4 -2
3 6 -3
6 7 1
6 8 2
8
1 2 3 4 5 6 7 8
1
6
3
4 7 8
```

`peapesimaitulburi.out`

```
1
0
-2
INF
INF
1
INF
INF
```