```markdown
# Task

The time has come for Mr. *B* to gather the dried peppers he will use to prepare the well-known paprika. He has $n$ peppers, connected by $n-1$ branches, so that one can reach any pepper from any other pepper through a series of branches. Formally, his peppers form a tree. Since he also has other more important tasks, Mr. *B* does not want to spend too much time picking peppers, so he calls in two friends to help him. Being an honest man, he decides to divide the tasks as fairly as possible. For this, he will cut $2$ branches and assign each of them one of the resulting **$3$** subtrees, but he wants to minimize the **difference** between the size of the largest and smallest subtree. You have to determine this minimum difference.

# Input data

The first line of the input file `paprika.in` contains $n$, the number of peppers.
Each of the next $n-1$ lines contains $2$ integers $x$ and $y$, which represent the labels of $2$ peppers that are directly connected by a branch.

# Output data

The first line of the output file `paprika.out` will contain a single integer, the required difference.

# Constraints and clarifications

* $1 \leq n \leq 200\ 000$
* $1 \leq x, y \leq n$

| **#**       | **Points**  | **Constraints** 
| ----------- | ----------- | -----------
| 1      | 15       |  $3 \leq n \leq 200$
| 2      | 35        |  $3 \leq n \leq 2\ 000$
| 3      | 50       |  No other constraints.

# Example 1

`paprika.in`
```
4
1 2
2 3
3 4
```

`paprika.out`
```
1
```

## Explanation

Any of the 3 ways to cut the branches will result in one component with two peppers and two components with one pepper each. Thus, the answer is $2-1=1$

# Example 2

`paprika.in`
```
6
1 2
1 3
3 4
3 5
5 6
```

`paprika.out`
```
0
```

## Explanation

It is possible to obtain three components of the same size if we cut the branches that connect peppers $1$ and $3$, and peppers $3$ and $5$.
```