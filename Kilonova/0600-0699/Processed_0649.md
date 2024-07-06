~[baloane_image.png|align=right|width=30%] 
On the occasion of June 1st, various activities for children were organized in the city center. Marcela is walking around $N$ stands that offer free balloons with unique designs, and she takes two: one for herself and one for her younger brother.
At the end of her walk, she realizes that she has collected so many balloons that she started to float, carried by the wind. Scared and worried that she might be blown away by a gust, she quickly lets go of one balloon without looking at its type.
After arriving home, she realizes that she no longer has a balloon for her brother, so she decides to go back to the city to get another one with the same design. However, she needs to hurry because there were fewer balloons offered by the stands.

# Task

You are given the number $N$ of stands visited and the remaining balloon designs. Help her quickly determine the type of the lost balloon.

# Input data

The input file `baloane.in` contains on the first line a natural number $N$ representing the number of stands visited, and on the next ($2*N - 1$) lines, the balloon designs, represented by non-zero integers. Among these, there are ($N - 1$) pairs of equal values and a unique value.

# Output data

The output file `baloane.out` will contain a single integer, representing the type of the lost balloon.

# Constraints and clarifications

* $1 \leq N \leq 800\ 000$
* $|x| < 2^{63}$, $x \neq 0$, where $x$ is the balloon design

# Scoring

* It is possible that the scores may differ from those in the competition even if the solution is the same.

|#| Score | Constraints|
|-|--------|-----------|
|1|5|$N \leq 1\ 000$, $ 0 < x \leq 10\ 000$, the numbers are in ascending order in the input file.|
|2|5|$N \leq 1\ 000$, $0 < x < 10\ 000$|
|3|10|$N \leq 100\ 000$, $0 < x \leq 500\ 000$ |
|4|33|$N \leq 100\ 000$, $\\vert x \\vert \leq 500\ 000$|
|5|34|$N \leq 500\ 000$|
|6|13|Without other constraints|

# Example

`baloane.in`
```
3
-1 2 3 -1 3
```

`baloane.out`
```
2
```

## Explanation

Marcela visited 3 stands, from which she took a total of 6 balloons, two of each design.
Among these, she let go of the balloon of type 2, so she arrived home with 5 balloons.