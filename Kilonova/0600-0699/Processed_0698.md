Initial, Andrei had two arrays $V$ and $P$ of $N$ elements. The array $V$ contained natural numbers $< M$, while the array $P$ contained numbers with the following property: $P_i = (P_{i-1} \times V_i)$ (mod $M$), for every $i$, $2 \leq i \leq N$, and $P_i=V_i$, for $i=1$.

One morning, he realized that some numbers had gotten wet, and they were unreadable!

Because Andrei wants both arrays $V$ and $P$ to be readable from start to finish, he asks you to help him reconstruct the arrays.

# Input data

The first line contains $2$ natural numbers $N$ and $M$, while the second and third lines of the input will contain the arrays $V$ and $P$, respectively. If a number $-1$ is found at any position $i$, it means that number is unreadable. It is guaranteed that readable numbers respect the property described in the statement.

# Output data

The first line will contain the array $V$ readable from start to finish, and the second line will contain the array $P$ readable from start to finish. Because Andrei is a considerate boy, he will allow any solution you have found as long as it respects the rule of the arrays.

# Constraints and clarifications

* $1 \leq N \leq 10^5$
* $1 \leq M \leq 1000$
* For $42$ points, $N \leq 1000$
* It is guaranteed that there is a solution
* During the contest "RoAlgo Contest #2", test case with ID 14 was not existent. It was added later so that only the solution with the best complexity would get 100 points.

# Example 1

`stdin`
```
3 6
1 -1 4
-1 -1 -1
```

`stdout`
```
1 4 4
1 4 4
```

## Explanation

* $1 = 1$
* $4 = (1 \times 4)$ (mod $6$)
* $4 = (4 \times 4)$ (mod $6$)

Therefore, these arrays respect the property.

# Example 2

`stdin`
```
3 7
-1 -1 5
-1 -1 6
```

`stdout`
```
2 2 5
2 4 6
```

## Explanation

* $2 = 2$
* $4 = (2 \times 2)$ (mod $7$)
* $6 = (4 \times 5)$ (mod $7$)

Therefore, these arrays respect the property.