~[image.png|align=right]

LLM has a multitude of friends around the world, more precisely $N$. For his birthday, he decides together with his friends to release lanterns. Each lantern is associated with a value $a_i$. The release of the lanterns is done according to the following rule:

In the first minute, LLM and his friends will mark the lanterns with a value divisible by 2, in the next minute they will mark the lanterns with a value divisible by 3, and in the next minute, those with a value divisible by 5 ... In the $i$-th minute, they will mark the lanterns with a value divisible by $p_i$, where $p_i$ is the $i$-th prime number.

Also, in each minute they will release those lanterns whose value $a_i$ has all its prime divisors marked.

# Task

You are given $P$, $N$ and the array $a_1$, $a_2$, ..., $a_N$.

If $P = 1$, display how many lanterns with associated prime number values were released in the first minute.

If $P = 2$, display, in ascending order, the square-free values associated with the lanterns released in the first two minutes.

If $P = 3$, display the minimum number of minutes after which at least $K$ lanterns will be released.

# Input data
The input file `lampion.in` contains:
- The first line contains the natural numbers $P$, $N$, and $K$.
- The second line contains $N$ natural numbers separated by a space, representing the array $a$.

# Output data
The output file `lampion.out` contains:
- The first line contains the answer to the task $P$. If $P = 1$, the output file’s first line will contain the number of lanterns with associated prime values released in the first minute. If $P = 2$, the output file’s first line will display the square-free values associated with the lanterns released in the first two minutes, in ascending order, separated by a space. If $P = 3$, the output file’s first line will display a single natural number representing the minimum number of minutes after which at least $K$ lanterns will be released.

# Constraints and clarifications
* A number is square-free if it is not divisible by any perfect square other than 1.
* $1 \leq K \leq N \leq 1 \ 000 \ 000$
* $2 \leq a_i \leq 5 \ 000 \ 000$, for any $1 \leq i \leq N$
* For 20 points $P = 1$.
* For 30 points $P = 2$.
* It is guaranteed that if $P = 2$, there will be at least one lantern released in the first two minutes.

# Example 1
`lampion.in`
```
1 7 7
10 6 11 5 2 38 33
```
`lampion.out`
```
1
```

# Example 2
`lampion.in`
```
2 7 7
10 6 11 5 2 38 33
```
`lampion.out`
```
2 6
```

# Example 3
`lampion.in`
```
3 7 7
10 6 11 5 2 38 33
```
`lampion.out`
```
8
```

# Explanations

In the first example:

The only lantern released in the first minute is the one with an associated value of 2.

In the second example:

In the first minute, the lantern with a value of 2 is released, and in the second minute, the lantern with a value of 6 is released, so after the first two minutes, the lanterns with values 2 and 6 are released.

In the third and fourth examples:

In the first minute, the lantern with a value of 2 is released.

In the second minute, the lantern with a value of 6 is released.

In the third minute, the lanterns with values 5 and 10 are released.

In the fourth minute, no lanterns are released.

In the fifth minute, the lanterns with values 11 and 33 are released.

In the sixth and seventh minutes, no lanterns are released.

In the eighth minute, the lantern with a value of 38 is released.

So, the minimum number of minutes after which at least 4 lanterns are released is 3, and the minimum number of minutes after which at least 7 lanterns are released is 8.