*\On a fateful winter morning, Cătălin invented a sorting algorithm with a complexity of $O(N)$, which he named "Binary Sort". Although this algorithm defies all laws of nature, it still cannot solve this problem.* 

# Task

Given an array $a_1,a_2,\ldots,a_n$. An array $b_1,b_2,\ldots,b_n$ is a *rearrangement* of $a$ if $b$ contains the same elements as $a$, possibly in a different order.

For example, rearrangements of $a=[2,1,2,3]$ include $[2,1,2,3]$, $[3,2,1,2]$ or $[1,2,2,3]$, but not $[1,2,3,4]$ or $[3,1,2,3]$.

The value of a rearrangement $b_1,b_2,\ldots,b_n$ is equal to $|b_1-b_2|+|b_2-b_3|+\ldots+|b_{n-1}-b_n|+|b_n-b_1|$, where $|x|$ represents the modulus or absolute value of $x$.

For example, the value of $b=[3,1,2,2]$ is equal to $|3-1|+|1-2|+|2-2|+|2-3|=2+1+0+1=4$.

Depending on the value of the task number $c$, you will need to find:

- If $c=1$, what is the *minimum* possible value of a rearrangement $b_1,b_2,\ldots,b_n$ of the array $a$?
- If $c=2$, what is the *maximum* possible value of a rearrangement $b_1,b_2,\ldots,b_n$ of the array $a$?


# Input data

The first line of the input file `binsort.in` will contain two numbers $c$ and $n$ - the task number and the length of the array $a$, respectively.

The second line will contain $n$ natural numbers $a_1,a_2,\ldots,a_n$ - the elements of the array $a$.

# Output data
- If $c=1$, then the output file `binsort.out` will contain the minimum possible value of a rearrangement of the array $a$, as well as any rearrangement $b_1,b_2,\ldots,b_n$ with the minimal value.
- If $c=2$, then the output file `binsort.out` will contain the maximum possible value of a rearrangement of the array $a$, as well as any rearrangement $b_1,b_2,\ldots,b_n$ with the maximal value.



# Constraints and clarifications

- $1 \le n \le 2 \cdot 10^5$;
- $-10^9 \le a_i \le 10^9$;
- For $20$ points, $c=1$ and $n \le 2 \ 000$;
- For another $20$ points, $c=1$;
- For $30$ points, $c=2$ and $n \le 2 \ 000$;
- For another $30$ points, $c=2$.

# Example 1

`binsort.in`
```
1 5
2 3 1 2 1
```

`binsort.out`
```
4
3 2 2 1 1
```

## Explanation 

The value of the rearrangement $[3,2,2,1,1]$ is equal to $|3-2|+|2-2|+|2-1|+|1-1|+|1-3|=4$, which is the minimum possible.

# Example 2

`binsort.in`
```
2 5
2 3 1 2 1
```

`binsort.out`
```
6
1 3 1 2 2
```

## Explanation

The value of the rearrangement $[1,3,1,2,2]$ is equal to $|1-3|+|3-1|+|1-2|+|2-2|+|2-1|=6$, which is the maximum possible.