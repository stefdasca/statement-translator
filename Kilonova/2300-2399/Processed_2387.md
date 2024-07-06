Ion, the young shepherd, has become passionate about photographing the landscapes around his sheepfold and, more recently, after buying a computer, he is also passionate about processing these images.

Now, Ion has a set of $t$ photos, numbered from $1$ to $t$. Ion has encoded each photo as a rectangular matrix of natural numbers, wherein he retains the color of each pixel in the photo.

For each photo, Ion analyzes square-shaped areas and observes that the "pattern" in certain areas appears multiple times in the photo. The occurrences he observes are not necessarily disjoint; they can partially overlap.

Now Ion wants to determine, for each photo $i$, the maximum length of the side of a square area whose pattern appears in the photo $i$ at least $k_i$ times, without rotations. The length of the side of a square area is equal to the number of lines (the same as the number of columns) of the area.

# Task

Write a program that determines, for each photo $i$ in the set, the maximum length of the side of a square area whose pattern appears in the photo at least $k_i$ times.

# Input data

The file `poze.in` will contain on the first line an integer $t$, representing the number of photos. The following lines in the file will contain the descriptions of the $t$ photos. The description of a photo will begin with a line containing three natural numbers $n \\ m \\ k$, separated by a space, where $n$ represents the number of lines of the matrix, $m$ the number of columns of the matrix, and $k$ the minimum desired number of occurrences of the square area. The following $n$ lines will contain $m$ natural numbers separated by spaces that represent the colors of the pixels in the photo.

# Output data

The file `poze.out` will contain exactly $t$ lines. Line $i$ will contain an integer representing the maximum length of the side of a square area that appears in photo $i$ at least $k_i$ times.

# Constraints and clarifications

* $1 \\leq t \\leq 5$
* $1 \\leq n, m \\leq 300$
* $2 \\leq k \\leq 5$
* The colors of the pixels are natural numbers $\leq 30\ 000$

# Example

`poze.in`
```
3 
4 4 2
0 0 1 0
0 0 1 0
1 1 0 1
1 1 0 0
3 3 2
3 0 1
0 3 0
1 0 3
3 3 5
0 0 1
0 0 1
1 1 2
```

`poze.out`
```
2
2
0
```

## Explanation

For the first photo, the pattern in the square area of side $2$ with the top-left corner in position $(1,3)$ appears twice.

For the second photo, the pattern in the square area of side $2$ with the top-left corner in position $(1,1)$ appears twice.

For the third photo, there is no square area whose pattern appears at least $5$ times, so the maximum side length is $0$.