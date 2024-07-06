```markdown
# Task

The joyful city is composed of $N$ buildings of heights $A_1, A_2, ..., A_N$. We want to promote OmegaSRL with a poster of area $X$. The poster must be rectangular and fully supported by the buildings. In how many ways can we promote?

# Input data

The first line contains $N$ and $X$.  
The second line contains the heights of the buildings $A_1, A_2, ..., A_N$.

# Output data

The number of ways.

# Constraints and clarifications

* $1 \leq N \leq 10^5$
* $1 \leq X, A_i \leq 10^9$
* The poster can be placed at any height

# Scoring

* For $40$ points $N \leq 1000$

# Example 1

`stdin`
```
3 4
2 4 1
```

`stdout`
```
2
```

## Explanation

This is what the joyful city looks like:  
~[Screenshot_2024-01-10_213911-removebg-preview_75_85_1_34.png]

These are the $2$ ways to place a poster of area $4$ on the buildings:  
~[Screenshot_2024-01-10_215010-removebg-preview_21.png]  
~[Screenshot_2024-01-10_215313-removebg-preview_21.png]

# Example 2

`stdin`
```
10 12
3 8 6 15 20 1 4 5 6 3
```

`stdout`
```
38
```
```