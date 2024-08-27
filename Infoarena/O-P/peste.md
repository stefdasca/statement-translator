## Task

Titus goes fishing on the banks of the Bahlui river, where he plans to stay for $T_{Total}$ minutes. He possesses $N$ fishing nets, and each net $i$ can catch $P_{i}$ fish if it is left in the water for at least $T_{i}$ minutes. If a net $i$ is left in the water for more than $T_{i}$ minutes, it will not catch more fish, and if it is left for less than $T_{i}$ minutes, it will not catch any fish at all. Additionally, no more than $K$ fishing nets can be in the water at any given time. Thus, Titus starts fishing at time $0$ (zero) and can perform one of the following actions at any time:
- Introduce a fishing net into the water, as long as there are not already $K$ fishing nets in the water and the net he wants to introduce is not already in the water
- Remove a net from the water and collect the fish in it, but only if all the nets that are in the water have finished catching fish (otherwise the fish will be scared away and he will not catch anything)

We consider that both actions are performed instantaneously (do not consume any unit of time), so at any given time Titus can perform either of the two actions multiple times. Determine the maximum number of fish Titus can catch in $T_{Total}$ minutes.

## Input data

The input file `peste.in` contains on the first line, separated by a space, the natural numbers $N$, $K$, and $T_{Total}$, having the meaning given in the statement. On the next $N$ lines, there is information about the fishing nets, on the $i+1$ line are $P_{i}$ and $T_{i}$, representing the information for net $i$.

## Output data

The output file `peste.out` contains on the first line the natural number $Res$, representing the maximum number of fish that Titus can catch in $T_{Total}$ minutes.

## Constraints

$1 \leq K$  
$1 \leq N$  
$1 \leq T_{Total} \leq 50000$  
$1 \leq P_{i}$  
$1 \leq T_{i} \leq 1000$

## Example

`peste.in`  
```
3 2 5
10 5
2 4
1 3
```

`peste.out`  
```
12
```

## Explanation

One possible solution is the following: at time $0$ introduce the first net, at time $1$ introduce the second net, at time $5$ both nets have finished catching fish, so he can first remove the first net, collect the fish from it, then do the same for the second net (recall that these actions are performed instantaneously), catching a total of $12$ fish.