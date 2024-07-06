# Task

After winning the Euro, Denis goes to a festival in Germany to celebrate. There, he finds $N$ bottles of juice lined up, with each bottle $i$ containing juice of type $s_{i}$. Additionally, he receives a voucher from the organizers, allowing him to select a sequence of bottles, pouring some juice from each bottle in the sequence into his glass. The goodness of the juice in the glass is equal to the xor of the juice types from the selected sequence of bottles.

For example, if he selects a sequence of bottles with juice types $5,\\ 1,\\ 2,\\ 5$, the juice in his glass will have a goodness equal to $5 \\oplus 1 \\oplus 2 \\oplus 5 = 3$.

Since Denis is too busy to think about which sequence he should choose, he asks you to help him calculate, for each position $i$, the maximum goodness of a sequence containing position $i$.

# Input data

The input file `xor.in` contains: 

The first line contains a number $N$. The second line contains $N$ natural numbers, the $i$-th of which represents $s_i$.

# Output data

The output file `xor.out` should contain:

The first line contains $N$ natural numbers, the $i$-th of which represents the maximum xor of a sequence containing position $i$.

# Constraints and clarifications

* $1 \\leq N \\leq 300 \\ 000$
* $0 \\leq s_{i} \\leq 127$

|# | Points | Constraints|
| - | - | ------------|
|0|0|The example below.|
|1|10|$N \\leq 500$|
|2|20|$N \\leq 5000$|
|3|70|No additional constraints|

# Example 1

`xor.in`
```
3
5 4 2
```

`xor.out`
```
5 6 6
```

## Explanation

The possible sequences are: 
* $[1,1]$ with xor $5$,
* $[1,2]$ with xor $1$,
* $[1,3]$ with xor $3$,
* $[2,2]$ with xor $4$,
* $[2,3]$ with xor $6$,
* $[3,3]$ with xor $2$.

For the first position, the sequence $[1,1]$ has the goodness (xor) $5$, being the highest goodness of a sequence containing the first position. For the 2nd and 3rd positions, the sequence $[2,3]$ with the goodness $6$ is the one with the highest goodness containing them.

# Example 2

`xor.in`
```
10
20 35 102 36 3 26 3 92 65 120 
```

`xor.out`
```
118 123 123 123 127 127 127 127 127 127
```