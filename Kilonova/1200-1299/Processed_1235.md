Here is the translated competitive programming problem statement in English:

```markdown
The $n$ prisoners of a prison, numbered from $1$ to $n$, need to dig a trench laid in a straight line between two points $A$ and $B$, situated at a distance of $250$ km from each other, where there are $251$ kilometer posts numbered from $0$ to $250$. However, each prisoner has a demand, "it’s democracy, isn't it?": he wants to dig only somewhere in the area between post $x$ and post $y$. Besides these demands, the prison also faces another problem: it doesn't have enough guards.

# Task

Knowing the number $n$ of prisoners and their demands, determine the place/places where the prisoners will be made to dig in a working day, respecting their demands, such that the number of guards required to guard the $n$ prisoners is minimized. The interval in which a guard can supervise cannot contain two or more disjoint areas from those expressed by the prisoners in their preferences.

# Input data

The input file `sant.in` contains on the first line the number $n$ of prisoners. On each of the next $n$ lines, there are two natural numbers, $a_i \\ b_i$, separated by a space $(a_i \\leq b_i)$, representing the prisoner's demand. More exactly, on line $i+1 \\ (1 \\leq i \\leq n)$, the demand of the prisoner with number $i$ is described.

# Output data

The output file `sant.out` will contain on the first line the natural number $k$ representing the minimum number of guards required to guard the $n$ prisoners put to work. On the following $2 \\cdot k$ lines, the places where the prisoners will be made to dig are described, as follows: each pair of lines $(2 \\cdot j, 2 \\cdot j+1)$ will contain on line $2 \\cdot j$ three natural numbers $p \\ x_j \\ y_j$, separated by a space, representing the guard's number and the kilometer posts $x_j$ and $y_j$ where the guard $p$ will supervise, and on line $2 \\cdot j+1$ the numbers of the prisoners who dig in this area will be written, separated by a space, in ascending order.

# Constraints and clarifications

* $1 \\leq n \\leq 10 \\ 000$;
* $0 \\leq a_i \\leq b_i \\leq 250$, for any $i$, $1 \\leq i \\leq n$;
* $0 \\leq x_j \\leq y_j \\leq 250$, for any $j$, $1 \\leq j \\leq k$;
* A prisoner can also dig at a single point ("at the kilometer post numbered $x$");
* If multiple solutions exist, only one will be displayed;
* The order numbers of the guards will be written in the file in ascending order;
* The numbering of the guards starts from $1$.
* The solution is not unique!

# Example 1

`sant.in`
```
3
0 20
8 13
30 60
```

`sant.out`
```
2
1 8 13
1 2
2 30 60
3
```

## Explanation

$2$ guards are needed: guard $1$ will supervise between post $8$ and post $13$, and the supervised prisoners are $1$ and $2$; guard $2$ will supervise between post $30$ and post $60$, and the supervised prisoner is $3$. 

# Example 2

`sant.in`
```
4
10 20
2 5
30 40
5 7
```

`sant.out`
```
3
1 10 20
1
2 5 5
2 4
3 30 40
3
```

## Explanation

$3$ guards are needed: guard $1$ will supervise between post $10$ and post $20$, and the supervised prisoner is $1$; guard $2$ will supervise at post $5$, and the supervised prisoners are $2$ and $4$; guard $3$ will supervise between posts $30$ and $40$, and the supervised prisoner is $3$.

# Example 3

`sant.in`
```
5
10 30
30 32
0 30
27 30
27 28
```

`sant.out`
```
2
1 30 30
1 2 3 4
2 27 28
5
```

## Explanation

$2$ guards are needed: guard $1$ will supervise at post $30$, and the supervised prisoners are $1$, $2$, $3$, and $4$; guard $2$ will supervise between posts $27$ and $28$, and the supervised prisoner is $5$. 
```