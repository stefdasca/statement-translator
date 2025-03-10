
# Task

Denis and George are playing darts during the national team's training camp. The target is represented as a number line, with its center at a point $K$, chosen by George. The number of points a player scores is equal to the distance from the hit point to the center. Since the two want to throw as close as possible to the center, a lower score is better.

George can set the center of the target, $K$, at one of the $M$ points given by their coach, Nea Mircea. Denis will throw $N$ times at the target. George, being a reliable teammate and knowing in advance where Denis will throw, wants to help him achieve the best possible score. Help George position the target optimally.

# Input data

The first line of the input file `darts.in` contains the integer $N$.
The second line contains $N$ coordinates $\displaystyle {x_i}$ that Denis will hit.
The third line of the file contains the integer $M$.
The fourth line contains $M$ coordinates $\displaystyle {a_i}$ from which George can choose.

# Output data

The first line of the output file `darts.out` should contain two numbers: the index (starting from 0) of the best center and its score. If there are multiple solutions with the minimum score, choose the one with the smallest index.

# Constraints and clarifications

* $1 \leq N, M \leq  300 \ 000$;
* $0 \leq \displaystyle {x_i}, \displaystyle {a_i} \leq  10^9$;

|# | Score | Constraints|
| - | - | ------------|
|0|0|Examples.|
|1|12|$N \leq 1 \ 000$|
|2|46|$N \leq 100 \ 000$|
|3|42|No additional constraints|

# Example 1

`darts.in`
```
4
4 0 3 1 
3
0 2 3 
```

`darts.out`
```
1 6
```

## Explanation

The center with index 1 has a score of 6: $|2 - 4| + |2 - 0| + |2 - 3| + |2 - 1| = 6$.

# Example 2

`darts.in`
```
7
0 4 8 9 2 6 7 
5
1 0 3 4 7 
```

`darts.out`
```
4 19
```
