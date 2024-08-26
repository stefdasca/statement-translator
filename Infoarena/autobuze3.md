## Task

Summer has arrived, and bus drivers are ecstatic because many people will go on vacation using their buses. The country they live in consists of $N$ cities connected by $M$ high-speed highways, of a kind seen only in Romania. And because they are very similar to those in Romania, each highway has a toll that you have to pay if you want to travel on it. There are two types of operations:
1. Drive $b$ $x$ $y$ - Bus $b$ moves from city $x$ to city $y$, provided that bus $b$ is in city $x$, there is at least one driver in it, and there is a highway built between cities $x$ and $y$. The cost of the operation is the highway toll.
2. Move $s$ $x$ $y$ - Driver $s$ moves from bus $x$ to bus $y$, provided that driver $s$ is in bus $x$ and buses $x$ and $y$ are in the same city. The cost of the operation is $0$. A city can have any number of buses and any bus can accommodate all $N$ drivers. Initially, driver $i$ is in bus $i$, in city $i$. Because the drivers want to devise a plan to earn as much money as possible this summer, they need to gather in a single bus to discuss. Since they don't want to pay too much, they ask you to tell them the minimum cost for all drivers to reach a single bus and a sequence of operations (1 and 2) so that all drivers end up in the same bus at the minimum cost mentioned above. Additionally, no driver should change buses more than 25 times.

## Input data

The input file `autobuze3.in` contains the following:
- The first line contains an integer $T$, representing the number of tests.
- The first line of each test contains two integers $N$ and $M$, representing the number of cities and the number of highways, respectively.
- The following $M$ lines each contain three integers $x$, $y$, and $c$, signifying that there is a highway between cities $x$ and $y$ with a toll $c$.

## Output data

The output file `autobuze3.out` will contain the answers for the $T$ tests:
- The first line of each test contains an integer $C_{min}$, representing the minimum cost for all drivers to reach a single bus.
- The following lines will display the operations, one per line. At the end of the operations, you will print the word `Gata` on a new line.

## Constraints and clarifications

For all evaluation tests:
$T = 10$ 
$1 \leq N \leq 2 \* 10^5$ 
$1 \leq M \leq 4 \* 10^5$ 
$0 \leq \text{highway toll} \leq 10^9$ 
$C_{min} \leq 2 \* 10^9$ 

The graph is connected!

## Example

`autobuze3.in` 
```
2 
3 3 
1 2 1 
1 3 1 
2 3 2 
4 5 
1 2 1 
1 3 1 
2 3 2 
2 4 1 
3 4 2 
```

`autobuze3.out` 
```
2 
Drive 2 2 1 
Drive 3 3 1 
Move 2 2 1 
Move 3 3 1 
Gata 
3 
Drive 4 4 2 
Drive 3 3 1 
Move 4 4 2 
Drive 2 2 1 
Move 2 2 1 
Move 4 2 1 
Move 3 3 1 
Gata 
```

## Explanation

In the first test, drivers 2 and 3 go to city 1 at a total cost of 2.

In the second test, the drivers gather in city 1. Driver 4 goes to city 2, moves to bus 2 and then goes together with driver 2 to city 1. Driver 3 goes to city 1. The total cost is $1 + 1 + 1 = 3$.