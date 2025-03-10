# Task

Given a value $n$, determine how many permutations of length $n$ exist such that any value $i$ is located at one of the positions $i-1$, $i$, or $i+1$. Additionally, no $3$ consecutive fixed points are allowed (if the value $i$ is precisely at position $i$, we say there is a fixed point).

# Input data

The first line of the input file `aproapeperm.in` contains the value $n$.

# Output data

The output file `aproapeperm.out` will contain a single integer, representing the required value modulo $10^9+7$.

# Constraints and clarifications

* For tests worth 19 points, $1 \\leq n \\leq 8$;
* For other tests worth 22 points, $1 \\leq n \\leq 40$;
* For other tests worth 59 points, $1 \\leq n \\leq 100\ 000$;

# Example 1

`aproapeperm.in`
```
6
```

`aproapeperm.out`
```
8
```

## Explanation

The counted permutations are:  

`1 2 4 3 5 6`  
`1 2 4 3 6 5`  
`1 3 2 4 6 5`  
`1 3 2 5 4 6`  
`2 1 3 4 6 5`  
`2 1 3 5 4 6`  
`2 1 4 3 5 6`  
`2 1 4 3 6 5` 