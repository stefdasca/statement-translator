## Task

On the surface of Romania, there are $K$ radio stations positioned at different coordinates and altitudes. Each of these stations has a certain transmission radius, which is the maximum distance it can send a radio signal. The government wants to place a radio antenna somewhere on the map, such that it receives signals from all $K$ radio stations (i.e., the distance to each radio station is less than or equal to the transmission radius of the respective station). The map of Romania can be viewed as a matrix with $M$ rows and $N$ columns, where the value at row $i$ and column $j$ represents the altitude of that area. The side length of a square in the matrix is $1$. All $K$ radio stations are placed in distinct areas on the map and at the altitude corresponding to the area where they are placed. In addition, they are positioned exactly at the center of the area (in the center of the respective square in the matrix). The radio antenna can be positioned at the center of any area that does not have a radio station, at the same altitude as that area or at a higher altitude (but necessarily an integer number). Determine how many possible placements exist for the radio antenna. If the antenna can be placed in the center of the area at row $i$ and column $j$ at altitudes $h_1$ and $h_2$ (with $h_1 \ne h_2$), these are considered two different possibilities.

## Input data

The first line of the input file `radio.in` contains $3$ integers, separated by a space: $M$, $N$, and $K$. $M$ and $N$ represent the number of rows and columns of the map, and $K$ represents the number of radio stations. The next $M$ lines contain $N$ integers each, representing the altitudes of the respective areas on the map. After this, $K$ lines follow, each containing $3$ numbers, separated by a space: $i$, $j$, and $R$. $i$ and $j$ represent the row and column of the area where a radio station is placed, and $R$ represents the transmission radius of the respective station. $i$ and $j$ are integers, and $R$ is a real number.

## Output data

In the output file `radio.out` you will print the total number of possible placements for the radio antenna on the map.

## Constraints and clarifications

$1 \leq M, N \leq 50$  
$1 \leq K \leq \min{M \times N - 1, 1000}$  
$0 \leq \text{altitude of any area} \leq 32\ 000$  
There will not be $2$ radio stations placed in the same area on the map.  
When calculating distances, note that they are distances in a $3D$ space.

## Example

`radio.in`  
```
5 5 3  
1 2 3 4 5  
6 7 8 9 10  
1 2 3 4 5  
6 7 8 9 10  
5 4 3 2 1  
1 1 4.3  
5 5 4.3  
5 1 4.3
```

`radio.out`  
```
4
```

## Explanation

The radio antenna can be placed in the area at row $3$ and column $2$, at the same height as that of the area or at a height $1$ higher. Also, the radio antenna can be placed in the area at row $3$ and column $3$, at the same height as that of the area or at a height $1$ higher.