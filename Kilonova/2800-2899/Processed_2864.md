
Ali-Baba and his $N$ thieves discovered a treasure map on an isolated island. The map can be thought of as a grid of $L \times C$ regions ($L$ rows and $C$ columns). In each region, there is a magical chest that contains rubies ($0$ or more), and the number of rubies in each chest is kept in the corresponding element of the grid.

The following action plan is established:
- A thief can move from one region to another neighboring region (a region can have up to $8$ neighboring regions);
- Each thief starts from a certain region, with given coordinates, and moves towards the region where Ali-Baba is (the bottom-right corner region, with coordinates $L$ and $C$), following the shortest path (the length of a path is equal to the number of regions crossed);
- When passing through a region, the thief puts the existing rubies from the chest into a bag;
- If there are multiple shortest paths, a thief will choose the one that allows him to collect as many rubies as possible;
- The first thief to move is the one with the order number $1$, followed by the thief with the order number $2$, $3$, and so on. During the movement of one thief, the others remain in place until he reaches Ali-Baba;
- Since the chest is magical, new identical rubies appear in place of the ones taken by the thief, with the appearance happening before each thief leaves his starting point towards Ali-Baba.

Each thief has gathered a number of rubies in his bag, known only to him, and arrives with the bag in Ali-Baba's region. When division of the rubies occurs, Sindbad the Sailor also appears, wanting a part of the bags. Knowing certain relationships that exist between pairs of thieves in the region, Ali-Baba will have to choose those relationships that imply the distribution of a minimal number of bags to Sindbad.

It is known that choosing a pair of thieves $(i,j)$ implies the distribution of thief $j$'s bag because of $i$ into Ali-Baba's treasure, but from this moment on, no pair of the form $(j,k)$ can be used anymore, as thief $j$ is eliminated.

# Task
Help Ali-Baba choose the order of pairs so that the remaining bags are as few as possible, knowing that those remain with Sindbad.

# Input data
The input file `rubine.in` contains:
- The first line contains the grid dimensions: the values of $L$ and $C$ separated by a space;
- The next $L$ lines contain $C$ values separated by spaces, representing the number of rubies in the chest found in the respective region;
- The next line contains $N$, the number of thieves;
- The next $N$ lines contain the coordinates of the regions (values separated by a space) where the thieves are initially found: the first line among them for thief one, the second line for thief two, etc.;
- On the following lines, until the end of the file, are the pairs representing the relationships in the problem.

# Output data
The output will be in the file `rubine.out` in the following format:
- The first line contains the number $T$ of pairs used by Ali-Baba, meeting the requirements of the problem;
- The next $T$ lines contain four values separated two by two by a space: $i \ {nr}_1 \ j \ {nr}_2$, where $i$ represents the first value in the pair (the thief with the order number $i$), ${nr}_1$ represents the number of rubies collected by thief $i$, $j$ represents the second thief in the pair (the thief with the order number $j$), ${nr}_2$ representing the number of rubies collected by thief $j$;
- The next line contains the order numbers of the thieves whose bags remained with Sindbad, values separated two by two by a space;
- The last line contains the sum of the rubies in the bags remaining with Sindbad.

# Constraints and clarifications
- $1 \le L,C,N \le 50$
- $0 \le A[i][j] \le 200$
- There are always solutions, and if there are multiple, one will be chosen.
- In each region, whether it is the starting point of a thief or the region where Ali-Baba is, there is a chest with a certain number of rubies. Ali-Baba does not know the number of rubies in each bag.
- There are no two thieves initially in the same region.

# Example
`rubine.in`
```
4 5
1 0 0 0 0
0 1 0 0 0
0 0 1 4 0
0 0 0 1 5
5
1 1
1 5
4 1
2 2
4 4
1 2
1 4
2 5
3 1
4 5
```
`rubine.out`
```
4
2 9 5 6
1 12 2 9
1 12 4 11
3 10 1 12
3
10
```
