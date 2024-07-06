~[mario.png|align=right|width=26em]

Mario games are online games for children of all ages. Now, Mario—the character from the game—needs your help to get from the tower of the castle where he is to the ground, where Princess Peach is eagerly waiting for him. The descent from the tower is made using horizontal platforms of different lengths, each located at a certain height above the ground. The movement from the tower to the ground will be as follows:

- Mario lets himself fall freely from the tower due to gravity;
- if he lands on a platform while falling, he will move along its surface to one of its left or right ends, from where he will again let himself fall freely towards the ground.

If Mario falls from a height **greater than $H$**, he loses all his energy and cannot continue the game.

# Task

Knowing the position where Mario is and the arrangement of the platforms (given in Cartesian coordinates), determine the **number of distinct paths** Mario can take to reach the princess.

# Input data

From the file `mario.in` we will read:

- The first line contains three natural numbers $h_M$, $x_M$ and $H$ representing in order: the height where Mario is above the ground, the x-coordinate of his position, and the maximum height he can fall freely;
- The second line contains one natural number $N$ representing the number of platforms;
- The following $N$ lines each contain three natural numbers $(h_p, x_1, x_2)$ with the meaning: at the height $h_p$ above the ground is a horizontal platform with the left end at $x_1$ and the right end at $x_2$.

# Output data

In the file `mario.out` print on the first line a single natural number representing the number of distinct paths Mario can take to the princess.

# Constraints and clarifications

- $1 \leq N \leq 10\ 000$
- $0 < H, h_p, h_M \leq 20\ 000$, $h_M > h_p$
- $0 < x_M, x_1, x_2 \leq 200\ 000$
- If there are multiple platforms at the same height, they are guaranteed not to overlap at any point.
- The number of paths is always greater than $0$ and less than $2^{63}$.

# Example

`mario.in`
```
14 8 7
4
9 8 15
2 10 13
12 6 11
4 2 10
```

`mario.out`
```
3
```

## Explanation

The tower is at a height of $14$ above the ground and has the x-coordinate $8$. Mario can fall freely up to $7$ units.

There are $4$ platforms: one platform is at a height of $9$ above the ground and has its ends at $8$ and $15$. Another platform is at a height of $2$ above the ground and has its ends at $10$ and $13$. The next platform is at a height of $12$ and has its left end at $6$ and its right end at $11$. The last platform is $4$ units above the ground and has its ends at $2$ and $10$.

There are $3$ distinct paths Mario can take from the tower to the ground.

~[mario2.png|width=40em]