Marius is a very curious boy who recently started playing a new game called Minecraft. In this game, materials of the same type are stacked together in groups (structures) of up to $k$ elements. Marius wants to find out into how many groups (stacks) all the $n$ materials he has will be stored and what is the least common multiple between the number of groups in which the materials are stored and the number of materials in the last group.

# Task

1. Determine the minimum number of groups, each containing up to $k$ elements (stacks), in which all the $n$ materials will be stored.
2. Determine the least common multiple between the number of groups in which the $n$ materials are stored and the number of materials in the last group.

# Input data

The input file `minecraft.in` contains on the first line an integer $c$ ($1 \le c \le 2$): $c = 1$ for the first task and $c = 2$ for the second task. The second line contains two integers $n$ and $k$ with the meanings described in the statement.

# Output data

The output file `minecraft.out` will contain a single natural number, specific to each task.

# Constraints and clarifications
* $ 1 \le k \le n \le 10^5 $

| # | Score |      Constraints     |
|:-:|:-----:|:--------------------:|
| 1 |  10   |  Examples in the statement  |
| 2 |  30   |       $c = 1$       |
| 3 |  60   |       $c = 2$       |

# Example 1

`minecraft.in`
```
1 
27 7
```
`minecraft.out`
```
4
```

## Explanation

There will be $3$ groups of $7$ materials and one of $6$ materials.

# Example 2

`minecraft.in`
```
2 
27 7
```
`minecraft.out`
```
12
```

## Explanation

The least common multiple between the number of groups $4$ and the number of materials in the last group $6$ is $12$.