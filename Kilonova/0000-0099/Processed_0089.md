Petrom Company has `n` gas stations located along the Sun Highway. The gas stations are numbered from `1` to `n` in the order of their placement on the highway.

The positions of the gas stations are known, being specified by the distances $d_1, d_2, \ldots, d_n$ ($d_i$ represents the distance from Petrom's headquarters to gas station `i`). Petrom's headquarters is located at the entrance of the Sun Highway.

In `k` of these gas stations, the company wants to set up fuel depots, which will supply the respective gas station and other neighboring gas stations. Each gas station will be supplied by the nearest depot.

The transportation cost for a given depot placement will be equal to the sum of the distances from each gas station to the depot from which it is supplied.

# Task
Write a program to determine the gas stations where depots should be built, so that the transportation cost is minimized.

# Input data
The input file `petrom.in` contains on the first line two natural numbers separated by a space `n` and `k`, representing the number of gas stations and the number of depots that need to be built, respectively. 
The next `n` lines contain `n` natural numbers $d_1, d_2, \ldots, d_n$, one number per line, representing the distances from Petrom's headquarters to the `n` gas stations.

# Output data
The output file `petrom.out` will contain on the first line the transportation cost (minimum possible).
The next `k` lines contain the gas stations where depots will be built to achieve the minimum cost, one gas station per line.

# Constraints and clarifications
* `1 \leq n \leq 400`
* `1 \leq k \leq 300`
* `k \leq n`
* $0 < d_1 < d_2 < \ldots < d_n \leq 30000$
* If there are multiple solutions, you can determine any of them.
* For each test, `40%` of the points are awarded for determining the minimum cost and `100%` for solving the entire task.

# Example

`petrom.in`
```
6 3
5
6
12
19
20
27
```

`petrom.out`
```
8
2
4
6
```

Explanation
---

Depot `1` will be built in gas station `2` and will supply gas stations `1, 2, 3`. (Cost: `1+0+6=7`)
Depot `2` will be built in gas station `4` and will supply gas stations `4, 5`. (Cost: `0+1=1`)
Depot `3` will be built in gas station `6` and will supply gas station `6`. (Cost: `0`)