## Task

Once upon a time in the land of King Red, there lived Harap-Alb and Ileana Cosanzeana who, being in love, met very often despite living in different cities. Initially, everything was perfect, since Harap-Alb was a clever young man and knew how to choose the shortest path to Ileana's house using the algorithms learned in college. However, the situation changed when King Red decided to tax the passage through the cities with a number of gold coins. Thus, Harap-Alb realized that his personal budget was not always enough if he used the shortest path to reach Ileana Cosanzeana. Knowing that Harap-Alb perfectly knows the map of the kingdom given by $N$ - the number of cities, and $M$ - the number of direct roads between cities that can be traveled in both directions, and having the budget available to Harap-Alb for traveling, $B$, help him discover how he can get to the city where Ileana Cosanzeana lives, $t$, knowing that at the beginning Harap-Alb is in the city $s$. Because he wants to see Ileana as soon as possible, Harap-Alb prefers to use the shortest route for which he has the necessary budget to pay the transport taxes in each city he passes through (excluding the source, but including the destination). If there are multiple such paths, he will obviously prefer the cheapest path because it leaves him more money to go out in the city with his girlfriend.

## Input data

The input file `drum-bugetat.in` contains:  
the first line contains three integers: $N$ - the number of cities, $M$ - the number of direct roads between cities, and $B$ - the number of gold coins that Harap-Alb has available.  
the second line contains another two integers: $s$ - the city where Harap-Alb is, and $t$ - the city where Ileana Cosanzeana is.  
the next line contains $N$ integers which represent the transit costs (the number of gold coins that need to be paid) through the $N$ cities (the first city appears first, city $N$ is last).  
the following $M$ lines each contain 3 numbers: the first two represent the cities between which there is this direct road, and the third is the length of that road.

## Output data

In the output file `drum-bugetat.out`, write a line that contains two integers separated by a space:  
the length of the shortest path that Harap-Alb can use  
the number of gold coins Harap-Alb spends to choose that path

## Constraints

$0 \leq N \leq 1000$  
$0 \leq M \leq 10000$  
$0 \leq B \leq 1000$  
the length of a direct road between 2 adjacent cities: $0 \dots 1000$  
the tax for passing through a city: $0 \dots B$

Observations  
In the input file, the cities are numbered from $1$ to $N$.  
If there is no path, print "$-1$" (without quotes).

## Example

`drum-bugetat.in`
```
7 9 4  
1 7  
0 1 2 10 1 3 0  
1 2 1  
1 3 3  
2 4 1  
2 5 5  
3 5 1  
3 6 2  
4 7 1  
5 7 5  
6 7 2  
```

`drum-bugetat.out`
```
9 3
```