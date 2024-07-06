A lego game has $P$ pieces which are identical cubes. Dorel is playing with them to build various toys, but to do this he needs your help.

# Task
Knowing the number of pieces $P$ he has, Dorel wants to know:
1. The number of pieces from which he can build the largest foundation. A foundation is in the shape of a square and has sides formed of at least 3 pieces (as in figure 1).
2. The number of pieces in the tallest tower that can be built. Dorel builds a lego tower as follows: at the beginning, he makes a square which he calls the ground floor (or level $0$). On top of it, he places $4$ pieces in the corners which he calls pillars. Then, on top of the pillars, he places a new square which he calls level $1$. On top of this, he places pillars again, over which he places level $2$. And he continues until the last level. Over the last level, he does **not** place pillars. All the constructed levels have the same number of pieces and are in the shape of a square with sides of at least $3$ pieces. The height of a tower is given by the number of levels. Pillars are not considered levels, they are part of the tower's structure. If multiple towers can be built with the same height, then Dorel wants to know the number of pieces in the tower with the most pieces. (See figure 2).
3. The number of legoball fields that can be built using all the lego pieces. A legoball field has the shape of a rectangle where each side is formed of at least $3$ pieces (as in figure 3).

~[fig1.png]

(Figure 1) A foundation with size `6 x 6`.

~[fig2.png]

(Figure 2) A tower with height $3$, each level having size `5 x 5`

~[fig3.png]

(Figure 3) A legoball field with size `6 x 3`.

# Input data
The file `legos.in` contains two non-negative integers $C$ and $P$, separated by a single space, representing the task number and the number of lego pieces Dorel has.

# Output data
For each of the $3$ tasks, the file `legos.out` will contain a single number which represents the answer to that task.

# Constraints and clarifications
* $1 \leq C \leq 3$;
* $1 \leq P \leq 1 \ 000 \ 000 \ 000$;
* For task $2$ a tower can be formed only from the ground floor, but it cannot be formed from the ground floor and pillars (as it would have pillars over the last level);
* For $31$ points, $C = 1$;
* For $33$ points, $C = 2$;
* For $36$ points, $C = 3$.

# Example 1

`legos.in`
```
1 29
```

`legos.out`
```
25
```

## Explanation

Task $1$ is solved. There are $29$ lego pieces. The largest foundation that can be built has the size `5 x 5`, it is formed from $25$ pieces.

# Example 2

`legos.in`
```
2 19
```

`legos.out`
```
16
```

## Explanation

Task $2$ is solved. There are $19$ lego pieces. The tallest tower that can be made consists only of the ground floor. There are two such towers, one with $9$ pieces and the other with $16$. Among these the one with $16$ pieces has more.

# Example 3

`legos.in`
```
3 18
```

`legos.out`
```
2
```

## Explanation

Task $3$ is solved. There are two ways to build a legoball field. These have the sizes `3 x 6` and `6 x 3`.