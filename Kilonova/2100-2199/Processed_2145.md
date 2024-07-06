The doctors at the Heart Institute want to calculate the maximum power of a patient's heart using measurements taken with electronic devices. Given $N$ natural numbers representing the intensities of heartbeats at one-second intervals. The intensities can be visualized as $N$ vertical lines with heights $h_1, h_2, \dots, h_n$. The distance between two consecutive lines is $1$.

The maximum power of a heart is defined as the maximum area of a rectangle that can be obtained between any two heartbeats.

# Task

Given the number $N$ of a patient's heartbeats and their intensities $h_1, h_2, \dots, h_n$, determine the maximum power of the heart.

# Input data

The input file contains on the first line a natural number $N$ representing the number of heartbeats. The second line contains $N$ natural numbers separated by spaces $h_1, h_2, \dots, h_n$, representing the intensities of the heartbeats.

# Output data

The output file must contain a natural number $P$ on the first line, where $P$ is the maximum power of the heart.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $1 \leq h_i \leq 200$
* For $50$ points, $N \leq 1 \ 000$.

# Example 1

`inima.in`
```
9
1 8 6 2 5 4 8 3 7
```

`inima.out`
```
49
```

## Explanation

The maximum power of the heart (the colored part) between two heartbeats is $49$.

~[img1.jpg|align=center]

# Example 2

`inima.in`
```
2
1 1
```

`inima.out`
```
1
```

## Explanation

The maximum power of the heart (the colored part) between two heartbeats is $1$.

~[img2.jpg|align=center]