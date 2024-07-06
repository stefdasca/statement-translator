The electoral campaign ended a while ago, but the wall in the central park of the city, where posters were placed, is still in a deplorable state. The rain and wind have acted and further defaced this area which once had beautifully colored posters. The city hall decided to take care of this problem. A commission was formed and it was decided to create advertisement panels to cover the deteriorated sections.

Since the funds are limited, it was decided that only a certain number of advertisement panels should be allocated, aiming to cover the smallest possible area. The commission received field data in the form: wall length, how many units are occupied with posters that need to be covered, and the number of panels they can use. Additionally, data is also provided on which units of the wall are occupied with already deteriorated posters.

# Task

Given the wall length, the number of deteriorated units, the maximum number of panels that can be used, and which units of the wall are deteriorated, determine the total minimum length of panels used to cover the area and how many panels are used. We define the minimum length as the total number of wall units covered to mask the problem areas. To cover the deteriorated units of the wall, it is not mandatory to use all the panels. Given the limited number of panels, it is possible to cover clean areas of the wall as well.

# Input data

The input file `afise.in` contains on the first line $3$ values separated by a space $L \\ n \\ k$, with the meaning: $L$ the total length of the wall, $n$ the number of units to be covered, and $k$ the maximum number of panels that can be used. The second line contains $n$ values $x_1, x_2, \\dots, x_n$ separated by a space, where $x_i$ represents the unit of the wall that is covered by an old poster. The values $x_1, x_2, \\dots, x_n$ appear in random order.

# Output data

The output file `afise.out` contains a single line with two values representing the total minimum length used and the number of panels used so that all deteriorated areas are covered.

# Constraints and clarifications

* $0 < L \\leq 1 \\ 000$;
* $0 < n \\leq L$;
* $0 < k \\leq L / 2$;

# Example 1

`afise.in`
```
25 8 3
3 11 6 4 19 15 20 12
```

`afise.out`
```
11 3
```

## Explanation

The wall has a length of $25$ units, and $8$ of them contain posters that need to be covered with a maximum of $3$ panels. All $3$ panels will be used, totaling $11$ units, covering the areas $3-6$, $11-15$, and $19-20$.

~[afise1.png]

# Example 2

`afise.in`
```
10 4 6
7 3 8 1
```

`afise.out`
```
4 3
```

