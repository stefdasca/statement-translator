## Task

In a garage, there are $N$ trucks, and at the garage door, $M$ bottles of natural grape juice are waiting to be transported to the shelter. Each truck $i$ has a maximum capacity $C_i$, which represents the maximum number of bottles that can be in the truck at any given time, and a time $T_i$ minutes to travel the distance from the garage to the shelter (so to go from the garage to the shelter and back to the garage it will travel $2 \cdot T_i$ minutes). The garage owner, Samson, wants to transport all the bottles to the shelter. He will choose certain trucks to use for transport, and each chosen truck will make as many trips garage $\rightarrow$ shelter $\rightarrow$ garage as needed to transport all the bottles (the trucks must always return to the garage to complete the transport successfully). He wants to minimize the maximum time in which a truck travels, in other words, he wants to finish transporting all the bottles in minimal time. After finding this minimal time, he also wants to use a minimal number of trucks from the garage to achieve that minimal time.

## Input data

The input file `garaj.in` contains the natural numbers $N$ and $M$ on the first line, with the meanings given in the statement. On the next $N$ lines, there follows a pair of natural numbers $C$ $T$ representing the maximum capacity and the time in which a truck covers the distance garage $\rightarrow$ shelter.

## Output data

The output file `garaj.out` contains on the first line two natural numbers $T_{min}$ and $Nr_{min}$, the minimal time in which the transport is completed and the minimal number of trucks that need to be used.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 10^9$

$1 \leq C, T \leq 1000$

All the numbers in the input file are natural numbers.

## Example

`garaj.in`
```
3 16
5 3
6 2
4 1
```

`garaj.out`
```
6 2
```

## Explanation

One possible solution is as follows: truck 2 makes one trip carrying 6 bottles to the shelter, and truck 3 makes 3 trips, carrying 4 bottles on the first and second trips and 2 bottles on the last trip. The second truck travels for 4 minutes, and the third truck for 6 minutes, so after 6 minutes, all the bottles have been transported. Another solution to achieve the minimal time of 6 would be to use all 3 trucks for transport, but that would not use a minimal number of trucks.