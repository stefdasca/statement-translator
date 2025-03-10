Certainly! Below is the translation of the competitive programming problem statement from Romanian to English, following the specified instructions:

---

"No man would put any word on paper if he had the courage to truly live the things he believes in." - Henry Miller

ASG visits the City Library and notices that each shelf has a length of $N$ and a height of 4. Each book has a length of 2 and a width of 1. ASG wants to find out how many different ways exist to arrange the books on the $K$ shelves such that each shelf is completely filled (without free spaces), and the configurations of the shelves are unique, regardless of whether you look at them from left to right or vice versa.

# Input data

The first line contains two numbers, $N$ and $K$, with the meaning from the statement.

# Output data

Print the number of ways to place the books on the $K$ shelves, such that if we take any $2$ ways to place the books, there is at least one shelf that differs. Since the value is very large, display the remainder of the division by $666\ 013$.

# Constraints and clarifications

* $1 \leq N \leq 10^{18}$
* $1 \leq K < 666\ 013$

# Example 1

`stdin`
```
2 3
```

`stdout`
```
10
```

# Explanation 

The number of ways to place on a shelf of size $2 \cdot 4$ books of size $1 \cdot 2$:

~[img1.jpg|align=center|width=70%]

# Example 2

`stdin`
```
3 1
```

`stdout`
```
11
```

# Example 3

`stdin`
```
88 132
```

`stdout`
```
505231
```

--- 

I have carefully translated the text while preserving the mathematical notation, structure, and specified image format. Any formatting or grammatical errors have been corrected according to standard English conventions. If there are any specific areas you would like me to look over again, please let me know!