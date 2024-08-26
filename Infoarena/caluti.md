Chernel's Ponies

Farmer Chernel has a big problem. He needs to transport $N$ ponies from the pasture to the barn. For this, he uses a truck that can carry at most $K$ ponies per trip. The time it takes for Chernel to make a trip from the pasture to the barn and back to the pasture with an empty truck is $P$. However, the frolicsome ponies are hard to convince to get into the truck before a certain time. For each pony $i$, the time $T_i$ is known, after which it can be loaded into the truck. Chernel wishes to finish his work as quickly as possible, in other words, he wants to minimize the time after which all ponies have been transported to the barn and he has returned to the pasture with the truck.

## Task

Help Chernel accomplish his difficult task of transporting all the ponies in minimum time.

## Input data

The first line of the input file `caluti.in` contains a natural number $T$, representing the number of tests. The following lines describe the $T$ tests, each having the following format: the first line contains three integers $N$, $K$, and $P$, and in the following $N$ lines contains the times $T_i$ of the ponies, sorted in ascending order.

## Output data

The output file `caluti.out` will contain $T$ lines. The $i$-th line will contain a single integer, representing the minimum transport time of the ponies corresponding to the $i$-th test in the input file.

## Constraints

$1 \leq T \leq 10$  
$1 \leq K \leq N \leq 100000$  
$1 \leq P \leq 10000000000$  
$1 \leq T_i \leq 10000000000$

For 40% of the tests $N \leq 500$

## Example

`caluti.in`  
```
1
3
2
15
10
20
30
45
```

`caluti.out`  
```
1
30
45
```

## Explanation

Chernel loads the first pony at time $10$, transports it to the barn, and returns to the pasture at time $25$. He waits until $30$, then loads the second and third ponies, transports them to the barn, and returns to the pasture at time $45$.