A forest ranger has just been appointed as the head of a new forest. He sees that his forest has quite a few trees, so he decides to plant some new trees. Instead of receiving simple offers, where he receives a number of trees for a sum of money, he receives offers of lines of trees for the incredible sum of **0.00 lei!** Seeing this possibility, he wants to choose $K$ of these lines, such that the area of the polygon obtained from some intersection points of these lines is as large as possible! A larger area polygon allows the ranger to bring in as many animals and tourists as possible, so he can turn the forest into a business! Our ranger is only interested in the area, not in the lines he chooses. Being quite lazy, he offers you a reward of **100 points** if you help him solve the problem!

# Task
Help the ranger turn the forest into a business by specifying the maximum area of a polygon obtained by selecting some intersection points of $K$ lines.

# Input data
The first line contains the numbers $N$ and $K$, which represent the number of lines and the number of lines we are allowed to select. The following $N$ lines contain $3$ numbers each: $a$, $b$, $c$, which represent the equation of a line (the equation of a line will be of the form $ax + by + c = 0$).

# Output data
Print the **maximum** area of a polygon formed from some vertices of the intersections of the selected $K$ lines.
You can display the number with as many decimals as you want. The answer will be considered correct if the absolute difference between the displayed value and the jury's answer is at most $10^{-5}$.

# Constraints and clarifications
- $3 \leq K \leq N \leq 14$
- $-10^6 \leq a, b, c \leq 10^6$
- It is guaranteed that all the numbers in the input are integers
- It is guaranteed that the slopes of the lines are distinct
- By some selected points, we mean a number greater than or equal to $3$ and at most equal to $\frac{K \cdot (K - 1)}{2}$
- For $10$ points, $N = 3$ (test 3)
- If the difference between the answer given by the program and that of the jury is at most $10^{-3}$, then 70% of the points will be awarded
- If the difference between the answer given by the program and that of the jury is at most $10^{-1}$, then 20% of the points will be awarded

# Example
`stdin`
```
4 3
1 0 0
0 1 0
1 -1 1
-1 -1 -2
```
`stdout`
```
2.25
```

# Explanation
We use lines 1, 3, and 4. The polygon of maximum area is formed by the following 3 points: the intersection of lines 1 and 3, the intersection of lines 3 and 4, the intersection of lines 4 and 1.
~[padurar1.png]