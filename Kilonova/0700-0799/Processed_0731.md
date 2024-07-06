Eager for perfect physical condition, a future national olympic in computer science proposes to climb the highest peak of a mountain range. He equips himself accordingly, buys a thermos, *fills it with water*, gathers information about the existing trails, and completes the input file `popas.in`. Along each trail, there are several springs from which the hiker can fill his thermos. Knowing that on the mountain it is good to walk at a constant pace and without breaking rhythm, he intends to reach the peak making *as few stops (to fill the thermos) as possible*.

# Task

Among all existing trails to the peak, determine the one for which the **total number of stops is minimum**. If there are multiple such trails, the one that is last in the input file will be chosen.

# Input data

The file `popas.in` contains:
- the first line contains $k$ - the total number of trails to the peak
- each of the next $k$ lines contains a description of a trail (each line contains numbers separated by a space), i.e.:
    - $i$ - the number associated with the trail (each trail is uniquely identified by a natural number between $1$ and $k$)
    - $r$ - the number of cold water springs on the trail
    - $d_1, d_2, \dots, d_r$ – $r$ numbers representing the distance from the starting point to each spring
- the last two lines contain:
    - t the distance for which the hiker has enough water in the thermos
    - u the distance the hiker can travel without water

# Output data

The file `popas.out` will contain on the same line, separated by a space, two numbers: the first represents the minimum number of stops required for the journey and the second the number of the chosen trail. If the problem has no solution, the output file will contain the digit $0$.

# Constraints and clarifications

* In the input file, all distances are expressed in kilometers
* For each trail, the distance between the last spring (the farthest from the starting point) and the peak is $1$ kilometer
* $0 < k \leq 100$; 
* $0 < r \leq 20$; 
* $0 < di \leq 360$; 
* $1 \leq t \leq 10$; 
* $1 \leq u \leq 5$;

# Example 1

`popas.in`
```
3
2 3 12 5 9
1 4 2 9 7 11
3 5 2 16 7 9 8
6
2
```

`popas.out`
```
1 1
```

# Example 2

`popas.in`
```
2
1 3 12 5 9
2 3 2 7 11
1
2
```

`popas.out`
```
0
```