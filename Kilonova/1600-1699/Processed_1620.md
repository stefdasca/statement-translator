Since kindergarten, Maria has been passionate about coloring using markers. One day, the teacher gave her $4$ markers (of different colors). She also gave Maria a very large number of square cards, identical in size. She told her to color the sides (the four edges) of each card so that any card would have one edge of each of the $4$ colors. Thus, the whole morning the girl colored.

Now, in middle school, after finding the cards she colored when she was younger, she thought about the following problem: she can arrange $a \cdot b$ cards on a rectangular surface with $a$ rows and $b$ columns such that the conditions are fulfilled: each of the $4$ edges of the rectangular area must be colored with a single color (each edge with a different color); neighboring cards inside must have the common side of the same color.

# Task

For multiple pairs $(a, b)$ given, to display a possibility of arranging the cards or to say that this is not possible.

# Input data

The file `carioci.in` contains on the first line a natural number $T$. Each of the following $T$ lines contains two natural numbers $a$ and $b$, separated by space, representing the number of rows and the number of columns for a rectangular area that needs to be formed.

# Output data

The file `carioci.out` will contain, in order for each of the $T$ tests, either a line with the value $0$ (when arranging is not possible) or $a$ lines with $b$ numbers each (separated by a space). A number represents the coding of a card. We agree to code as follows: we number the colors with numbers $1$, $2$, $3$, $4$. The code to display is formed by writing the color codes in the order North, East, South, West. Thus, a number with $4$ distinct digits is formed. This is the card's code.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq a, b \leq 100$
* Maria has colored a sufficiently large number of cards, in all ways.
* Any correct solution is accepted.

# Example 1

`carioci.in`
```
2
1 1
2 2
```

`carioci.out`
```
1234
1234 1342
3124 4321
```

## Explanation

~[carioci.png]

The drawing represents a solution for the test $a=2$, $b=2$.

# Example 2

`carioci.in`
```
3
1 1
1 2
2 2
```

`carioci.out`
```
1234
0
1234 1342
3124 4321
```

