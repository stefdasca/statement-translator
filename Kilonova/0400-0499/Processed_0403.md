```markdown
A sequence with $N$ values $0$ and $1$ is read. We call an alternating subarray of the given sequence, a succession of at least $3$ terms located on consecutive positions in the sequence, in which adjacent terms have different values. 
We say that an alternating subarray is a subarray `T0`, if it starts and ends with $0$. For example `0 1 0 1 0` or `0 1 0` are `T0` subarrays.
We say that an alternating subarray is a subarray `T1`, if it starts and ends with $1$. For example `1 0 1 0 1` or `1 0 1` are `T1` subarrays.
We say that two subarrays `T0` and `T1` intersect if they have common elements.

~[secv01.png]

# Task
1) Find the longest subarray of elements equal to 0. Display the number of elements in it.
2) Choose two subarrays, one `T0` and another `T1`, such that the subarray determined by their intersection is the longest. Display the starting and ending position of the subarray of elements corresponding to this intersection. If there are multiple such subarrays, choose the leftmost one.

# Input data
In the file `secv01.in`, the first line contains two values $C$ and $N$ separated by a space. The second line contains $N$ values $0$ and $1$ representing the elements of the sequence. For $C = 1$ only task $1$ is solved and for $C = 2$ only task $2$ is solved.

# Output data
- If $C = 1$, then only the first task will be solved, and the length of the required subarray is displayed in the file `secv01.out`;
- If $C = 2$, then only the second task will be solved, and two natural numbers `i` and `j` with the following meanings will be displayed in the file `secv01.out`: `i` is the starting position and `j` is the ending position of the subarray corresponding to the determined intersection.

# Constraints and clarifications
- $4 \leq n \leq 100 \ 000$;
- The existence of `T0` and `T1` subarrays in the sequence is guaranteed.

# Example 1

`secv01.in`
```
1 14
0 1 0 0 0 1 1 0 1 1 0 0 1 0
```

`secv01.out`
```
3
```

## Explanation

$0 \ 1 \ \colorbox{DarkGray}{0 0 0} \ 1 \ 1 \ 0 \ 1 \ 1 \ 0 \ 0 \ 1 \ 0$

# Example 2

`secv01.in`
```
2 23
0 0 1 0 1 1 0 1 0 0 0 1 0 1 0 1 0 0 1 0 1 0 0
```

`secv01.out`
```
12 16
```

## Explanation

$0 \ \colorbox{DarkGray}{0 \textcolor{red}{1 0} 1} \ \colorbox{DarkGray}{1 \textcolor{red}{0 1} 0} \ 0 \ \colorbox{DarkGray}{0 \textcolor{red}{1 0 1 0 1} 0} \ \colorbox{DarkGray}{0 \textcolor{red}{1 0 1} 0} \ 0$

The intersection between a `T0` subarray and a `T1` subarray generates the longest subarray which starts at position $12$ and ends at position $16$.
```