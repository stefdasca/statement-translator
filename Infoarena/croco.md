# Croco

The tests for this problem are not well constructed enough to correctly differentiate inefficient or wrong solutions. Click here if you want to help us improve the quality of the tests for this problem! Professor Utonium made an amazing discovery; he managed to create the most adorable pets, which he named crocobauzers. The professor created $N$ crocobauzers through experiments and intends to let them reproduce for one year before giving them to his friends. After much study of the $N$ crocobauzers, the professor discovered that any pair can reproduce and, moreover, he knows how many offspring each pair will have in one year. Obviously, if the professor kept the crocobauzers in the same room, all pairs would reproduce and have the maximum number of offspring possible at the end of the year. Unfortunately, this is not possible because the rooms are too small, and if he puts all the crocobauzers in one room, they will die. However, it seems that two rooms are sufficient to keep them. After the professor divides the crocobauzers, they will stay like this until the end of the year, and any two crocobauzers in the same room will reproduce.

## Task

If you want a crocobauzer to get to you, you must help the professor divide the crocobauzers so that at the end of the year they have the maximum number of offspring possible.

## Input data

The first line of the input file `croco.in` contains the natural number $N$ representing the number of crocobauzers. The next $N$ lines contain $N$ natural numbers separated by spaces; the $j$-th number on the $i$-th line represents the number of offspring that crocobauzers $i$ and $j$ would have if they were in the same room. Obviously, if $i$ is equal to $j$ the value is $0$, and if $j$ is less than $i$ the value is equal to the $i$-th value on line $j$.

## Output data

The output file `croco.out` will contain on the first line the maximum number of offspring the professor can have at the end of the year, as well as the number of crocobauzers in the first room, separated by a space. The second line will contain the ordinals of the crocobauzers in the first room, separated by spaces.

## Constraints and clarifications

$1 \leq N \leq 110$  
$0 \leq$ number of offspring of a pair of crocobauzers $\leq 221$  

## Example

`croco.in`  
```
5
0 4 1 1 0
4 0 0 0 1
1 0 0 4 0
1 0 4 0 4
0 1 0 4 0
```

`croco.out`  
```
12 2
1 2
```

## Explanation

In the first room are crocobauzers $1$ and $2$ who will have $4$ offspring together. In the second room will be crocobauzers $3$, $4$, and $5$. Crocobauzers $3$ and $4$ will have $4$ offspring together, crocobauzers $3$ and $5$ will have $0$ offspring, and crocobauzers $4$ and $5$ will have $4$ offspring. In total, there will be $12$ offspring.