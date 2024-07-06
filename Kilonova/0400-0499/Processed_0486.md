# Task

Omeskok is playing a budget version of Minecraft. It is a 2D Minecraft in which there are only 2 types of blocks: a dirt block and a "water block". The map is represented by multiple columns of dirt of different heights. Water has the same characteristics as in the original game, but reduced to 2 dimensions. 

Thus, if we place a "water block" on a dirt column, it will flow to the left or right only if the dirt column in the direction of the flow has a height less than or equal to the current column. Unlike the original game, the water level remains constant (see drawing). Omeskok now has 2 questions:

1. For each dirt column, what would be the area of the water structure formed if we place a "water block" on top of it, if the water level does not remain constant?
2. For each dirt column, what would be the area of the water structure formed if we place a "water block" on top of it, if the water level remains constant?

# Input data

The first line will contain the task to be solved. The second line contains a number $N$, the number of dirt columns. The next line contains a permutation of order $N$ representing the heights of the dirt columns.

# Output data

It will contain a sequence of length $N$ which represents the solution to the task.

# Constraints and clarifications

- $1 \le N \le 10^6$
- The heights of the dirt columns are a permutation of the set $\{1, 2, \ldots, N\}$
- Water cannot flow out of the play area under any circumstances.
- For correctly solving the first task, 40 points are awarded, and for the second, 60 points are awarded.

# Observation

Due to the fact that the input is very large, it is recommended to use the following instructions at the beginning of the code:

```cpp
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

stdin

```
1
7
4 2 3 7 6 5 1
```

stdout

```
2 1 2 6 3 2 1
```

# Explanation

If we pour water on the fourth column, the terrain will look like this:
~[Screenshot 2023-03-11 130347.png]

So there will be $6$ pieces of water in that case.

# Example

stdin

```
2
7
1 5 4 2 3 6 7
```

stdout

```
1 15 6 1 3 21 28
```

# Explanation

If we pour water on the third column, the terrain will look like this:
~[Screenshot 2023-03-11 131415.png]

So there will be $6$ pieces of water, so the answer for the third column is $6$.