*Because geometry is not part of the OJI material, the committee proposes the following problem:*

# Task

Three numbers $a \le b \le c$ can be the lengths of the sides of a triangle if and only if $a+b>c$. 

A sequence of numbers $a_1,a_2,\ldots,a_n$ is *stable* if:

- $n < 3$; or 
- $a_i$, $a_j$, and $a_k$ can be the lengths of the sides of a triangle, for any $1 \le i < j < k \le n$.

For example: $[]$, $[1]$ and $[5,3,4,3]$ are *stable*, whereas $[1,3,1]$ and $[3,3,1,4,2,5,4]$ are not *stable*. 

Given a sequence $a_1,a_2,\ldots,a_n$. Verify if all subarrays of the sequence $a$ are *stable*.

# Input data

The first line of the input file `magie.in` will contain a single number $n$ - the length of the array $a$.

The second line will contain $n$ numbers $a_1,a_2,\ldots,a_n$ - the elements of the array $a$.

# Output data

The output file `magie.out` will contain `YES`, if all subarrays of the given array are *stable*, otherwise it will contain `NO`.

# Constraints and clarifications

- $1 \le n \le 2 \cdot 10^5$;
- $1 \le a_i \le 10^9$;
- For $30$ points, $n \le 50$;
- For another $10$ points, $n \le 100$;
- For another $10$ points, $n \le 500$;
- For another $20$ points, $n \le 5 \ 000$;
- For the remaining $30$ points, no additional constraints are imposed.

# Example 1

`magie.in`
```
3
2 3 4
```

`magie.out`
```
YES
```

## Explanation

The subarrays $[2]$, $[3]$, $[4]$, $[2,3]$ and $[3,4]$ are *stable* because they have fewer than $3$ elements. 

The subarray $[2,3,4]$ is *stable* because $2+3 > 4$.

# Example 2

`magie.in`
```
4
5 3 4 3
```

`magie.out`
```
YES
```

# Example 3

`magie.in`
```
7
3 3 1 4 2 5 4
```

`magie.out`
```
NO
```

## Explanation

The subarray $[3,1,4,2]$ is not *stable* because $1$, $4$ and $2$ cannot be the lengths of the sides of a triangle ($1+2 \le 4$).