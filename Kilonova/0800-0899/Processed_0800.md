The die used in various games is a cube with each face displaying 1, 2, 3, 4, 5, or 6 dots. On a die, there are no two faces with the same number of dots, and the sum of the dots on any two opposite faces is equal to 7.

On a game table, a square path is drawn with a side size of $ n $. Each side of the path is divided into $ n $ identical squares, each having the same side length as the die. The die is initially placed in the top left corner of the path and then rolled from one face to another, from square to square, along the path, in a clockwise direction.

At any time we look at the die, we can see the number of dots on three of its faces (as shown in the drawing above).

We denote by $ f_1 $ the face of the cube oriented towards us, $ f_2 $ the upper face of the cube, and $ f_3 $ the right-side face of the cube. For the example in the figure: $ n = 4 $, the face towards us ($ f_1 $) contains three dots, the upper face ($ f_2 $) contains two dots, the right-side face ($ f_3 $) contains one dot, and the direction of movement is specified by arrows.

~[zar.png]

# Task

Given the size $ n $ of the path and the number of dots on the three faces of the die in the initial position, determine after $ k $ rolls the number of dots that can be seen on each of the three faces of the die.

# Input data

The file `zar.in` contains on the first line the natural numbers $ n $ and $ k $ separated by a space. On the second line, there are three natural numbers separated by spaces corresponding to the number of dots on the faces $ f_1, f_2 $, and $ f_3 $ of the die in the initial position.

# Output data

The file `zar.out` will contain a single line with three natural numbers separated by a space, representing the number of dots that can be seen on the faces $ f_1, f_2 $, and $ f_3 $ (in this order) after $ k $ rolls on the given path.

# Constraints and clarifications

* $ 2 \leq n \leq 20 \ 000 $
* $ 1 \leq k \leq 1 \ 000 \ 000 $

# Example

`zar.in`
```
4 11
3 2 1
```

`zar.out`
```
1 5 3
```

## Explanation

Each side of the path consists of 4 squares, and 11 rolls will be performed. After the first roll to the right, the values of the three faces ($ f_1, f_2 $, and $ f_3 $) of the die will be 3, 6, and 2. After the second roll, we get the numbers 3, 5, 6, and after the third roll, the values of the faces will be 3, 1, and 5. At this point, the die has completed one side of the path. The next three rolls will be performed downwards along the path where the faces will have the successive values 1, 4, 5, then 4, 6, 5, and 6, 3, 5. Next are the rolls to the left, and on the faces of the die, we will observe the values 6, 5, 4, then 6, 4, 2, and respectively 6, 2, 3. The last two rolls will be performed upwards along the left side of the path. After the penultimate roll, we get 5, 6, 3, and after the last roll, the values of the faces will be 1, 5, and 3.