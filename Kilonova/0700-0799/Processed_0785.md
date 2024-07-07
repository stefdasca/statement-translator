~[inimioare.png|align=right]

Two friends, Valentin and Valentina, each have $n$ stickers with hearts. Each sticker is square-shaped and divided into four identical squares containing hearts, at least one and at most $9$ in each square. The two friends propose that on the card they will gift together to their teacher, they will stick stickers with many hearts. The place on the card where the stickers can be attached is not square-shaped and can only fit two halves of stickers attached next to each other. Thus, Valentina chooses a single sticker from the $n$ she owns, cuts it in half (either horizontally or vertically) and then, from the two halves obtained, selects one single half to stick on the card. After horizontally cutting a sticker, the obtained half can be rotated in any way and then placed on the card. At the same time, Valentin proceeds similarly. After attaching the cut stickers on the card (Valentina's first and then Valentin's next to it, or vice versa), four adjacent squares containing hearts can be observed. The children write underneath each of the four squares the number of hearts on it and thus obtain a number $m$, of four digits (read from left to right), as seen in the adjacent example.

Help the two friends choose one sticker each, how each will cut it, and the position where it will stick on the card such that, after writing under each square the corresponding number of hearts, the largest possible four-digit number $m$ is obtained.

# Task

Write a program that displays the largest number $m$ determined.

# Input data

~[inimioare1.png|align=right]

From the file `inimioare.in`, read in order:

* The first line contains the number $n$ which represents the number of stickers each child has.
* The following $n$ lines contain $4$ non-zero digits (separated by a space), representing the number of hearts **drawn on each of Valentina's stickers**. These $4$ values are read in the order described in the adjacent drawing.
* The following $n$ lines contain $4$ non-zero digits (separated by a space), representing the number of hearts **drawn on each of Valentin's stickers**. These $4$ values are read in the order described in the adjacent drawing.

# Output data

The file `inimioare.out` will contain a single line which will print the natural number $m$, representing the largest number that can be formed from the stickers of the two friends.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$;

# Example

`inimioare.in`
```
4
1 6 1 1
2 2 2 2
2 3 1 1
1 5 6 2
2 3 4 2
8 1 1 8
2 8 1 1
2 4 3 8
```

`inimioare.out`
```
8865
```

## Explanation

Valentina's stickers:

```
1 6 1 1
2 2 2 2
2 3 1 1
1 5 6 2
```

Chosen sticker by Valentina:
```
1 5
2 6
```

Valentin's stickers:
```
2 3 4 2
8 1 1 8
2 8 1 1
2 4 3 8
```

Chosen sticker by Valentin:
```
8 1
8 1
